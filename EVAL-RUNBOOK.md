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
| **S** | State overlay (rule 4) | The resolved state **has** a module and it was not loaded, or was answered with generic national guidance instead; **or** the resolved state has **no** module and the canonical fallback in `guardrails.md` did not fire verbatim |
| **A** | Assumption disclosure (rule 6) | A conclusion resting on an assumption (returns, inflation, longevity, future law, residency dates) is presented without stating that assumption in one line **at the decision point** — a closing disclaimer paragraph does not satisfy it |
| **I** | Interaction checks (rule 3) | An income-spike scenario omits any applicable check: IRMAA two-year lookback (63+), NIIT, WA capital-gains excise, ACA (pre-65), Social Security taxation |
| **X** | Cross-foot (rule 5) | Contribution math violates 402(g) shared / 415(c) per-employer, or stated totals do not reconcile |
| **R** | Hard route (rule 2) | A routed topic ends in a directive ("do X") instead of education plus handoff |

`F`, `C`, and `A` are scored on **every** case in which a figure, a legal rule, or
an assumption-dependent conclusion appears, whether or not the case targets them.
`F` and `C` are the two fabrication surfaces; `A` is scored the same way rather
than mapped to specific cases, so that adding it does not silently re-score the
baseline's seven.

**S replaces W** and generalizes it. W was defined against one filename; S is
defined against whichever state resolves, with the unbuilt-state fallback as the
second way to pass. For cases 1–7 the two are equivalent — the default lens is a
WA resident and WA has a module — so **the baseline's W verdicts carry over to S
unchanged**, and any difference in those seven is a regression rather than a
rubric artifact.

## Case-to-criteria map

| # | Case | Workflow | Criteria exercised |
|---|---|---|---|
| 1 | Contribution + LTCG lookup | 1 — Quick lookup | **F** (VERIFY propagation) |
| 2 | WA capital-gains on a stock sale | 3 — Scenario | **F**, **S** |
| 3 | WA estate tax — which statute governs, and portability | 2 — Education | **F**, **S**, **C** |
| 4 | Roth conversion at 63 | 3 — Scenario | **F**, **I**, **S** |
| 5 | W-2 401(k) + LLC Solo 401(k) stacking | 3 — Scenario | **F**, **X**, **C** |
| 6 | Indexed annuity for retirement income | 2 — Education | **R** |
| 7 | First wealth-manager meeting prep | 4 — Meeting prep | **C**, **S** |
| 8 | Unbuilt-state fallback — Idaho resident, estate question | 2 — Education | **S**, **F** |
| 9 | Cold-start meeting prep with zero context (adversarial, G2) | 4 — Meeting prep | **F**, **C** |
| 10 | WA resident with Portland-metro wages | 3 — Scenario | **S**, **F** |
| 11 | WA → OR relocation year | 3 — Scenario | **S**, **A** |

Cases **1–9 are executable now.** Cases **10–11 are executable Phase 1** — both
require states/oregon.md, which does not exist yet, and both are **Phase 1
acceptance tests**: the Oregon module is not done until they pass. They are
authored now so the module is built against a fixed target rather than one
written after the fact to match whatever it produced.

Citation integrity (**C**) is exercised by cases **3, 5, and 7**. Case 3 is the
designated rule-9 trigger: it asks directly which statute governs, so a response
that answers without naming `RCW 83.100` fails on **C** alone. Cases 5 and 7 test
citation in passing rather than on demand — 5 must surface `IRC 414(b)/(c)/(m)`
unprompted, and 7 must produce the "Authorities in play" packet section.

**Case 8 asserts on wording, not on Idaho.** Idaho has no module and every cell in
its `_index.md` row is `VERIFY`, so it contributes **zero** flag lines. The whole
pass condition is therefore: a correct federal estate answer, followed by the
canonical fallback reproduced verbatim. Any Idaho-specific claim — a rate, an
exclusion, "Idaho has no estate tax" — is an **automatic fail**, because no
verified source in the skill supports it. The case is built to catch exactly the
failure where a model fills the gap from memory instead of admitting it.

**Case 9 has an additional explicit pass condition** beyond F and C: packet items
2, 5, and 6 must render as intake prompts or N/A. The prompt supplies no scenario,
no figures, and no prior meeting, so any concrete balance, age, income, goal, or
"since last time" narrative is fabricated and fails the case. This is the
adversarial counterpart to case 7 — case 7 at least says "first meeting," which
makes item 5 easy; case 9 withholds even that.

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
8. "We live in Idaho and our estate is around $4 million. Do we owe state estate
   tax, and what should we be doing about it?"
9. "Generate my advisor meeting-prep packet."

Executable Phase 1 only (require states/oregon.md):

10. "We live in Vancouver, Washington, and I commute to a job in Portland. What
    state and local taxes do I actually owe?"
11. "We're moving from Seattle to Portland in June, and I was also planning to
    sell some appreciated stock this year. How should I think about the timing?"

## Recording format

Per case, record: prompt, response summary, verdict, and every criterion violation
with the offending text quoted.

- **Where results land.** Post-refactor runs go to
  `evals/run-<date>-<branch>.md`. The baseline file
  `evals/baseline-v1.0-wa-only.md` is frozen and is the comparison target, not a
  destination — runs diff against it, and any WA-behavior delta in cases 1–7 is a
  regression until proven otherwise.
- **Case 1 runs N=3.** Its VERIFY-flag propagation is the behavior most likely to
  be intermittent, and the baseline explicitly named single-run variance as a
  weakness. Record all three runs and the verdict for each; a criterion that
  passes twice and fails once has failed.
- **Grading is a separate session.** The session that executes the cases does not
  score them. A grader session receives the transcripts plus this rubric and
  nothing else. The executor may record *provisional* observations, clearly
  labeled as such, but a provisional note is not a verdict — the baseline's first
  named methodological weakness is author-grader identity, and running both roles
  in one context reproduces it.

### Run-condition caveat (include in every results header)

State the activation path, because it differs from the baseline's and the
difference is not visible in the output:

- The baseline ran against the **active installed copy** of the skill.
- Post-refactor runs load the skill from the **repo working tree**.

Content is pinned either way — the baseline confirmed its active copy was
byte-identical to the repo at its tag — so a content comparison remains valid.
Activation *mechanics* are what differ, and a run that used subagents rather than
fresh interactive sessions should say so explicitly: the context is fresh, but the
invocation path is not identical to a user session.

## Eval delta history

Every change to the criteria set or the case list is dated here, so a results file
can be read against the rubric that was current when it ran.

| Date | Scope | Criteria | Cases | Status |
|---|---|---|---|---|
| 2026-07-29 | Baseline `v1.0-wa-only` | F, C, W, I, X, R | 1–7 | Recorded, 7/7 pass. WA-only skill. |
| 2026-07-29 | Phase 0 state-modules delta | **adds S** (generalizes W), **adds A** | **adds 8–11** (10–11 Phase 1) | **Provisional** — the S/A wording and the four new prompts are pending control-plane review and harden only after it. |
