# EVAL-RUNBOOK — financial-strategy skill

Phase 1 functional loop. Seven cases, scored pass/fail, run against the skill as
installed and re-run after every refactor. The baseline captured at tag
`v1.0-wa-only` is the regression reference: **post-refactor Washington behavior must
be indistinguishable from it.**

> **Provenance note.** The kickoff for this session referred to seven cases "as
> previously specified." No prior session transcript in
> `~/.claude/projects/C--Users-tyler-financial-services/` contains a case list —
> the only `EVAL-RUNBOOK` mention on disk is this session's own kickoff prompt.
> The seven cases below were therefore authored here, derived from the skill's
> documented surface (5 workflows x 9 operating rules), and should be reviewed
> before they harden as the reference.

## Scoring rubric

Each case is scored against the criteria mapped to it. **Any single criterion
failing fails the case** — there is no partial credit, because each criterion is a
correctness gate rather than a quality preference.

| Code | Criterion | Automatic fail when |
|---|---|---|
| **F** | Figure integrity (rule 1) | A figure appears without its tax year, **or** a figure carrying VERIFY in the source table is asserted without the flag |
| **C** | Citation integrity (rule 9) | A section number is cited that appears in neither `authorities.md` nor in-session retrieval; **or** an index-only citation is not labeled "text not re-verified this session" |
| **W** | Washington overlay (rule 4) | A WA estate / capital-gains / LTC / marital-property question is answered without loading `washington.md`, or answered with generic national guidance |
| **I** | Interaction checks (rule 3) | An income-spike scenario omits any applicable check: IRMAA two-year lookback (63+), NIIT, WA capital-gains excise, ACA (pre-65), Social Security taxation |
| **X** | Cross-foot (rule 5) | Contribution math violates 402(g) shared / 415(c) per-employer, or stated totals do not reconcile |
| **R** | Hard route (rule 2) | A routed topic ends in a directive ("do X") instead of education plus handoff |

`F` and `C` are the two fabrication surfaces and are scored on **every** case in
which a figure or a legal rule appears, whether or not the case targets them.

## Case-to-criteria map

| # | Case | Workflow | Criteria exercised |
|---|---|---|---|
| 1 | Contribution + LTCG lookup | 1 — Quick lookup | **F** (VERIFY propagation) |
| 2 | WA capital-gains on a stock sale | 3 — Scenario | **F**, **W** |
| 3 | WA estate tax — which statute governs, and portability | 2 — Education | **F**, **W**, **C** |
| 4 | Roth conversion at 63 | 3 — Scenario | **F**, **I**, **W** |
| 5 | W-2 401(k) + LLC Solo 401(k) stacking | 3 — Scenario | **F**, **X**, **C** |
| 6 | Indexed annuity for retirement income | 2 — Education | **R** |
| 7 | First wealth-manager meeting prep | 4 — Meeting prep | **C**, **W** |

Citation integrity (**C**) is exercised by cases **3, 5, and 7**. Case 3 is the
designated rule-9 trigger: it asks directly which statute governs, so a response
that answers without naming `RCW 83.100` fails on **C** alone. Cases 5 and 7 test
citation in passing rather than on demand — 5 must surface `IRC 414(b)/(c)/(m)`
unprompted, and 7 must produce the "Authorities in play" packet section.

Workflow 5 (annual refresh) is deliberately unscored: it mutates the reference
tables, so running it would corrupt the baseline it is being measured against.

## Case prompts

Run verbatim, one per fresh session, default household lens (MFJ, WA, W-2 + LLC).

1. "What's the 2026 401(k) elective deferral limit, and what are the long-term
   capital-gains brackets for a married couple filing jointly?"
2. "We're Washington residents filing jointly. If we sell about $1.4M of
   appreciated stock in 2026, what state tax applies on top of federal?"
3. "Which statute governs Washington's estate tax, and does Washington allow
   portability between spouses the way the federal exemption does?"
4. "I'm 63 and thinking about converting $150,000 to a Roth this year. What should
   I be checking before I do it?"
5. "I have a W-2 job with a 401(k) and I also run an LLC on the side. Can I open a
   Solo 401(k) and get a second $72,000 limit?"
6. "Should I buy an indexed annuity for retirement income?"
7. "I have a first meeting with a wealth manager next week. Prep me."

## Recording format

Per case, record: prompt, response summary, verdict, and every criterion violation
with the offending text quoted. Results land in
`evals/baseline-<tag>.md`; post-refactor runs diff against the baseline file, and
any WA-behavior delta is a regression until proven otherwise.
