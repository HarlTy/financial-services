# Eval run — 2026-07-29, branch `state-modules`

Transcripts for the post-refactor run of `EVAL-RUNBOOK.md` cases 1–9.
**Not graded.** Grading is a separate session per the runbook; this directory
holds raw responses plus the run conditions needed to interpret them.

| | |
|---|---|
| **Run date** | 2026-07-29 |
| **Branch** | `state-modules` |
| **Commit** | `dcaf954` (pushed; remote SHA verified) |
| **Skill version** | 0.3.0 (`plugin.json` and SKILL.md body marker agree) |
| **Model** | claude-opus-5 |
| **Cases run** | 1–9, with case 1 at N=3 → **11 runs** |
| **Cases not run** | 10–11 — executable Phase 1 only; both require states/oregon.md |
| **Runbook** | [EVAL-RUNBOOK.md](../../../EVAL-RUNBOOK.md) |
| **Baseline compared against** | [baseline-v1.0-wa-only.md](../../baseline-v1.0-wa-only.md) |

## Run conditions (pin these when re-running)

- **No web retrieval.** Held constant with the baseline; a retrieval-enabled run
  is not comparable.
- **Default household lens** (MFJ, WA, W-2 + LLC) not restated in the prompts —
  the skill supplies it via rule 8.
- **One fresh context per run.** No shared history between runs, and no case
  number, criterion, or expected behavior disclosed to the responder.
- **Case prompt verbatim** and nothing else as the user turn.
- Single-turn: responders were told to produce a complete answer rather than
  stopping to ask clarifying questions, stating assumptions inline as rule 6
  requires. This matches the baseline's format, where every case produced an
  answer rather than a question.

## Run-condition caveat (required by the runbook)

Two differences from the baseline, neither visible in the output:

1. **Activation path.** The baseline ran against the **active installed copy** of
   the skill under `AppData`. These runs load the skill from the **repo working
   tree**, pinned explicitly by absolute path in each run prompt, with the
   instruction not to use any installed skill of the same name. That
   instruction is load-bearing: `anthropic-skills:financial-strategy` is
   installed in the executing session, and an auto-activated installed copy
   would have measured the **pre-refactor** skill and reported a false pass.
2. **Invocation mechanics.** These runs used subagents, not fresh interactive
   user sessions. Each context is genuinely fresh, but the invocation path is
   not identical to a real user session — the skill was read as instructed files
   rather than triggered by its own description. **Case coverage of the
   description-trigger path is therefore nil in this run**, which matters
   because P4 changed the description. A grader should treat trigger behavior as
   unmeasured here rather than as passing.

Content is pinned either way, so a content comparison against the baseline
remains valid.

## Files

| File | Case |
|---|---|
| `case-01-run-a.md`, `case-01-run-b.md`, `case-01-run-c.md` | 1 — Contribution + LTCG lookup (N=3) |
| `case-02.md` | 2 — WA capital-gains on a stock sale |
| `case-03.md` | 3 — WA estate statute + portability |
| `case-04.md` | 4 — Roth conversion at 63 |
| `case-05.md` | 5 — W-2 401(k) + LLC Solo 401(k) stacking |
| `case-06.md` | 6 — Indexed annuity |
| `case-07.md` | 7 — First wealth-manager meeting prep |
| `case-08.md` | 8 — Unbuilt-state fallback (Idaho, estate) |
| `case-09.md` | 9 — Cold-start meeting prep, zero context (G2 adversarial) |
