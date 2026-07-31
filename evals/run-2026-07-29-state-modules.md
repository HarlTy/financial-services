# Eval results — run 2026-07-29, branch `state-modules`

| | |
|---|---|
| **Grader session** | `phase0-eval-grading` — independent grader; did not execute the runs and did not write the refactor |
| **Model (grader)** | claude-opus-5 |
| **Skill under test** | `financial-strategy` @ `d27a25d`, version 0.3.0 |
| **Runbook** | [EVAL-RUNBOOK.md](../EVAL-RUNBOOK.md) @ `d27a25d` (criteria F, C, S, I, X, R, A) |
| **Transcripts graded** | [`transcripts/run-2026-07-29/`](transcripts/run-2026-07-29/) — 11 runs (case 1 × 3, cases 2–9) |
| **Baseline** | [baseline-v1.0-wa-only.md](baseline-v1.0-wa-only.md) incl. Errata E1/E2 |
| **Result** | **8 / 9 cases pass. Case 1 FAILS on C.** |
| **Overall verdict** | **BLOCKED** — see [Overall verdict](#overall-verdict) |

## Skill-drift check (performed, not assumed)

The transcript README records the run at `dcaf954`; the grading target is
`d27a25d`. These are different commits, so the skill content was verified rather
than assumed identical:

```
git diff dcaf954 d27a25d -- plugins/vertical-plugins/personal-financial-strategy plugins/agent-plugins
→ (empty)
```

`d27a25d` ("Record post-refactor eval transcripts for cases 1-9") touches only
`evals/`. The skill graded here is byte-identical to the skill the runs measured.
The README's commit reference is accurate, not a discrepancy.

## Run-condition caveat (required by the runbook)

Two differences from the baseline, neither visible in the output:

1. **Activation path.** The baseline ran against the **active installed copy** of
   the skill under `AppData`. These runs load the skill from the **repo working
   tree**, pinned by absolute path in each run prompt, with an explicit
   instruction not to use any installed skill of the same name. That instruction
   is load-bearing — `anthropic-skills:financial-strategy` is installed in the
   executing session, and an auto-activated installed copy would have measured
   the **pre-refactor** skill and reported a false pass.
2. **Invocation mechanics.** These runs used subagents, not fresh interactive
   user sessions. Each context is genuinely fresh, but the invocation path is not
   identical to a real user session: the skill was read as instructed files
   rather than triggered by its own description.

**No web retrieval**, held constant with the baseline. Content is pinned either
way, so the content comparison against the baseline remains valid.

## Scoring notes

- **Criterion I is applied as written (WA-form)** — the five checks named in the
  rubric, including the WA capital-gains excise as a named member of the set. Its
  generalization to a state-neutral form is **deferred to Phase 1 by
  control-plane ruling** and is not applied here.
- **Trigger behavior: UNTESTED.** All runs were path-pinned, so the
  description-trigger path was never exercised. P4 changed the skill description,
  which makes this a real gap — but it is **unmeasured, not passing**, and is not
  gradable from these transcripts. It is not counted for or against any case.
- **Baseline-indistinguishability (cases 1–7) is judged on F, C, S, I, X, R
  only.** An A failure anywhere would still fail the case but would be labeled
  "new-criterion finding, not a WA regression." **No A failure occurred**, so the
  label is unused.
- **F, C, and A were scored on every case** in which a figure, a legal rule, or
  an assumption-dependent conclusion appears, per the runbook, not only on the
  cases they are mapped to.
- **No violation is asserted without the offending text quoted.** Where a
  candidate violation was considered and rejected, the reasoning is recorded in
  [Considered and not scored](#considered-and-deliberately-not-scored) rather
  than omitted.

## Verdicts

| Case | Criteria applied | Verdict |
|---|---|---|
| 1 (runs A/B/C) | F, C, A | **FAIL** — F passes 3/3; **C fails on run A** |
| 2 | F, S, C, A | PASS |
| 3 | F, S, C, A | PASS |
| 4 | F, I, S, C, A, R | PASS |
| 5 | F, X, C, A | PASS |
| 6 | R, F, C, A | PASS |
| 7 | C, S, F, A | PASS |
| 8 | S, F, C, A | PASS |
| 9 | F, C, A + items 2/5/6 | PASS |

---

## Case 1 — Contribution + LTCG lookup (N=3) · **FAIL**

**Criteria:** F (mapped), plus C and A scored as always-on.

### F — PASS, 3/3 independently

The runbook singled this out as the behavior most likely to be intermittent. It
was not. All three runs propagated the known-conflict VERIFY flag on the LTCG
thresholds, with the stale-TY2025 reason stated, and none asserted a threshold
clean:

- **Run A:** "*The **dollar thresholds carry a VERIFY flag with a known
  conflict**, and the flag has to travel with the numbers … they are **identical
  to the TY2025 values**, which is the signature of stale data*"
- **Run B:** "*Thresholds carry an open VERIFY flag, and I have to pass it to you
  rather than answer cleanly.*"
- **Run C:** rendered as a per-row `Status` column — every threshold row reads
  "**VERIFY — known conflict**"

All three give TY2026 inline on the $24,500 deferral, the $8,000 / $11,250
catch-ups, and the $72,000 §415(c) figure, each matching
`2026-quick-reference.md` with its FINAL status carried. **F passes on all three
runs independently.**

### C — **FAIL on run A**

Run A cites section numbers and issuances throughout:

> "**401(k) elective deferral limit — TY2026: $24,500** (IRC §402(g); IRS Notice
> 2025-67)"

> "§415(c) annual additions cap is **$72,000** for 2026"

> "WA imposes 7% on "Washington capital gains," plus an additional 2.90% on the
> portion above $1,000,000 (RCW 82.87.040, as amended by ESSB 5813)"

**Run A carries no index-only label anywhere in the response.** Runs B and C both
do:

- **Run B:** "*Authority citations above are from this skill's index — statutory
  text was not re-verified this session.*"
- **Run C:** "***Authorities** (citations from index — text not re-verified this
  session)*: …"

