# Eval run — 2026-07-30, branch `state-modules` — case 1 rule-9 recheck

Transcripts for a **case-1-only re-run at N=5**, executed against the skill as of
commit `8cd5f93`. **Not graded.** Grading is a separate session per the runbook;
this directory holds raw responses plus the run conditions needed to interpret
them.

| | |
|---|---|
| **Run date** | 2026-07-30 |
| **Branch** | `state-modules` |
| **Commit** | `8cd5f93` (pushed; `HEAD` and `origin/state-modules` verified equal, tree clean) |
| **Skill version** | 0.3.0 (`plugin.json` and SKILL.md body marker agree) |
| **Model** | claude-opus-5 |
| **Subagent type** | `general-purpose` |
| **Cases run** | 1 only, at N=5 → **5 runs** |
| **Cases not run** | 2–9 (not in scope for this recheck); 10–11 executable Phase 1 only |
| **Runbook** | [EVAL-RUNBOOK.md](../../../EVAL-RUNBOOK.md) |
| **Prior run** | [run-2026-07-29/](../run-2026-07-29/) — case 1 at N=3 |
| **Prior grading** | [run-2026-07-29-state-modules.md](../../run-2026-07-29-state-modules.md) |

## Why this run exists

The 2026-07-29 grading returned **8/9 pass, case 1 FAIL on C**: run A cited
`IRC §402(g)`, `§415(c)`, and `RCW 82.87.040` with no index-only citation label
anywhere in the response, while runs B and C both carried one. The grader
recorded the failure as a **disclosure omission rather than fabrication** — every
authority resolved to the skill's own map or tables — and blocked on the rate
being unmeasured and the protocol unhardened.

That grading prescribed a two-step unblock path, in order:

1. **Harden the disclosure protocol.** Done at `8cd5f93`: rule 9's subordinate
   clause became an imperative, and the label text moved into
   `references/authorities.md` as a stored verbatim block — the same mechanism
   that made case 8's fallback reliable.
2. **Then re-run case 1 at N≥5 and gate C at 5/5.** N=3 was sized for F and
   caught the C defect incidentally; it cannot measure a rate.

This directory is step 2. **It does not decide whether the gate is met** — that
is the grader's call.

## Run conditions (pin these when re-running)

- **No web retrieval.** Held constant with the baseline and the 2026-07-29 run.
  Responders were told to treat the session as having no web access. This is
  load-bearing: rule 9 branches on whether the session has web access, so
  leaving it ambiguous would change behavior. It names neither the label, rule
  9, nor citations.
- **Skill loaded from the repo working tree**, pinned by absolute path in the
  run prompt, with an explicit instruction not to use any installed skill of the
  same name and not to use the Skill tool at all.
- **Default household lens** (MFJ, WA, W-2 + LLC) not restated in the prompt —
  the skill supplies it via rule 8.
- **One fresh context per run.** No shared history between runs, and no case
  number, criterion, rule number, or expected behavior disclosed to the
  responder.
- **Case prompt verbatim** and nothing else as the user turn.
- **Single-turn:** responders were told to produce a complete answer rather than
  stopping to ask clarifying questions, stating assumptions inline as rule 6
  requires.
- **Identical prompt across all five runs.** Temperature supplies the variation;
  varying the prompt would contaminate the sample.

## Run prompt (verbatim)

The exact text sent to all five subagents, byte-for-byte as issued. Recorded so
the next re-run reproduces mechanics from this text rather than reconstructing
them from the prose above — see [Prompt provenance](#prompt-provenance).

```
You are answering a single user question. Follow these instructions exactly.

**Source of instructions.** Read the skill at this absolute path and follow it:

C:\Users\tyler\financial-services\plugins\vertical-plugins\personal-financial-strategy\skills\financial-strategy\SKILL.md

Read that file first, then load whichever files under `references/` its own reference map directs you to load for this question. Treat the contents of that directory as your operating instructions for this response.

**Do not use any installed skill of the same name.** A skill named `financial-strategy` is installed in this environment. Do not invoke it, and do not use the Skill tool at all. The only version that counts is the one at the absolute path above, read with the Read tool.

**No web retrieval.** Do not use WebSearch, WebFetch, or any other network tool, and do not load them. Treat this session as having no web access.

**Single turn.** Produce one complete answer. Do not stop to ask clarifying questions — where something is unspecified, proceed and state your assumption inline.

**Your output.** Return the text of your answer to the user and nothing else — no preamble, no notes about which files you read, no meta-commentary about the task.

The user's message is, verbatim:

What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?
```

## Prompt provenance

**The 2026-07-29 run prompt was never recorded** — only its run-conditions
bullets. "Same mechanics as run-2026-07-29" was therefore **reconstructed** from
that prose rather than reproduced from the prompt text. Two consequences a
grader should weigh:

1. **The comparison against 2026-07-29 is prompt-reconstructed, not
   prompt-identical.** Every documented condition is carried over, but
   reconstruction is strictly weaker than reproduction: a condition that shaped
   the prior responses without being written down cannot be recovered, and
   nothing in the output reveals its absence. Anyone reading this run's label
   rate against the prior run's should know that one dimension of "held
   constant" rests on the prior README's completeness.
2. **Two conditions are newly fixed here** because the prior conditions block
   did not state them, and they are recorded so the next run inherits them
   rather than re-deriving them:
   - **Subagent type** is `general-purpose`. The prior run did not record its
     own, so this dimension is not provably identical across the two runs.
   - **"Treat this session as having no web access"** is phrased as an
     environment fact in the prompt. The prior run held "no web retrieval"
     constant but did not record how it was worded to the responder.

## Run-condition caveats (required by the runbook)

Two differences from the baseline, neither visible in the output:

1. **Activation path.** The baseline ran against the **active installed copy**
   of the skill under `AppData`. These runs load the skill from the **repo
   working tree**. That instruction is load-bearing:
   `anthropic-skills:financial-strategy` is installed in the executing session,
   and an auto-activated installed copy would have measured a different content
   state and reported a false result.
2. **Invocation mechanics.** These runs used subagents, not fresh interactive
   user sessions. Each context is genuinely fresh, but the invocation path is
   not identical to a real user session — the skill was read as instructed files
   rather than triggered by its own description. **Trigger behavior is therefore
   unmeasured in this run**, exactly as in the 2026-07-29 run, and should be
   treated as unmeasured rather than as passing.

Content is pinned either way, so a content comparison remains valid.

## On the provisional notes

Each transcript carries a `## Provisional executor note (NOT a verdict)`.
Per the runbook, the executor may record provisional observations but a
provisional note is not a verdict.

**These notes are per-run and carry no cross-run aggregation** — no tally, no
"all five agree," no pass/fail language. That constraint is deliberate: the
2026-07-29 grading faulted that run's executor note for concluding "all three
runs of case 1 agree" when the label was in fact present in B and C and absent
in A, which framed the case as uniform when it was not. Any statement about the
five runs as a set belongs to the grader.

## Files

| File | Run |
|---|---|
| `case-01-run-a.md` | Case 1, run A |
| `case-01-run-b.md` | Case 1, run B |
| `case-01-run-c.md` | Case 1, run C |
| `case-01-run-d.md` | Case 1, run D |
| `case-01-run-e.md` | Case 1, run E |
