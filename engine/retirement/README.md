# Retirement engine — the parameter layer

The workbook builder split into two data planes plus an engine that holds
neither.

| File | Plane | Committed? |
|---|---|---|
| `parameters.json` | 1 — legal parameters, cited and versioned | yes |
| `parameters.schema.json` | 1 — the envelope's normative shape | yes |
| `retrieved-text/` | 1 — evidence the hashes cover | yes |
| `paramlayer.py` | 1 — loader, validation, two access modes | yes |
| `inputs.local.json` | 2 — a real household's inputs | **never** |
| `inputs.example.json` | 2 — attested fictitious twin | yes |
| `inputs.schema.json` | 2 — the input shape | yes |
| `build.py` | engine — zero legal, zero personal literals | yes |
| `test_identity.py` | the gate | yes |
| `build_v2.py` | reference fixture | **never** (gitignored) |

## Why split at all

The reference engine mixed two kinds of value in one Python file: legal
parameters that change on someone else's schedule and need citations, and
personal figures that can never enter a public repo. Mixed, the file could not
be committed, its numbers could not be audited against authority, and nothing
noticed when a limit went stale.

The split is not only about the cells. A note reading `$218,000 MFJ / $109,000
single` is as much a legal literal as the formula beside it, and a header
reading `178,740 + 44,594.68` is personal data in prose. Both are composed at
build time from the record or the input.

## Running it

```bash
py -3.12 engine/retirement/build.py
```
Uses `inputs.local.json` when present, else `inputs.example.json`. Override with
`--inputs`, `--out`, `--parameters`.

Validate the records and recompute every stored hash:
```bash
py -3.12 engine/retirement/paramlayer.py --verify-hashes
```

Run the gate:
```bash
py -3.12 engine/retirement/test_identity.py
```
Exit `0` identical, `1` differences, `2` skipped because the reference fixture
is absent. Two is not zero deliberately — `build_v2.py` is gitignored, so a
fresh clone lacks it, and a skip that exited `0` would report success while
comparing nothing.

## Reading a parameter

```python
reg.as_of("us.irc.402g.elective_deferral", 2026)   # fail-closed
reg.latest_published("us-wa.rcw82_87.standard_deduction")  # value + validity end
```

`as_of` raises if no active record covers the date, naming the `parameter_id`.
There is no default for a legal parameter. `latest_published` exists for the two
parameters this model must project *past*: it returns the validity end alongside
the value, so extrapolating with a plane-2 indexation assumption is a visible
act rather than an accident. Records with `status: "expected"` are never
returned by either — an expected record says "an amount exists and we have not
recorded it".

## What provenance claims, and what it doesn't

- `retrieval_status` is paired. `not_retrieved` ⇒ `source_hash` and
  `retrieved_at` both null, no `hash_scope`. `retrieved` ⇒ all present.
- `hash_scope` says *what* was hashed. Everything here is
  `tool_extracted_text`: the sha256 covers a file under `retrieved-text/`, not
  the publisher's bytes. It detects drift in what we recorded, not in the
  source. All of it is queued for a `raw_source` upgrade.
- `valid_from_basis` says what the validity start rests on — `retrieved`,
  `provision_text` (the codified provision's own operative language),
  `repo_verified` (a human-verified file in this repo, named with its own
  verification date), or `unretrieved`, in which case `valid_from` is null and
  **no lower bound is asserted**.
- `confidence` mirrors the repo skill's FINAL/VERIFY convention, and a `verify`
  must say what is outstanding.
- `verification` carries no human name, because **no human has signed off**.
  Every record is `pending_owner_signoff`.

### Backfill queue

Landing as *superseding records*, never edits:

1. Every `not_retrieved` record — needs `source_hash` + `retrieved_at`.
2. Every `retrieved` record — needs a `raw_source` hash to replace the
   tool-extracted one.
3. Every `unretrieved` `valid_from_basis` — needs a real effective date.
   Until then `as_of()` treats null as unbounded below, which is unsound for
   historical queries and safe here only because this engine queries the model
   start year forward.
4. `us-wa.rcw82_87.standard_deduction` TY2026 — from WA DOR.
5. `us-wa.rcw83_100.estate_exclusion_indexed` — the indexed early-2026 figure.
6. `us.irc.401a9.rmd_applicable_age` — the SECURE 2.0 §107(b) effective-date
   clause, and the Treasury regulation resolving the 1959-cohort overlap.

## The 1959 overlap

Worth reading `us.irc.401a9.rmd_applicable_age`'s `authority_note`. The
retrieved text of 26 U.S.C. §401(a)(9)(C)(v) has two clauses that **both** reach
someone born in 1959: they attain 73 in 2032 (before Jan 1 2033) and 74 in 2033
(after Dec 31 2032). The engine's `IF(birth_year>=1960,75,73)` silently picks
one horn — that is Treasury's administrative resolution of a drafting defect,
not bare statute, and the resolving regulatory pin is flagged VERIFY.

The formula had encoded an interpretive choice as if it were law. Making that
seam visible is the point of the layer.