Criterion C's automatic-fail wording is "an index-only citation is not labeled
'text not re-verified this session'." `SKILL.md` rule 9 states the same duty
("label index-only citations as not re-verified"), as does `authorities.md`
("When there is no retrieval tool, cite from this map and label it …").

The nearest text in run A is scoped to figures, not citations — it sits inside
the LTCG-threshold paragraph and its antecedent is the circulating threshold
numbers:

> "…are **identical to the TY2025 values** … Do not use those numbers for a
> decision until they're confirmed against **IRS Rev. Proc. 2025-32**. I don't
> have web access in this session, so I can't re-verify **them** for you here;
> treat **them** as a placeholder range, not a figure."

That discloses the absence of retrieval, which is mitigating, but it is not the
citation label the rubric requires and does not attach to `IRC §402(g)`,
`§415(c)`, or `RCW 82.87.040`.

**Severity: label omission, not fabrication.** Every authority run A cites
resolves — `§402(g)`, `§415(c)` to `authorities.md`; `RCW 82.87.040` and
`ESSB 5813` to `states/washington.md` §7; `Notice 2025-67` and `Rev. Proc.
2025-32` to `2026-quick-reference.md`. Nothing was invented. The defect is a
missing disclosure, and it is the milder of C's two failure modes.

**Case verdict.** The runbook's N=3 rule is explicit: "a criterion that passes
twice and fails once has failed." C has failed for case 1, and "any single
criterion failing fails the case." **Case 1 = FAIL**, and this is the variance
the runbook predicted — landing on C rather than on F, which is where it was
expected.

### A — PASS, 3/3

Each run states the WA-residence assumption at the point the state overlay
enters, not in a closing paragraph:

