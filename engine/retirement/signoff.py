#!/usr/bin/env python3
"""Owner sign-off tool for the parameter layer.

Updates ONLY the verification block of selected records:
    verified_by, verified_on, status -> owner_verified, method (optional).
Everything else is guarded byte-for-byte. Any selector error aborts the whole
run with no changes written. Records are selected by parameter_id, with an
'@ valid_from' suffix required when one id has multiple records.

Usage:
  py -3.12 signoff.py --by "NAME" --on YYYY-MM-DD --ids-file FILE
                      [--method TEXT] [--dry-run]
ids-file: one selector per line; '#' starts a comment.
  us.irc.402g.elective_deferral
  us-wa.rcw82_87.standard_deduction @ 2025-01-01
"""
from __future__ import annotations
import argparse, copy, datetime, json, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARAMS = HERE / "parameters.json"


def load_selectors(path: Path) -> list[tuple[str, str | None]]:
    out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if "@" in line:
            pid, vf = (part.strip() for part in line.split("@", 1))
            out.append((pid, vf))
        else:
            out.append((line, None))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--by", required=True)
    ap.add_argument("--on", required=True)
    ap.add_argument("--ids-file", required=True, type=Path)
    ap.add_argument("--method", default=None)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    datetime.date.fromisoformat(args.on)  # validates format
    if not args.by.strip():
        sys.exit("refusing an empty --by")

    doc = json.loads(PARAMS.read_text(encoding="utf-8"))
    records = doc["records"]
    originals = copy.deepcopy(records)

    errors, signed = [], []
    for pid, vf in load_selectors(args.ids_file):
        hits = [r for r in records if r["parameter_id"] == pid
                and (vf is None or r.get("valid_from") == vf)]
        if len(hits) != 1:
            errors.append(f"{pid}{' @ ' + vf if vf else ''}: "
                          f"{len(hits)} matches (need exactly 1; disambiguate with '@ valid_from')")
            continue
        rec = hits[0]
        ver = rec["verification"]
        if ver.get("status") != "pending_owner_signoff":
            errors.append(f"{pid}: status is {ver.get('status')!r}, not pending_owner_signoff")
            continue
        ver["verified_by"] = args.by
        ver["verified_on"] = args.on
        ver["status"] = "owner_verified"
        if args.method:
            ver["method"] = args.method
        signed.append(f"{pid}{' @ ' + vf if vf else ''}")

    if errors:
        print("ABORT -- nothing written:")
        for e in errors:
            print("  ", e)
        return 1

    # Integrity guard: nothing outside 'verification' may differ, on any record.
    for before, after in zip(originals, records):
        b = {k: v for k, v in before.items() if k != "verification"}
        a = {k: v for k, v in after.items() if k != "verification"}
        if b != a:
            print("ABORT -- non-verification change detected on", before["parameter_id"])
            return 1

    # Validate the result through the loader before touching the real file.
    sys.path.insert(0, str(HERE))
    import paramlayer  # noqa: E402
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False,
                                     dir=HERE, encoding="utf-8") as tf:
        json.dump(doc, tf, indent=2, ensure_ascii=False)
        tf.write("\n")
        tmp = Path(tf.name)
    try:
        paramlayer.load(tmp)
    finally:
        if args.dry_run:
            tmp.unlink()
        else:
            tmp.replace(PARAMS)

    print(("DRY RUN -- would sign" if args.dry_run else "signed"),
          len(signed), "record(s) as", repr(args.by), "on", args.on)
    for s in signed:
        print("  ", s)
    return 0


if __name__ == "__main__":
    sys.exit(main())
