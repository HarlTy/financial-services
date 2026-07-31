"""Plane 1 access: versioned, cited legal parameters.

Two access modes, deliberately different:

  as_of(parameter_id, when)   FAIL-CLOSED. Returns the payload of the single
                              active record whose validity window contains
                              `when`. No record, or more than one, raises.
                              There are no defaults and no fallthrough.

  latest_published(parameter_id)
                              Returns (payload, valid_to) for the newest active
                              record. Use this ONLY where a model must project
                              past the last published amount -- the caller then
                              has both the amount and the date its authority
                              runs out, so extrapolating is a visible, labelled
                              act rather than a silent one.

Records with status "expected" are never returned by either mode. An expected
record says "an amount exists and we have not recorded it"; handing it to a
calculation would defeat the point.

CAVEAT -- unretrieved lower bounds. A record whose statutory effective date was
not retrieved carries valid_from: null and provenance.valid_from_basis:
"unretrieved". Null is treated as unbounded below, so as_of() will happily
resolve such a parameter for a year BEFORE the law existed. That is unsound for
historical queries and is only safe here because this engine queries the model
start year forward. The backfill queue in README.md closes it: every
"unretrieved" basis is queued for upgrade, landing as a superseding record.

Validation runs at load. It is not decoration: the invariants encode promises the
records make about themselves (no half-retrieved provenance, no human name on an
unsigned verification, no two active records claiming the same day), and a
violation is a data defect that must stop the build rather than be queried
around. parameters.schema.json is the normative statement of the same rules for
external tools; this module reimplements them so the engine needs no third-party
dependency to fail closed.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARAMETERS = HERE / "parameters.json"
RETRIEVED_TEXT = HERE / "retrieved-text"

_STATUSES = {"active", "expected", "terminated", "superseded"}
_LEVELS = {"statute", "regulation", "agency_guidance"}
_RETRIEVAL = {"retrieved", "not_retrieved"}
_HASH_SCOPES = {"tool_extracted_text", "raw_source"}
_BASES = {"retrieved", "provision_text", "repo_verified", "unretrieved"}
_UNITS = {"usd", "rate", "years", "age", "divisor"}


class ParameterError(Exception):
    """Base for every failure in this module."""


class ParameterDataError(ParameterError):
    """parameters.json violates an invariant. The build must not continue."""


class ParameterNotFound(ParameterError):
    """No active record covers the requested parameter and date."""

    def __init__(self, parameter_id: str, when):
        self.parameter_id = parameter_id
        self.when = when
        super().__init__(
            f"no active record for parameter_id={parameter_id!r} as of {when}. "
            f"Fail-closed: there is no default for a legal parameter."
        )


class ParameterAmbiguous(ParameterError):
    """More than one active record covers the date -- a data defect, not a tie."""

    def __init__(self, parameter_id: str, when, count: int):
        super().__init__(
            f"{count} active records for parameter_id={parameter_id!r} cover {when}. "
            f"Overlapping validity windows are a data defect; refusing to pick one."
        )


def _as_date(when) -> _dt.date:
    if isinstance(when, _dt.date):
        return when
    if isinstance(when, int):
        return _dt.date(when, 1, 1)
    if isinstance(when, str):
        return _dt.date.fromisoformat(when)
    raise TypeError(f"unsupported as-of value: {when!r}")


def _parse(value):
    return None if value is None else _dt.date.fromisoformat(value)


def body_sha256(path: Path) -> str:
    """Hash of a retrieved-text file's body: everything after the '---' line,
    with line endings normalised to LF so a checkout on either platform agrees."""
    raw = path.read_bytes().replace(b"\r\n", b"\n")
    marker = b"\n---\n"
    i = raw.find(marker)
    if i < 0:
        raise ParameterDataError(f"{path.name}: no '---' separator")
    return hashlib.sha256(raw[i + len(marker):]).hexdigest()


class Registry:
    def __init__(self, doc: dict, source: Path):
        self.source = source
        self.schema_version = doc.get("schema_version")
        self.records = doc.get("records") or []
        self._validate()

    # -- validation --------------------------------------------------------

    def _validate(self) -> None:
        errors: list[str] = []

        def bad(i, msg):
            pid = self.records[i].get("parameter_id", "<missing id>")
            errors.append(f"record {i} ({pid}): {msg}")

        for i, r in enumerate(self.records):
            for key in ("parameter_id", "jurisdiction", "valid_from", "valid_to",
                        "recorded_at", "superseded_at", "correction_of", "status",
                        "provenance", "verification", "payload"):
                if key not in r:
                    bad(i, f"missing envelope field {key!r}")
            if errors:
                continue

            if r["status"] not in _STATUSES:
                bad(i, f"status {r['status']!r} not one of {sorted(_STATUSES)}")

            vf, vt = _parse(r["valid_from"]), _parse(r["valid_to"])
            if vf and vt and vf > vt:
                bad(i, f"valid_from {vf} is after valid_to {vt}")

            p = r["provenance"]
            if p.get("authority_level") not in _LEVELS:
                bad(i, f"authority_level {p.get('authority_level')!r} invalid")
            if p.get("retrieval_status") not in _RETRIEVAL:
                bad(i, f"retrieval_status {p.get('retrieval_status')!r} invalid")
            if p.get("valid_from_basis") not in _BASES:
                bad(i, f"valid_from_basis {p.get('valid_from_basis')!r} invalid")

            # No half-states in retrieval provenance.
            if p.get("retrieval_status") == "not_retrieved":
                if p.get("source_hash") is not None or p.get("retrieved_at") is not None:
                    bad(i, "not_retrieved but source_hash/retrieved_at is populated")
                if "hash_scope" in p or "hash_source_file" in p:
                    bad(i, "not_retrieved but carries a hash_scope/hash_source_file")
            else:
                if not p.get("source_hash") or not p.get("retrieved_at"):
                    bad(i, "retrieved but source_hash/retrieved_at is missing")
                if p.get("hash_scope") not in _HASH_SCOPES:
                    bad(i, "retrieved but hash_scope is missing or invalid")
                if not p.get("hash_source_file"):
                    bad(i, "retrieved but hash_source_file is missing")

            # A validity start and its basis are paired.
            if p.get("valid_from_basis") == "unretrieved":
                if r["valid_from"] is not None:
                    bad(i, "valid_from_basis is 'unretrieved' but valid_from is set")
            elif r["valid_from"] is None:
                bad(i, f"valid_from is null but basis is {p.get('valid_from_basis')!r}")

            if p.get("valid_from_basis") == "repo_verified":
                if not p.get("repo_source") or not p.get("repo_source_verified_on"):
                    bad(i, "repo_verified basis without repo_source and its verification date")

            v = r["verification"]
            if v.get("status") == "pending_owner_signoff":
                if v.get("verified_by") is not None or v.get("verified_on") is not None:
                    bad(i, "pending_owner_signoff but a verifier is named")
            elif v.get("status") == "owner_verified":
                if not v.get("verified_by") or not v.get("verified_on"):
                    bad(i, "owner_verified without a named verifier and date")
            else:
                bad(i, f"verification.status {v.get('status')!r} invalid")

            pay = r["payload"]
            kind = pay.get("type")
            if kind == "scalar":
                if pay.get("unit") not in _UNITS:
                    bad(i, f"payload.unit {pay.get('unit')!r} invalid")
                if "value" not in pay:
                    bad(i, "scalar payload without a value")
            elif kind == "rule":
                if not pay.get("expression") or not pay.get("description"):
                    bad(i, "rule payload without expression/description")
            else:
                bad(i, f"payload.type {kind!r} is not a Phase 0 type (scalar|rule)")

            if r["status"] == "expected" and pay.get("value") is not None:
                bad(i, "an 'expected' record must not carry a value")

        # Overlapping active windows for one id are a defect -- catch at load,
        # not at the query that happens to hit the overlap.
        by_id: dict[str, list[tuple]] = {}
        for i, r in enumerate(self.records):
            if r.get("status") == "active" and not r.get("superseded_at"):
                by_id.setdefault(r["parameter_id"], []).append(
                    (i, _parse(r["valid_from"]), _parse(r["valid_to"]))
                )
        for pid, windows in by_id.items():
            for a in range(len(windows)):
                for b in range(a + 1, len(windows)):
                    (_, af, at_), (_, bf, bt) = windows[a], windows[b]
                    lo_ok = at_ is None or bf is None or bf <= at_
                    hi_ok = bt is None or af is None or af <= bt
                    if lo_ok and hi_ok:
                        errors.append(
                            f"{pid}: two active records have overlapping validity windows"
                        )

        if errors:
            raise ParameterDataError(
                f"{self.source.name} failed validation:\n  - " + "\n  - ".join(errors)
            )

    # -- access ------------------------------------------------------------

    def _active(self, parameter_id: str) -> list[dict]:
        return [r for r in self.records
                if r["parameter_id"] == parameter_id
                and r["status"] == "active"
                and not r["superseded_at"]]

    def as_of(self, parameter_id: str, when) -> dict:
        """Fail-closed lookup. Returns the payload; raises if none or many."""
        day = _as_date(when)
        hits = []
        for r in self._active(parameter_id):
            vf, vt = _parse(r["valid_from"]), _parse(r["valid_to"])
            if (vf is None or vf <= day) and (vt is None or day <= vt):
                hits.append(r)
        if not hits:
            raise ParameterNotFound(parameter_id, day.isoformat())
        if len(hits) > 1:
            raise ParameterAmbiguous(parameter_id, day.isoformat(), len(hits))
        return hits[0]["payload"]

    def value_as_of(self, parameter_id: str, when):
        """as_of(), narrowed to a scalar's value."""
        payload = self.as_of(parameter_id, when)
        if payload.get("type") != "scalar":
            raise ParameterError(
                f"{parameter_id} is a {payload.get('type')!r} payload, not a scalar"
            )
        if payload.get("value") is None:
            raise ParameterError(f"{parameter_id} carries no value as of {when}")
        return payload["value"]

    def latest_published(self, parameter_id: str) -> tuple[dict, str | None]:
        """Newest active record's payload plus the date its validity ends.

        For parameters a model must project past -- the caller gets the amount
        AND the date its authority runs out, so the extrapolation is explicit.
        """
        hits = self._active(parameter_id)
        if not hits:
            raise ParameterNotFound(parameter_id, "latest_published")
        hits.sort(key=lambda r: (r["valid_from"] or "0000-00-00"))
        newest = hits[-1]
        return newest["payload"], newest["valid_to"]

    def record_for(self, parameter_id: str, when) -> dict:
        """The whole record, for callers that need provenance (citations,
        status flags) rather than just the number."""
        day = _as_date(when)
        for r in self._active(parameter_id):
            vf, vt = _parse(r["valid_from"]), _parse(r["valid_to"])
            if (vf is None or vf <= day) and (vt is None or day <= vt):
                return r
        raise ParameterNotFound(parameter_id, day.isoformat())

    def records_for(self, parameter_id: str) -> list[dict]:
        """Every record for an id, any status -- including 'expected' ones."""
        return [r for r in self.records if r["parameter_id"] == parameter_id]

    # -- hash verification -------------------------------------------------

    def verify_hashes(self) -> tuple[list[str], list[str]]:
        """Recompute every stored hash. Returns (failures, orphaned files)."""
        failures, referenced = [], set()

        def check(pid, rel, expected):
            referenced.add(rel)
            path = HERE / rel
            if not path.exists():
                failures.append(f"{pid}: missing {rel}")
                return
            actual = body_sha256(path)
            if actual != expected:
                failures.append(
                    f"{pid}: {rel} hashes {actual[:12]}..., "
                    f"record says {expected[:12]}..."
                )

        for r in self.records:
            p = r["provenance"]
            if p["retrieval_status"] != "retrieved":
                continue
            check(r["parameter_id"], p["hash_source_file"], p["source_hash"])
            for ev in p.get("supporting_evidence", []):
                check(r["parameter_id"], ev["file"], ev["source_hash"])
        orphans = []
        if RETRIEVED_TEXT.is_dir():
            for f in sorted(RETRIEVED_TEXT.iterdir()):
                if f.suffix == ".txt" and f"retrieved-text/{f.name}" not in referenced:
                    orphans.append(f.name)
        return failures, orphans


_registry: Registry | None = None


def load(path: Path | None = None) -> Registry:
    global _registry
    target = path or PARAMETERS
    if _registry is None or _registry.source != target:
        _registry = Registry(json.loads(target.read_text(encoding="ascii")), target)
    return _registry


def _main(argv: list[str]) -> int:
    reg = load()
    print(f"loaded {len(reg.records)} records "
          f"({len({r['parameter_id'] for r in reg.records})} parameter ids), "
          f"schema {reg.schema_version} -- validation passed")
    if "--verify-hashes" in argv:
        failures, orphans = reg.verify_hashes()
        for f in failures:
            print(f"HASH MISMATCH  {f}")
        for o in orphans:
            print(f"ORPHAN         retrieved-text/{o} is referenced by no record")
        if failures:
            return 1
        print("all stored hashes recomputed and matched")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