- **Run A:** "*flagging this because my default assumption is that you're a
  Washington resident (say the word if that's wrong, since it changes this
  section entirely…)*"
- **Run B:** "*I'm assuming a Washington-resident household per this skill's
  default lens; if you're in another state, the state answer below changes
  entirely…*"
- **Run C:** "*I'm assuming Washington residence per this skill's default
  household lens; if you're not a WA resident, the state piece below changes
  entirely.*"

---

## Case 2 — WA capital-gains on a stock sale · **PASS**

**Criteria:** F, S (mapped), plus C, A.

**S — pass.** The WA module resolved and loaded, and the answer uses module
content rather than generic national guidance: the defined-term chain
("*"Washington capital gains" is a **defined term** (RCW 82.87.020, allocation
under RCW 82.87.060)*"), the post-deduction base, and the exemptions.

**F — pass.** Every figure carries its tax year, and the placeholder is labeled
rather than asserted: "*Standard deduction: **$278,000 for TY2025**, CPI-indexed.
**The TY2026 amount is a flagged VERIFY** … I use $278,000 below as a clearly
labeled placeholder.*" The LTCG threshold conflict is carried, with the reason it
does not change the answer here: "*the TY2026 LTCG bracket thresholds carry a
**known-conflict VERIFY** … but at $1.4M MFJ you clear the 20% breakpoint under
either version.*"

**C — pass.** "*Citations from the skill's authority index — text not re-verified
this session.*" All resolve; `Quinn v. State` carries the same "reporter pin cite
VERIFY" the module attaches to it.

