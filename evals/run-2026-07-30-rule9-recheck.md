# Eval results — case-1 rule-9 recheck, run 2026-07-30, branch `state-modules`

| | |
|---|---|
| **Grader session** | independent grader; did not execute the runs and did not write the rule-9 hardening |
| **Grading date** | 2026-07-31 |
| **Model (grader)** | claude-opus-5 |
| **Skill under test** | `financial-strategy` @ `8cd5f93`, version 0.3.0 |
| **Runbook** | [EVAL-RUNBOOK.md](../EVAL-RUNBOOK.md) (criteria F, C, S, I, X, R, A) |
| **Transcripts graded** | [`transcripts/run-2026-07-30-rule9-recheck/`](transcripts/run-2026-07-30-rule9-recheck/) — case 1 × 5 (runs A–E) |
| **Scope** | Case 1 only. Cases 2–9 are not re-run and their 2026-07-29 verdicts stand. |
| **Gate under test** | criterion **C** at **5/5**, per the unblock path in [run-2026-07-29-state-modules.md](run-2026-07-29-state-modules.md#overall-verdict) |
| **Result** | **C passes 5 / 5. F passes 5 / 5. A passes 5 / 5. Case 1 = PASS.** |
| **Gate outcome** | **MET** — see [Gate outcome](#gate-outcome) |

## Skill-drift check (performed, not assumed)

The transcript README records the run at `8cd5f93`; this grading runs at `6d4648d`.
Different commits, so the skill content was verified rather than assumed identical:

```
git diff --stat 8cd5f93 6d4648d -- plugins/vertical-plugins/personal-financial-strategy plugins/agent-plugins
→ (empty)

git diff --name-only 8cd5f93 6d4648d
→ evals/transcripts/run-2026-07-30-rule9-recheck/README.md
  evals/transcripts/run-2026-07-30-rule9-recheck/case-01-run-{a,b,c,d,e}.md
```

`6d4648d` touches only `evals/`. The skill graded here is byte-identical to the
skill the runs measured. Working tree clean at grading time.

## Run-condition caveat (required by the runbook)

Carried from the transcript README and unchanged from the 2026-07-29 run:

1. **Activation path.** The baseline ran against the **active installed copy** of
   the skill under `AppData`. These runs load the skill from the **repo working
   tree**, pinned by absolute path, with an explicit instruction not to use any
   installed skill of the same name and not to use the Skill tool at all.
2. **Invocation mechanics.** These runs used subagents, not fresh interactive user
   sessions. Each context is genuinely fresh, but the invocation path is not
   identical to a user session — the skill was read as instructed files rather
   than triggered by its own description. **Trigger behavior remains UNMEASURED**,
   exactly as in the prior run, and is not counted for or against this gate.

**No web retrieval**, held constant. This is load-bearing: rule 9 branches on
whether the session has web access, and the run prompt phrases it as an
environment fact ("*Treat this session as having no web access*"). Content is
pinned either way, so the content comparison remains valid.

### Prompt provenance — weighed, per the README

The README's [Prompt provenance](transcripts/run-2026-07-30-rule9-recheck/README.md)
section opens "*Two consequences a grader should weigh*". Both are weighed here
and both constrain what this result may be read to say:

1. **The comparison against 2026-07-29 is prompt-reconstructed, not
   prompt-identical.** The prior run's prompt text was never recorded, only its
   conditions prose. A condition that shaped the prior responses without being
   written down cannot be recovered.
2. **Two conditions are newly fixed** (subagent type `general-purpose`; the
   no-web-access wording), because the prior run did not record its own. Neither
   dimension is provably identical across the two runs.

**Consequence for this verdict.** The gate condition is a property of *this* run
measured against the rubric — "C at 5/5 at `8cd5f93`" — and that is established
below. What is **not** established is **causal attribution**: no control arm was
re-run at the pre-hardening commit at N=5, and the cross-run comparison is
prompt-reconstructed. So this file records that **C passes uniformly at N=5 after
the hardening**; it does not assert that the hardening is what produced the
change. The unblock path as written does not require that attribution — it
requires uniform passing at N≥5 — so the gate is met on its own terms.

> **Note on the request.** This grading was asked to read the README's "What the
> grader should weigh" section. **No section carries that title.** The nearest is
> **Prompt provenance**, whose lead sentence is "*Two consequences a grader should
> weigh*"; that section is treated as the intended referent and is weighed above,
> together with **Run-condition caveats** and **On the provisional notes**.

## Scoring notes

- **N=5, not the runbook's N=3.** The runbook sizes case 1 at N=3; the 2026-07-29
  unblock path supersedes it for this recheck ("*re-run case 1 at N≥5 and gate C
  at 5/5*"). The runbook's rule that a criterion passing some runs and failing
  others has failed is applied unchanged — here it is not reached, because no run
  fails.
- **F and A scored as always-on**, per the runbook, on every run in which a figure
  or an assumption-dependent conclusion appears. Both appear in all five.
- **The §1250 / Notice 2025-67 rubric-artifact ruling is applied, not
  re-litigated**, per the 2026-07-29 results file
  ([Considered and deliberately not scored](run-2026-07-29-state-modules.md#considered-and-deliberately-not-scored)):
  issuances and section numbers that resolve to the skill's own **figure tables**
  rather than to `authorities.md` are not C clause-1 violations, because C names
  only `authorities.md` while the figure tables legitimately carry issuance
  numbers of their own. See [The ruling is load-bearing for this gate](#the-1250--notice-2025-67-ruling-is-load-bearing-for-this-gate)
  — it is not a side note here.
- **Criteria not scored:** S, I, X, R are not mapped to case 1 and are not
  always-on. Run E volunteers the rule-3 interaction-check list unprompted; that
  is recorded as an observation, not scored. See
  [Considered and not scored](#considered-and-deliberately-not-scored).
- **No violation is asserted without the offending text quoted**, and the label
  text is quoted for every run in which it appears, as requested.
- **Verification was mechanical where it could be.** The label was compared
  byte-for-byte against the canonical block, and every citation token in every
  response was extracted by pattern and resolved against the reference set, rather
  than being read for.

## The gate — criterion C at 5/5

### The duty, as it now reads at `8cd5f93`

Rule 9 was rewritten by `8cd5f93` from a subordinate clause into an imperative
**and** given a stored template. `SKILL.md:22`:

> 9. **Cite the controlling authority — and the label travels with the
> citations.** … **If any citation was not re-verified this session, the response
> ends with the canonical index-only label from `references/authorities.md`,
> verbatim — a single unlabeled index-only citation is a defect, regardless of
> answer length.**

`references/authorities.md:9–13` now stores the label as the single source of
truth:

> - **Canonical index-only label (single source of truth).** When any cited
>   authority was not re-verified against current text this session, end the
>   citation block — or the response, if citations are inline — with this text
>   **verbatim**:
>
>   > Citations from this skill's index — text not re-verified this session.
>
>   Do not paraphrase or shorten it. It is stored here and nowhere else so the
>   wording cannot drift between the skill, the rubric, and the answers.

### Label presence and fidelity — 5/5, byte-exact

The canonical string was extracted from `authorities.md:11` and compared
character-for-character against the label line in each response body (executor
notes excluded from the comparison):

| Run | Label text as it appears in the response | Byte-exact vs canonical | Rendering | Ends the response? |
|---|---|---|---|---|
| **A** | "Citations from this skill's index — text not re-verified this session." | **True** | plain line | No — closing disclaimer follows |
| **B** | "> Citations from this skill's index — text not re-verified this session." | **True** | blockquote | **Yes** |
| **C** | "> Citations from this skill's index — text not re-verified this session." | **True** | blockquote | **Yes** |
| **D** | "Citations from this skill's index — text not re-verified this session." | **True** | plain line | **Yes** |
| **E** | "> Citations from this skill's index — text not re-verified this session." | **True** | blockquote | No — closing disclaimer follows |

Exactly one label-bearing line per response; no run carries a paraphrase, a
duplicate, or a shortened variant. The em dash, the apostrophe, and the terminal
period match in all five. **This is the behavior the 2026-07-29 grading did not
get: run A of that run carried no label anywhere, and the two that did carry one
carried two different wordings** ("*Authority citations above are from this
skill's index — statutory text was not re-verified this session*" in B;
"***Authorities** (citations from index — text not re-verified this session)*" in
C). Both would pass C, which tests presence; neither is the canonical string.
Storing the block collapsed that variance to zero.

### Clause 1 — no unresolved section number in any run

Every citation token in all five responses was extracted by pattern and resolved
against the reference set. **Zero unresolved.** Distinct tokens across the run set:

| Token | Resolves to |
|---|---|
| `IRC §402(g)`, `§415(c)` | `authorities.md` (+ `2026-quick-reference.md`, `business-owner.md`) |
| `IRC §414(v)`, `§402A`, `§1(h)`, `§1411`, `SECURE 2.0 §603` | `authorities.md` |
| `IRC §414(b)/(c)/(m)` (run A) | `authorities.md`, `business-owner.md` |
| `RCW 82.87`, `82.87.040`, `82.87.020`, `ESSB 5813` | `states/washington.md` (module authority table, line 177) |
| `IRS Notice 2025-67`, `Rev. Proc. 2025-32`, `§1250` | `2026-quick-reference.md` — **rubric artifact, not scored** |

Run C additionally states "*(Verification pass date: 2026-07-28…)*". That
resolves: `authorities.md:3` and `states/washington.md:3` both read "Last
verified: 2026-07-28". Accurate, not invented.

**C = PASS on all five runs. The gate condition is met.**

### The §1250 / Notice 2025-67 ruling is load-bearing for this gate

This is not a footnote and should not be read as one. **All five runs cite
`IRS Notice 2025-67` and `Rev. Proc. 2025-32`**, neither of which appears in
`authorities.md`. Under a strict reading of C clause 1 — "*a section number is
cited that appears in neither `authorities.md` nor in-session retrieval*" — the
gate would return **0/5**, not 5/5. The entire outcome turns on the prior
grading's ruling that figure-table issuances are outside clause 1's target.

Two things follow:

1. **`Rev. Proc. 2025-32` is inside the ruling's scope, and treating it so is
   application rather than extension.** The 07-29 ruling named `§1250` and
   `Notice 2025-67` as its examples, but stated its reasoning by class: "*C names
   only `authorities.md`, while the figure tables legitimately carry section and
   issuance numbers of their own.*" `Rev. Proc. 2025-32` is an IRS issuance named
   by `2026-quick-reference.md:5` as a primary source and by line 55 as the
   confirmation target for the flagged thresholds — squarely that class. It also
   appeared in the 07-29 transcripts (run A, case 4) and no run was failed on it,
   so the ruling was already being applied to it implicitly.
2. **The rubric gap is now gating a release decision, and its priority should
   rise accordingly.** The 07-29 file recorded C's clause-1 scope as "*a gap to
   close*" before that file hardened as a reference. It is no longer merely
   untidy: an unblock gate now returns PASS or FAIL depending on an
   interpretation that the runbook's criterion text does not contain. **C clause 1
   should be amended to name the skill's verified figure tables alongside
   `authorities.md`** before this file is cited as precedent.

## Per-run verdicts

### Run A — **PASS** (F ✓, C ✓, A ✓)

**C — pass.** Citations consolidated into an "Authorities in play" line, followed
by the canonical label:

> Authorities in play: elective deferral limit — **IRC §402(g)**; catch-ups — **IRC §414(v)**; mandatory Roth catch-up — **IRC §402A** and **SECURE 2.0 §603**; annual additions — **IRC §415(c)**; LTCG rates — **IRC §1(h)**; NIIT — **IRC §1411**; WA excise — **RCW 82.87**, rate mechanics at **RCW 82.87.040** as amended by ESSB 5813 (2025) sec. 101, defined terms at **RCW 82.87.020**.
>
> Citations from this skill's index — text not re-verified this session.

All resolve. **This is the run to compare against 07-29 run A**, which carried the
same citation set and no label at all. The label is present, byte-exact, and
placed immediately after the citation block it governs. Placement relative to the
closing disclaimer is treated under [finding 2](#2--rule-9-and-authoritiesmd-disagree-on-placement-and-c-cannot-see-it), not as a C failure.

**F — pass.** VERIFY propagated with the source's own reason:

> The dollar thresholds carry a **VERIFY flag with a known conflict**, and I have to hand that flag to you rather than a clean number

> those figures match the TY2025 values exactly and are almost certainly stale in the secondary sources they came from — a genuinely inflation-adjusted TY2026 table should sit roughly 2–3% higher. This session has no web access, so I could not confirm them against **Rev. Proc. 2025-32**

Matches `2026-quick-reference.md:55` ("*VERIFY — known conflict*") one for one.
$24,500 / $8,000 / $11,250 carry TY2026 + FINAL; the WA standard deduction carries
"*$278,000 for TY2025 … **VERIFY the TY2026 amount at WA DOR***", matching
`washington.md:46`. Also the only run to state the MFJ standard deduction
("*$32,200 MFJ standard deduction, TY2026, FINAL*" — `2026-quick-reference.md:13`).

**A — pass.** At the decision point, not in a closing block:

> I'm assuming the default lens here: married filing jointly, Washington resident. If you're in another state, say so, because the state answer changes materially.

### Run B — **PASS** (F ✓, C ✓, A ✓)

**C — pass.** Consolidated authorities line, then the canonical label as the final
line of the response:

> Authorities: elective deferral limit, IRC §402(g); catch-ups, IRC §414(v); mandatory Roth catch-up, IRC §402A and SECURE 2.0 §603; LTCG rates, IRC §1(h); NIIT, IRC §1411; WA excise, RCW 82.87 (rate mechanics at RCW 82.87.040 as amended by ESSB 5813 (2025) sec. 101).
>
> > Citations from this skill's index — text not re-verified this session.

**F — pass.** The strongest rendering of the flag in the set — a per-row `Status`
column reading `VERIFY` on all three threshold rows, plus the prose statement:

> The **threshold dollars are flagged VERIFY — known conflict**, and I have to pass that flag through rather than hand you clean numbers

NIIT carries its tax year explicitly here ("*$250,000 MFJ (TY2026, FINAL)*"),
which the other runs leave to section scope.

**A — pass.**

> I'm assuming WA residence per the default household lens; say so if that's wrong, because it changes this line entirely.

### Run C — **PASS** (F ✓, C ✓, A ✓)

**C — pass.** Citations inline throughout rather than consolidated; the canonical
label closes the response, which is the branch `authorities.md:9` prescribes for
inline citations ("*or the response, if citations are inline*"):

> > Citations from this skill's index — text not re-verified this session.

**F — pass.** Flag carried in the rule's own words, and the figures hedged with
`~`:

> The **thresholds carry a VERIFY flag — known conflict**, and the flag travels with the numbers

The `~` hedging is additional to the flag, not a substitute for it. The only run
to state the skill's verification-pass date; verified accurate above.

**A — pass.**

> (assuming the default lens — MFJ, WA residents; say so if that's wrong, because this piece changes entirely by state)

### Run D — **PASS** (F ✓, C ✓, A ✓)

**C — pass.** Inline citations; canonical label as the final line, plain-rendered:

> Citations from this skill's index — text not re-verified this session.

**F — pass.** Flag carried plus an explicit do-not-rely instruction:

> Those figures are identical to the TY2025 values, which is the tell … **Do not use them to size a gain-realization decision without confirming against IRS Rev. Proc. 2025-32.** I have no web access this session, so I could not re-check them for you.

**A — pass.**

> I'm assuming the default household lens here (married filing jointly, Washington resident); say the word if that's wrong, because the state answer changes completely.

### Run E — **PASS** (F ✓, C ✓, A ✓)

**C — pass.** Consolidated "Authorities in play" line followed by the canonical
label:

> **Authorities in play:** elective deferral limit — IRC §402(g); catch-ups — IRC §414(v); mandatory Roth catch-up — IRC §402A and SECURE 2.0 §603; annual additions — IRC §415(c); LTCG rates — IRC §1(h); NIIT — IRC §1411; WA excise — RCW 82.87, rate mechanics at RCW 82.87.040.
>
> > Citations from this skill's index — text not re-verified this session.

**F — pass**, and this run carries the flag furthest — into the section heading
itself:

> **Long-term capital-gains brackets, MFJ — TY2026, VERIFY (known conflict)**

> The **thresholds carry an unresolved verification flag**, and it travels with the figures

Its expanded WA exemption list — "*real estate, assets inside retirement accounts,
timber, livestock/agricultural assets, commercial fishing privileges*" — matches
`washington.md:48–49` exactly, including the three items the other four runs omit.
"*The $1M threshold is not indexed*" matches `washington.md:45`. Nothing added
from memory.

**A — pass.**

> **Washington overlay** (assuming the default lens — married filing jointly, Washington resident; tell me if that's wrong)

## Gate outcome

| Criterion | Runs passing | Gate |
|---|---|---|
| **C** — citation integrity (rule 9) | **5 / 5** (A, B, C, D, E) | **gated at 5/5 → MET** |
| F — figure integrity (rule 1) | 5 / 5 | not gated; scored always-on |
| A — assumption disclosure (rule 6) | 5 / 5 | not gated; scored always-on |

**Case 1 = PASS.** No criterion failed on any run, so the runbook's
"passes-twice-fails-once" rule is not reached, and "any single criterion failing
fails the case" is not triggered.

Combined with the 2026-07-29 verdicts for cases 2–9, which stand unchanged and
were not re-run: **9 / 9 executable cases pass.**

## Unblock determination

> ### **UNBLOCKED**

Measured against the two-step unblock path in
[run-2026-07-29-state-modules.md](run-2026-07-29-state-modules.md#overall-verdict):

| Step | Required | Status |
|---|---|---|
| 1 | **Harden the disclosure protocol** — "*either restate rule 9 imperatively, **or** embed the label in the citation-block template itself*" | **Done at `8cd5f93`, and both options were taken, not one.** Rule 9 is now imperative (`SKILL.md:22`) **and** the label is a stored verbatim block (`authorities.md:9–13`) — the mechanism the path identified as the one "*that made case 8 reliable*". |
| 2 | **Re-run case 1 at N≥5 and gate C at 5/5** — "*Uniform passing at N≥5 clears the block. Anything less records a measured intermittency rate and keeps it open.*" | **N=5 executed; C passes 5/5.** Uniform. No intermittency rate to record. |

Both steps are satisfied in the prescribed order. The block rested on exactly two
things — "*the rate is unmeasured and the protocol that produced it is
unhardened*" — and neither now holds: the protocol is hardened and the rate is
measured at 5/5.

The third path, the transcript audit, was already closed by the 07-29 file as
executed and exhausted, and was **not** re-attempted here.

**Two limits on what this clears**, neither of which reopens the block:

- **It clears the case-1 C block only.** It is not a re-validation of cases 2–9,
  which were not re-run, and it does not speak to trigger behavior.
- **It does not establish that the hardening caused the improvement** — see
  [Prompt provenance](#prompt-provenance--weighed-per-the-readme). The gate as
  written asks for a measured rate, not a causal claim, and the measured rate is
  uniform.

## Findings vs the executor's provisional notes

The notes are labeled provisional and are not verdicts. Graded from the
transcripts first, then reconciled against the notes.

**Overall: the notes reproduce this time.** Every factual claim in the five notes
was re-derived independently and holds, with one exception at finding 1. In
particular the claim made in all five — "*its wording character-identical to the
canonical block at `references/authorities.md`*" — is **confirmed byte-for-byte**,
and all five position claims ("final line" / "not the final line") are confirmed
against the response bodies. This is a change from 2026-07-29, where the executor
notes framed case 1 as uniform when the runs diverged on C.

### 1 — "each carry TY2026 inline" overstates four of the five runs

All five notes assert: "*Deferral limit, catch-ups, and the §415(c) figure each
carry TY2026 inline with FINAL status.*" For the **§415(c) $72,000 figure this is
accurate only in run C.** In A, B, D, and E the figure inherits its tax year and
status from a section heading or list stem rather than carrying either inline:

| Run | How the $72,000 appears | TY/status inline? |
|---|---|---|
| **A** | "*the $24,500 is separate from the §415(c) annual-additions limit of **$72,000***" — in a paragraph opening "*Two 2026-specific wrinkles worth knowing*" | No — paragraph-scoped |
| **B** | "*(The separate $72,000 §415(c) annual-additions limit *is* per unrelated employer.)*" | No — heading-scoped |
| **C** | "*§415(c) total annual additions …: **$72,000***", under the stem "*Related TY2026 figures, all FINAL:*" | **Yes** — list-scoped and explicit |
| **D** | "*Separate from the $72,000 §415(c) annual-additions limit*" | No — heading-scoped |
| **E** | "*Separate from the §415(c) annual-additions limit of **$72,000***" | No — heading-scoped |

**This does not change any verdict.** F is scored here as the 2026-07-29 grading
scored it, which read section-scoped tax years as satisfying "*state the tax year
inline*" — that grading applied the same phrase to the same $72,000 figure across
its three runs. Consistency of scoring across the two files matters more than
tightening the reading mid-gate, and a figure sitting under a heading that states
TY2026 is not a figure floating free of a tax year, which is what rule 1 targets.

Recorded for two reasons: the notes state as observed fact something that is
observed in only one of the five runs, and **the scope reading is doing real work
in four of five runs while appearing nowhere in the rubric text.** The next
grader should inherit the reading explicitly rather than re-deriving it — or the
rubric should say which scopes count.

### 2 — Rule 9 and `authorities.md` disagree on placement, and C cannot see it

The hardening wrote the placement duty differently in its two locations:

- `SKILL.md:22` — "*the response **ends** with the canonical index-only label*"
- `authorities.md:9` — "*end the **citation block** — or the response, if
  citations are inline*"

**Runs A and E satisfy the second and not the first.** Both consolidate citations
into an "Authorities in play" line, place the label immediately after it, and then
close with the educational disclaimer — so the label ends the citation block but
the response ends elsewhere. Run A's trailing text:

> Educational information only — not individualized investment, tax, or legal advice, and no advisory relationship is created. Figures are for the stated tax year and change. Decide with your fiduciary advisor, CPA, or estate attorney before acting.

Run E's is the same boilerplate in shorter form. Neither is a citation, so neither
leaves a citation unlabeled.

**Not a C failure, and not scored.** C's automatic-fail wording is presence-only —
"*an index-only citation is not labeled 'text not re-verified this session'*" — and
the label is present, canonical, and adjacent to the citations it governs in both
runs. Under `authorities.md`'s own branch structure both are conformant.

Recorded because the divergence is real and the rubric is blind to it: **2 of 5
runs do not satisfy rule 9's literal wording, and nothing in the scored set would
ever report that.** The executor notes deserve credit for capturing the raw fact —
all five record the label's position precisely, which is what made this checkable
— but position is data there, not assessment. The fix is a one-line reconciliation:
either soften `SKILL.md` rule 9 to match `authorities.md`'s two-branch rule, or
tighten `authorities.md` to require the response-final position. **`authorities.md`
is the better target to preserve**, since it is the single-source-of-truth file by
design and its two-branch rule is the more sensible one — a closing educational
disclaimer after the label is not a defect worth engineering against.

### 3 — Run E's unprompted interaction-check list is correct but out of scope

Run E volunteers the full rule-3 set, though the prompt describes no income spike:

> the checks that most often break an otherwise-correct analysis are: IRMAA two years forward (if either of you will be 63+ in the spike year), NIIT, the WA excise above, ACA marketplace premiums if pre-65, and Social Security benefit taxation if claiming. Happy to run that.

The executor recorded this as "*a factual difference from the other runs, not
assessed here*". Assessed: the list is complete and correct against
`SKILL.md:16` — all five members, correctly conditioned. **I is not mapped to case
1 and is not always-on, so it is not scored in either direction**, and it is
offered conditionally rather than executed, so it does not convert a lookup into
an unrequested scenario. No finding against it.

### Considered and deliberately not scored

- **NIIT `$250,000` without an inline tax year (runs A, C, D).** E.g. run A: "*an
  additional 3.8% on net investment income once MAGI exceeds **$250,000 MFJ**
  (FINAL, and *not* indexed…)*". No inline TY. Not an F violation, on the
  2026-07-29 precedent for the Form 5500-EZ `$250,000` threshold: a **stable,
  non-indexed** threshold is not an inflation-indexed tax-year figure.
  `2026-quick-reference.md:56` states "*NOT indexed*" in the source row, and every
  run that omits the year states the non-indexing in the same sentence. Runs B and
  E state TY2026 explicitly.
- **Collectibles / unrecaptured §1250 at 28% / 25% (runs C, E).** Rate structure,
  stated FINAL, inside a section headed TY2026. Same class as the 0/15/20%
  structure that all five state as FINAL. Matches `2026-quick-reference.md:57`.
- **The `~` hedging on threshold figures (runs C, D, E).** E.g. "*0% | up to
  ~$96,700*". Additional to the VERIFY flag, never a substitute for it — all three
  runs also state the flag in prose. Not an F concern in either direction.
- **Run A citing `IRC §414(b)/(c)/(m)` in a lookup answer.** Resolves to
  `authorities.md` and `business-owner.md`. Surfaced as an advisor question about
  the second §415(c) limit, not as a directive. X and R are not mapped to case 1;
  not scored.
- **Label rendering as blockquote vs plain line** (3 blockquote, 2 plain). The
  canonical block is stored as a blockquote in `authorities.md`, but the stored
  text is the sentence, not the `>` marker — the byte comparison above strips it.
  Not a fidelity defect.

## Carry-forward — open items not resolved by this run

Unchanged from 2026-07-29 unless noted:

- **Trigger behavior is still UNMEASURED.** All runs were path-pinned. P4 changed
  the skill description and nothing in this run or the prior one exercises the
  description-trigger path. It should not be inferred as passing.
- **C clause-1 scope — priority raised.** Now demonstrably outcome-determining for
  a release gate, not merely untidy. See
  [above](#the-1250--notice-2025-67-ruling-is-load-bearing-for-this-gate).
- **New: rule 9's placement wording is inconsistent between `SKILL.md` and
  `authorities.md`.** Finding 2. Cosmetic today; it becomes a real defect the
  moment someone writes a placement check against either file.
- **New: F's tax-year scope is unstated.** Finding 1. Four of five runs pass on a
  scope reading the rubric does not contain.
- **X's mapping (case 5 only)** still leaves arithmetic errors outside case 5 with
  no criterion to fail. Not exercised here — case 1 contains no reconciliation
  math.
- **The case-8 arithmetic error** remains in a recorded transcript and is
  untouched by this run.
- **The 2026-07-29 delta row is still marked Provisional** in the runbook's
  history table — the S/A wording and cases 8–11 harden only after control-plane
  review. This grading applied A as written and did not apply S/I/X/R to case 1.
