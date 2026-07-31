# Parameter Layer — Phase 0 Spec

Session: param-layer-phase0. Base: `param-layer` @ `5f8c413` (guard commit).
Goal: extract every legal/regulatory literal from the retirement engine into a
versioned, cited, human-verified parameter file; refactor the engine to read
parameters and personal inputs from data files; prove content-identical output.
Design basis: `Versioned Legal Parameter Layer` survey §2 (envelope + typed
payload), Stage 0 scope.

HARD RULES for the entire session:
- **No value written from model memory.** Every parameter value comes from the
  reference engine (`engine/retirement/build_v2.py`, local-only) for the
  *number*, and from a primary authority for the *citation*. If those disagree,
  STOP and flag — do not resolve silently.
- **No real personal data in any committed file.** This repo is PUBLIC. The
  reference engine's embedded balances and birth year are owner-attested
  FICTITIOUS example values (attested 2026-07-31) and may appear in
  `inputs.example.json`. Real inputs, if and when the owner supplies them,
  live only in gitignored `*.local.json`. Before EVERY commit:
  `git diff --cached` and inspect for values outside the attested example set.
- Citations obey the skill's three-source rule (authority map, reference
  tables, or retrieved text) but parameter records cite **primary authority**
  (IRC/Notice/CMS release/RCW), not the skill's tables.

## Data planes

1. **Legal parameters — committable.** `engine/retirement/parameters.json`.
   One record per parameter per validity window, envelope fields mandatory:
   `parameter_id`, `valid_from`/`valid_to`, `recorded_at`/`superseded_at`,
   `correction_of`, `status` (active|expected|terminated|superseded),
   `jurisdiction`, `provenance` {`citation` (pin-cite), `source_url`,
   `authority_level` (statute|regulation|agency_guidance), `retrieved_at`,
   `source_hash` (sha256 of retrieved text)}, `verification` {`verified_by`,
   `verified_on`}, `payload`. Payload types for Phase 0: `scalar`
   {value, unit, tax_year} and `rule` {expression, inputs, citation-anchored
   description} — nothing more until a parameter demands it.
   Corrections are new records via `correction_of`; records are never edited.
2. **Personal inputs — local only.** `engine/retirement/inputs.local.json`
   (gitignored by pattern `/engine/retirement/*.local.json`): opening
   balances, birth year, deferral/employer split, escalation, return/inflation/
   indexation assumptions, SWR settings, conversion assumptions, filing status.
   Committed twin: `inputs.example.json` carrying the reference engine's
   embedded values verbatim (owner-attested fictitious), same schema — so the
   identity test is reproducible from the committed tree alone.

## Parameter scope (from the reference engine's literal inventory)

TY2026 402(g) elective deferral; age-50+ catch-up; ages-60–63 enhanced
catch-up; 415(c) annual additions (all: IRS Notice 2025-67, FINAL);
IRMAA first-tier MAGI threshold MFJ and single (CMS 2026 release, FINAL);
WA capital-gains excise base rate 7% and additional 2.9% > $1M post-deduction
(RCW 82.87.040 as amended by ESSB 5813 §101); WA CG standard deduction
(TY2025 $278,000 — TY2026 record `status: expected` + VERIFY, per the
skill's quick-reference flag); RMD applicable age rule (birth ≥1960 → 75,
else 73; SECURE 2.0 §107 amending IRC §401(a)(9)) as a `rule` payload.
Model assumptions (indexation %, returns, inflation, SWR) are NOT legal
parameters — they move to plane 2. If extraction surfaces a literal not
listed here, classify it (legal → plane 1 with full envelope; personal/model
→ plane 2) and record the addition in the session report.

## Engine refactor

- `engine/retirement/build.py` (committed): successor of `build_v2.py` with
  ZERO legal literals and ZERO personal literals — every such value read from
  the two data files. Structure, formulas, formatting otherwise unchanged.
- Fail-closed: a parameter lookup for a date with no `active` record raises
  with the `parameter_id`; no defaults, no fallthrough.
- Parameter access is by `parameter_id` + as-of date (model start year).

## Acceptance test (the gate)

`engine/retirement/test_identity.py` (committed): builds the workbook twice —
reference `build_v2.py` (its example values are embedded) and new `build.py`
reading `inputs.example.json`, which mirrors those embedded values verbatim —
and
compares **content**, not container bytes: every sheet, every cell's value,
formula string, and number format. Zip-container metadata (timestamps) is
excluded by design; a naive byte diff would fail dishonestly. Test passes ⇔
zero cell-level differences. The test reads personal data only at runtime,
locally; it commits nothing and prints no personal values in failure output
(report cell addresses and a diff category, not contents, for input-derived
cells).

## Executor boundary

Touch only: `engine/`, `.gitignore`, `plans/` (this file). NO `plugins/`
files, NO `EVAL-RUNBOOK.md`, NO `evals/`. Wiring the skill to the parameter
layer is a later phase with its own eval implications.

## Deferred (recorded, not built)

Source-text hash-diff monitoring jobs; fail-closed presentation gate in the
skill; authority-level review-cadence tags; graduated-schedule and duration
payload types; multi-state parameter namespaces beyond `us` / `us-wa`.

## Process

Logical commits (spec / gitignore pattern / schema+parameters / example
inputs / engine / test). `py -3.12 scripts/check.py` before each commit.
Push `param-layer`; verify remote SHA. DO NOT merge to main. SESSION REPORT:
standard template + PUSHED line + the literal-classification table (every
literal in build_v2.py → plane 1 record id, plane 2 key, or structural
constant) + identity-test output summary.