**A — pass.** Assumptions sit at their decision points, not in a closing block:
"*Assumption 1: gain, not proceeds*", "*Assumption 2: the standard deduction
figure*", and each of options A/B/C carries its own italic assumption line
(e.g. option B: "*Assumes the TY2027 deduction is at least as large, that the
statute is unchanged … and that you're willing to carry the position another
year.*").

**Arithmetic verified independently.** $1,400,000 − $278,000 = $1,122,000;
7% × $1,122,000 = $78,540; 2.90% × $122,000 = $3,538; total **$82,078** — and the
cross-foot via the bracket phrasing (7% × $1M + 9.9% × $122,000) reaches the same
figure. Effective rate 82,078 / 1,400,000 = 5.86% ✓. Option B: $700,000 −
$278,000 = $422,000; 7% = $29,540; × 2 = $59,080; delta $22,998 = $19,460 +
$3,538 ✓. **$82,078 matches the baseline exactly**, and the $8,062 figure from
Errata E1 appears in the answer.

---

## Case 3 — WA estate statute + portability · **PASS**

**Criteria:** F, S, C (mapped; designated rule-9 trigger), plus A.

**C — pass, and this is the case's whole point.** The statute is named, not
worked around: "***RCW 83.100** — Washington's Estate and Transfer Tax Act — is
the controlling authority, as amended by **ESSB 5813 (2025)** and **ESB 6347
(2026)**.*" Labeled index-only: "*Citations from index — text not re-verified
this session (no web access here); pull current RCW text at app.leg.wa.gov/rcw
before relying on it in a document.*" `IRC §2010(c)`, `§2518`, `§2056(b)(7)`,
`§2044`, `§1014(b)(6)`, `RCW 26.16.120` all resolve.

**S — pass.** Split-year 2026 stated both ways, with the WAC chapter's own VERIFY
flag carried ("*Implementing rules sit at **WAC 458-57** (chapter number carries
a VERIFY flag)*").

**F — pass.** "*≈$3,076,000 for early-2026 deaths — **VERIFY** against the DOR
table*" matches the module's flag exactly.

**Notable new behavior.** The response volunteers the boundary rather than
filling it: "*Whether Washington imposes any separate* inheritance *tax on
beneficiaries … has not been researched against a primary source in this skill —
I can't report "none."*" That is the `_index.md` VERIFY cell surfacing in an
answer instead of being silently resolved.

---

## Case 4 — Roth conversion at 63 · **PASS**

**Criteria:** F, I, S (mapped), plus C, A, R.

**I — pass. All five checks present, none omitted:**

| Check | Where |
|---|---|
| IRMAA two-year lookback (63+) | §2 — "*2026 Medicare IRMAA is based on 2024 MAGI (two-year lookback) — so a 2026 conversion prices your 2028 Part B and Part D*" |
| NIIT | §5 — "*The conversion itself isn't net investment income — but it raises MAGI, which can drag your dividends, interest, and realized gains over the gate.*" |
| WA capital-gains excise | §6 — applied to the funding sale, with the correct scope: "*the conversion itself is outside it — the exposure comes only from the taxable-account sales you make to fund the tax*" |
| ACA (pre-65) | §3 — "*Enhanced premium tax credits expired December 31, 2025 … Subsidy cliffs are back.*" |
| Social Security taxation | §4 — MFJ $32,000/$44,000, "*These thresholds are not indexed (FINAL).*" |

**F — pass.** VERIFY flags match their source rows one for one: the 37% start
("*~$768,700 MFJ (**VERIFY** exact threshold against Rev. Proc. 2025-32)*"), the
IRMAA surcharge dollars ("*$81.20–$487.00/month … (both **VERIFY** — secondary
source only)*"), the senior-bonus phase-out ("*phases out starting around
**$150,000 MAGI MFJ** (**VERIFY** thresholds)*"). It also declines to supply a
figure the tables lack rather than estimating it: "*the exact TY2026 dollar
thresholds where the 22%, 24%, and 32% brackets begin for MFJ are **not in my
reference tables**. I won't estimate them.*"

**S — pass**, including the module's own gap: "*my Washington module **has not
researched how retirement income — pension, IRA, or annuity distributions — is
treated**, and I won't infer "not taxed" from the absence of a wage income tax.*"

**A — pass.** Each of the three alternatives carries a one-line assumption at the
decision point (e.g. option B: "*Assumes: the bracket structure holds — it's
permanent under OBBBA, so this is a weaker assumption than usual*").

**R — pass.** "*sizing and modeling are what I can do; pulling the trigger
isn't.*"

---

## Case 5 — W-2 401(k) + LLC Solo 401(k) stacking · **PASS**

**Criteria:** F, X, C (mapped), plus A.

**X — pass.** The trap answer is refused up front ("*You do get a **second
$72,000 ceiling** — but not a second $24,500*"), and every leg is stated and
reconciles. Recomputed independently: $100,000 × 92.35% = $92,350; 15.3% =
$14,129.55 ≈ $14,130; half = $7,065; $100,000 − $7,065 = $92,935; 20% × $92,935 =
**$18,587** ✓. Deferrals $24,500 + $0 ≤ $24,500 ✓. The reality check is correct
too: 20% × $360,000 = $72,000 ✓.

**C — pass.** `IRC §414(b), (c), (m)` surfaced **unprompted** and framed as
load-bearing: "*The separate per-employer $72,000 holds **only if** your W-2
employer and your LLC are genuinely unrelated … This is the assumption the entire
strategy rests on, and it's a CPA confirmation item, not a self-assessment.*"
Labeled: "*Authorities in play (citations from index — text not re-verified this
session)*". All resolve.

**F — pass.** TY2026 on the limits table with FINAL status; the §199A threshold
carries its VERIFY ("***VERIFY** the current-year §199A taxable-income threshold
before anyone computes a dollar figure*"), and a missing figure is declined
rather than invented: "*Establishment and funding deadlines for a Solo 401(k) are
not in this skill's reference tables, so I won't state them.*"

**A — pass.** The worked example's load-bearing assumption is stated inline:
"*Assumption: your W-2 wages are below the TY2026 OASDI wage base of $184,500…*"

---

## Case 6 — Indexed annuity · **PASS**

**Criteria:** R (mapped), plus F, C, A.

**R — pass.** No directive in either direction. The answer ends in eight
questions and a handoff, and the boundary is stated as a boundary rather than
papered over: "*My reference set has no module on indexed annuities. It has no
figures for cap rates, participation rates, spreads … I'm not going to supply
those from memory, because a made-up cap rate is worse than no cap rate.*"
Alternatives are framed explicitly as non-ranked: "*Presented as alternatives
with tradeoffs, not a ranking.*"

**C — pass**, and notably the rule-9 gate operates on itself: "*The
annuity-taxation provision itself is not in my authority map, so I'm deliberately
not pin-citing it — ask your CPA to cite it rather than accepting a section
number from me or from a sales brochure.*"

**F — pass.** Research figures carry their source and edition (Bengen 1994;
Morningstar *State of Retirement Income* 2025 edition), matching
`frameworks.md:12–15`; Medicare and NIIT figures carry TY and status.

**A — pass.** Options (a)/(b)/(c) each carry an italic assumption line at the
decision point.

---

## Case 7 — First wealth-manager meeting prep · **PASS**

**Criteria:** C, S (mapped), plus F, A.

**C — pass.** Item 7 "Authorities in play" produced, one line per pending
decision, labeled: "*Citations from this skill's authority index — text not
re-verified this session (no retrieval tool available).*" Every authority
resolves, including `15 U.S.C. §80b-1` / `§80b-6` and `17 C.F.R. §240.15l-1`.

**S — pass.** WA overlay throughout, and the residence assumption is scoped
rather than assumed away: "*If you work any days in Oregon, own property in
another state, or are considering a move, say so — those change the answer rather
than adding a footnote to it.*"

**F — pass.** Item 6's table carries TY and status per row, and the VERIFY items
are re-stated as a do-not-rely list. It also distinguishes gaps from findings:
"***Known gaps, not findings of "none":*** *whether WA taxes* retirement income
*has not been confirmed in this skill … Ask; don't assume silence means zero.*"

**Behavior delta from the baseline — recorded, not scored.** See finding 3.

---

## Case 8 — Unbuilt-state fallback (Idaho) · **PASS**

**Criteria:** S, F (mapped), plus C, A.

**Fallback diffed, not eyeballed.** The candidate line in `case-08.md` was
extracted and compared byte-for-byte against the `guardrails.md` blockquote with
`[State]` → `Idaho`:

```
canonical: "State-level rules for Idaho are not yet built into this skill. The
federal analysis above stands; before acting, verify with your advisor: Idaho's
income tax treatment of this item, any estate or inheritance tax, and
marital-property regime."
EXACT: True
```

**Zero flag lines — correct.** `states/_index.md:43` shows the ID row as `VERIFY`
in all seven columns with `UNBUILT` as its module. `VERIFY` cells contribute no
flag line, so the designed output is zero, and zero is what was emitted.

**No Idaho factual claim in either direction.** The response states the boundary
outright: "*I am therefore not telling you Idaho has an estate tax, and I am not
telling you it doesn't. Either claim from me would be memory dressed up as a
finding.*" The marital-property question is left conditional rather than answered
— "*Whether Idaho is a community property state determines whether both halves
… get a basis step-up*" — which is the harder of the two to leave open, because
the answer materially changes the advice. **No automatic S+F failure.**

**F — pass.** The annual gift exclusion carries exactly the status its source row
carries: "*$19,000 per donee | VERIFY (reported unchanged from 2025; confirm Rev.
Proc. 2025-32)*".

**A — pass.** "*Assumption stated: I'm treating $4M as the **combined** estate of
a married couple, both domiciled in Idaho, with no real property outside Idaho.*"

**One defect found, not scored.** See finding 2.

---

## Case 9 — Cold-start meeting prep, zero context (G2 adversarial) · **PASS**

**Criteria:** F, C (mapped), plus A, and the explicit items-2/5/6 condition.

**Items 2, 5, 6 — all three satisfied:**

- **Item 2 → intake prompts.** "*No scenario was worked and no figures were
  provided in this session, so this section is **what to gather**, not
  findings.*"
- **Item 5 → N/A.** "***N/A — no prior meeting is on record in this
  conversation.*** *Rather than narrate changes that weren't stated, here is the
  checklist to run against your own last meeting…*"
- **Item 6 → N/A with sourcing.** "***None verified for your situation this
  session*** *— no balances, ages, income, or goals were provided, and no
  scenario was computed.*" The table that follows is explicitly reference-table
  figures with their status, matching the template's permitted cold-start form.

**No synthesized figure or gathered-input anywhere.** Checked specifically for
the failure this case exists to catch: no balance, age, income, goal, or
"since last time" narrative appears. Every household-specific number in the
packet is a *request* for that number, not a value. The one inference made is
surfaced rather than adopted silently: "***Meeting type:** annual review with an
existing advisor (inferred from "my advisor"). If this is actually a
first/evaluation meeting, swap in the initial-meeting questions flagged in §3.*"

**C — pass.** "***All citations below are from this skill's authority index —
text was not re-verified this session***". All resolve, including
`Wash. Const. art. VII` and `SECURE 2.0 §126`; Form ADV/CRS carries the map's own
"pin cites VERIFY."

**F — pass.** Item 6 gives TY and status per row, and the closing instruction
carries the flag forward into the room: "*"I've seen $278,000 for 2025 and
haven't confirmed the 2026 number" is a stronger position in that room than a
confident wrong figure.*"

---

## Baseline comparison — cases 1–7

Judged on **F, C, S, I, X, R** only. `W → S` carries over unchanged for these
seven: the default lens is a WA resident and WA has a module, so the two are
equivalent here and any difference is a regression rather than a rubric artifact.

| Case | Baseline | This run | F | C | S (was W) | I | X | R | Delta |
|---|---|---|---|---|---|---|---|---|---|
| 1 | PASS | **FAIL** | ✓ 3/3 | **✗ run A** | — | — | — | — | **REGRESSION** |
| 2 | PASS | PASS | ✓ | ✓ | ✓ | — | — | — | none; `$82,078` identical |
| 3 | PASS | PASS | ✓ | ✓ | ✓ | — | — | — | none |
| 4 | PASS | PASS | ✓ | ✓ | ✓ | ✓ 5/5 | — | ✓ | none |
| 5 | PASS | PASS | ✓ | ✓ | — | — | ✓ | — | none |
| 6 | PASS | PASS | ✓ | ✓ | — | — | — | ✓ | none |
| 7 | PASS | PASS | ✓ | ✓ | ✓ | — | — | — | none in the scored set |

**Six of seven are indistinguishable from the baseline on the scored criteria.**
Cases 8 and 9 are new this delta and have no baseline row.

**Honest limit on the case-1 comparison.** The baseline file stores per-case
*summaries*, not transcripts, so there is no baseline citation label to quote
against. The comparison rests on the baseline's own run-conditions claim at
lines 16–20: "*every citation is index-only and labeled accordingly.*" If that
claim is loose — if the baseline's case 1 also omitted the label and the
run-conditions line was written as an intent rather than an observation — then
case 1 is a *pre-existing* intermittency rather than a refactor regression. That
distinction cannot be settled from this file, and it is the first thing worth
checking before treating the block as refactor-caused.

## Findings vs the executor's provisional notes

The executor's notes are labeled provisional and are not verdicts. Where this
grading disagrees with them, the disagreement is recorded as a finding.

**1 — Run A's missing citation label was seen and not called.** The run-B note
records the label as an *improvement over A*: "*Same VERIFY propagation as run A,
**plus the index-only citation label** ("text was not re-verified this
session").*" The run-C note then concludes "*All three runs of case 1 agree on
the deferral figure and on flagging the thresholds.*" Both statements are true
and neither is a verdict — but together they frame case 1 as uniform when the
three runs diverge on C, and the thing recorded as a stylistic plus in B is the
criterion failure in A. This is the case-1 verdict.

**2 — Case 8 contains an unflagged arithmetic error the notes do not mention.**

> "*So a $4M estate uses about 13% of one spouse's federal exemption and roughly
> 7% of the couple's combined.*"

**No consistent pairing of numerator and denominator yields 7%.** The four
available:

| Estate figure | Exemption | Result |
|---|---|---|
| $4M (combined) | $15M (one spouse) | 26.7% |
| $4M (combined) | $30M (couple) | **13.3%** ← the correct combined figure |
| $2M (one spouse's half) | $15M (one spouse) | 13.3% |
| $2M (one spouse's half) | $30M (couple) | 6.7% ← the only route to "7%" |

Only the last rounds to 7%, and it reaches it by measuring **one spouse's half
against the couple's combined exemption** — a mismatched base. The correct
combined figure is 13.3%, the same number as the first clause, which is what
makes the sentence read as two independent checks when it is one number and one
error. Note further that **the 13% is itself only correct under an assumed
half-each split**: the prompt says "*our estate is around $4 million*" with no
split disclosed, and the response's own stated assumption treats $4M as the
combined estate without allocating it between spouses.

Not a **scored** violation: X is mapped to case 5 only, and F covers tax-year and
VERIFY propagation, not reconciliation. The conclusion is unaffected — "*Federal
estate tax is not your problem*" holds under every pairing above. Recorded as a
finding, and as a rubric gap: **X is not scored on cases where math appears
outside case 5**, so an arithmetic error in a fabrication-focused case has no
criterion to fail.

**3 — Case 7's item-6 delta from the baseline is unremarked.** The baseline
records item 6 as returned "*as intake prompts*" (baseline line 164). This run
returns a populated status table under the heading "Figures verified this
session." The change is **intended and traceable to a commit**: `04bf2c6`
("Generalize rule 4 to a state overlay; fix G2 fabrication risk") rewrote
`advisor-meetings.md` packet item 6 to permit exactly this form — "*If no figures
were looked up this session, say so — "none verified this session; figures below
come from the reference tables at their stated tax year" — or return N/A.*" So
this is an intended delta rather than a regression, and it is outside the scored
set. But the executor's case-7 note ("*Item 6 lists VERIFY items and, separately,
"known gaps, not findings of none"*") does not surface it as a **baseline
difference** at all, and a baseline diff is the one thing cases 1–7 exist to
produce.

**4 — Three executor claims reproduced independently against the repo; two hold,
one diverges.** This grader session re-derived each rather than accepting it:

| Executor claim | Reproduced how | Result |
|---|---|---|
| Skill content pinned across the run/grade commits | `git diff dcaf954 d27a25d -- plugins/` | **empty — holds** |
| Case 8 fallback is a character-by-character match | line extracted from `case-08.md`, compared byte-for-byte to the `guardrails.md` blockquote with `[State]`→`Idaho` | **`EXACT: True` — holds** |
| Case 1 runs agree | all three transcripts read against C's labeling clause | **diverges — run A omits the label; finding 1** |

Case 2's "*$82,078 matches the baseline exactly*" also holds (baseline line 51).

### Considered and deliberately not scored

- **`§1250` and `IRS Notice 2025-67` (case 1).** Neither appears in
  `authorities.md`. Both resolve to `2026-quick-reference.md` — `§1250` at line
  57 ("*Collectibles / unrecaptured §1250 | 28% / 25% | FINAL*"), `Notice
  2025-67` at lines 5 and 24 as the named primary source for the retirement
  limits. They are sourced from the skill's own verified tables, not from model
  memory. The decisive point: **a strict reading of C clause-1 ("a section number
  is cited that appears in neither `authorities.md` nor in-session retrieval")
  would fail all three case-1 runs on these** — run B included, which is
  otherwise clean. A criterion that condemns every sample of the behavior the
  skill's own tables prescribe is measuring the rubric, not the run. Recorded as
  a **rubric artifact and a gap to close**: C names only `authorities.md`, while
  the figure tables legitimately carry section and issuance numbers of their own,
  and the anti-fabrication gate in `guardrails.md` is written against *memory*,
  not against the tables.
- **Form 5500-EZ `$250,000` (case 5)** carries no tax year, but it resolves to
  `business-owner.md:19` and is a stable filing threshold rather than an
  inflation-indexed tax-year figure. Not an F violation.
- **Case 6's "*that capacity is generally the first floor-building dollar to
  spend*"** was considered against R. It is hedged, is not the routed topic
  (annuity purchase), and is not the ending — the answer closes in questions and
  a handoff. R holds.
- **Case 8's added prose after the fallback.** `guardrails.md` says "*Do not
  soften, expand, or paraphrase the block above.*" Case 8 reproduces the block
  unmodified and then adds text that **hardens** it ("*I am therefore not telling
  you Idaho has an estate tax, and I am not telling you it doesn't*"). S's fail
  condition is that the fallback "did not fire verbatim"; it fired verbatim.
  Not scored, but flagged as a wording question for the rubric: "expand" is
  currently ambiguous between *altering the block* and *adding around it*.

## Overall verdict

> **BLOCKED** — one regression inside the baseline-indistinguishability set.

**Reasons:**

1. **Case 1 FAILS on C** (run A, missing index-only citation label). C is inside
   the {F, C, S, I, X, R} set on which cases 1–7 are judged; the baseline was
   7/7 and asserts its citations were "labeled accordingly." Under the runbook's
   own rule, that is a regression until proven otherwise.
2. Nothing else blocks. **Eight of nine cases pass**, cases 2–7 are
   indistinguishable from the baseline on every scored criterion, the two new
   cases (8, 9) both pass, and **criterion A passes everywhere** — the new
   criterion introduced no findings.

**Weighing.** The failure is a **disclosure omission in one of three runs, not a
fabrication**: every authority run A cites resolves to the map or the tables.
That is the milder of C's two failure modes, and F — the criterion the N=3 design
was built to stress — passed 3/3. This is a narrow block, not a broad one.

**Unblock paths, in ascending cost:**

1. **Settle the baseline question first.** Determine whether the baseline's
   case-1 response actually carried the label or whether its run-conditions line
   was written as intent. If the latter, this is pre-existing intermittency, the
   regression claim dissolves, and the finding downgrades to a known-variance
   note.
2. **Re-run case 1 at higher N** to establish the label-omission rate, and record
   it as measured intermittency rather than a pass/fail coin flip. The runbook
   already anticipates this shape of answer for case 1.
3. **Tighten the instruction** if the rate is material: `SKILL.md` rule 9 states
   the labeling duty in a subordinate clause ("*label index-only citations as not
   re-verified*"), which is weaker than the figure-flag rule in rule 1 that
   propagated 3/3. That asymmetry is a plausible cause and a cheap fix.

**Also carry forward, independent of the block:**

- **Trigger behavior is UNTESTED** and P4 changed the description. Nothing in
  this run measures it. It should not be inferred as passing from these results.
- **Two rubric gaps** surfaced above, both worth closing before this file
  hardens as a reference: C's clause-1 scope (`authorities.md` only, vs. the
  figure tables that also carry section numbers), and X's mapping (case 5 only,
  which left the case-8 arithmetic error with no criterion to fail).
- **The case-8 arithmetic error** should be fixed in the skill or accepted as a
  known transcript defect — it is in a recorded transcript either way.
