Session: phase0-state-modules-refactor. Base: state-modules @ fb95540.
Goal: restructure financial-strategy into a jurisdiction-neutral federal core +
pluggable state modules, per locked decisions D1-D4. WA behavior must be
indistinguishable from evals/baseline-v1.0-wa-only.md afterward.
HARD RULE for the entire session: no state-specific fact (rates, thresholds,
programs, flags) may be written from model memory. Content either moves from
existing verified files, comes from control-plane text quoted in this spec, or
is marked VERIFY/UNBUILT.

P0a. Spec-as-file: save this entire session prompt verbatim as
     plans/PHASE0-SPEC.md and commit it before any other change. (Process
     rule, new as of this phase: specs are files; the control plane's chat
     context is volatile and execution sessions cannot reach it.)

P0b. Errata commit (separate commit, before the refactor):
     Append to evals/baseline-v1.0-wa-only.md a dated "## Errata" section:
     - G1 delta corrected: the two defensible readings (surcharge threshold
       post- vs pre-deduction) differ by 2.9% x $278,000 = $8,062 on the
       Case 2 facts, not ~$27,500 ($27,522 = 9.9% x $278,000, corresponding
       to dropping the deduction entirely — not a defensible reading of
       RCW 82.87.020's definitional chain).
     - G1 resolved against the enrolled bill: ESSB 5813 sec. 101 amends RCW
       82.87.040 to impose (1)(a) 7% x an individual's Washington capital
       gains and (1)(b) an additional 2.90% x the portion of Washington
       capital gains exceeding $1,000,000 — "Washington capital gains" is the
       post-deduction defined term (RCW 82.87.020), so the $1M threshold is
       measured AFTER the standard deduction. Case 2's $82,078 embodies the
       correct reading; verdict unaffected.
     Baseline body above the Errata section is frozen.

P1. Directory restructure:
    - git mv skill references/washington.md -> references/states/washington.md
    - Create references/states/_template.md: fixed section order — Header
      (last-verified, sources, VERIFY conventions); Income tax; Estate &
      inheritance; Marital property; State programs; SUB-STATE LAYER (required
      section: county/metro/city income taxes; state resolution must return
      state + locality flags); Cross-state interactions (in-module per D1,
      with a "mirror" note convention: bilateral content names its counterpart
      file so refreshes update both); Authorities (same column schema as
      authorities.md's federal table); Advisor questions (3-5); Legislative
      watch.
    - Create references/states/_index.md: one row per state+DC, columns:
      code | income tax | taxes retirement income | estate tax | inheritance
      tax | community property | local income taxes | LTC/auto-IRA program |
      module | last verified. Fill ONLY the WA row (from washington.md, cite
      it) and an OR row marked "in progress (Phase 1)". ALL other rows: every
      flag cell = VERIFY, module = UNBUILT. Do not fill any flag from memory.

P2. states/washington.md upgrades (all sourced):
    - G1 fix at the rate section: state the mechanics explicitly — base 7% x
      "Washington capital gains" (the post-deduction, WA-allocated defined
      term, RCW 82.87.020/.060); additional 2.9% x portion exceeding
      $1,000,000; threshold measured after the standard deduction; cite RCW
      82.87.040 as amended by ESSB 5813 sec. 101. Note the equivalent bracket
      phrasing (7% to $1M post-deduction, 9.9% above) is arithmetically
      identical.
    - Move the Washington table out of authorities.md into this file's
      Authorities section, unchanged, same schema (D4).
    - Add Cross-state interactions stub: WA-resident-with-OR-metro-wages and
      WA<->OR relocation items, each marked "mirror: states/oregon.md
      (Phase 1)", content flagged VERIFY pending the Oregon build. Facts
      permitted now (control-plane verified): Oregon taxes nonresident
      OR-source wages; Metro SHS turns on physical presence within the Metro
      boundary, not employer location; WA has no income tax, so no credit
      mechanism exists on the WA side.
    - Conform header/sections to _template.md order.

P3. authorities.md slims to federal (D4): keep the federal map and retrieval
    protocol; add one convention line ("state authorities live in the state's
    own module under references/states/, same table schema"); remove the WA
    table (now moved). Add the Oregon source slate under the retrieval-
    protocol section, marked "Phase 1 input":
      ORS ch. 316 (income) and ch. 118 (estate) at
      oregonlegislature.gov/bills_laws/ors/ (note ch. 118 amended 2025 c.577,
      c.595 — ORS 118.145 natural-resource exemption, $15M cap); Oregon DOR
      (income, estate/OR-706, kicker); Portland Revenue Division
      (portland.gov/revenue/personal-tax — Metro SHS + Multnomah PFA);
      Multnomah County Code ch. 11 (PFA; rate-increase delay to 1/1/2027;
      TY2026 estimated-payment threshold $1,000->$5,000); Metro Code (SHS;
      June 2025 changes; TY2026+ threshold inflation-indexing — PFA
      thresholds NOT indexed); OregonSaves program rules. Watch list: 2025
      estate bills HB 2058/2112/2301/2362/3737, SB 380/405/648/764 —
      disposition to be recorded at build; PFA 0.8% rate increase eff.
      1/1/2027 (pre-positioned VERIFY for TY2027 refresh).

P4. SKILL.md changes:
    - Rule 4 becomes "State overlay": resolve the user's state AND locality
      where relevant; load references/states/<state>.md if it exists; if no
      module exists, answer the federal layer then emit the canonical
      fallback (verbatim; stored in guardrails.md as the single source):
      "State-level rules for [State] are not yet built into this skill. The
      federal analysis above stands; before acting, verify with your advisor:
      [State]'s income tax treatment of this item, any estate or inheritance
      tax, and marital-property regime." + one flag line per _index.md cell
      marked Y for that state (VERIFY cells contribute no flag line).
    - Rule 8: default state remains WA; add — ask rather than assume when the
      scenario involves relocation, cross-border income, or out-of-state
      property; never assume for estate-situs questions.
    - Workflow 3 intake: three separate state questions — residence,
      income-source state(s), real-property situs state(s).
    - Description: add generic triggers ("state income, estate, or
      inheritance tax", "moving to another state", "multi-state income or
      property"); keep all WA triggers; OR triggers wait for Phase 1.
    - Reference map: washington.md row -> states/washington.md; add rows for
      states/_index.md ("state resolution and unbuilt-state flags") and
      states/_template.md ("module authoring only").
    - Rule 6 unchanged in text; note it is now eval-enforced (criterion A).
P4a. guardrails.md: add the canonical fallback verbatim (single source of
     truth); refresh checklist gains per-module refresh stamps; _index.md
     rows refresh only when researched.
P4b. advisor-meetings.md G2 fix: explicit instruction at items 2/5/6 — when
     the conversation contains no gathered inputs / verified figures / prior
     meeting, return these as intake prompts or N/A; never synthesize.

P5. Runbook update (EVAL-RUNBOOK.md), per control-plane eval delta:
    - Criterion W generalizes to S (state overlay): correct module loaded for
      the resolved state OR the canonical fallback fired verbatim for an
      unbuilt state. Baseline's W scoring unchanged for cases 1-7.
    - New criterion A (rule 6): an assumption-dependent conclusion states the
      assumption in one line at the decision point.
    - New cases: 8 (unbuilt-state fallback: Idaho resident, estate question;
      asserts on the canonical wording), 9 (G2 adversarial cold-start "prep
      me" with zero context; passes only if items 2/5/6 return as intake
      prompts/N/A), 10 (WA resident, Portland-metro wages) and 11 (WA->OR
      relocation year) — author 10-11 now, mark "executable Phase 1 (requires
      states/oregon.md); Phase 1 acceptance tests".
    - Post-refactor protocol: results in evals/run-<date>-<branch>.md; Case 1
      runs N=3; grading by a SEPARATE session given transcripts + rubric, not
      the executor. Add an "eval delta history" table (dated: baseline scope
      = cases 1-7 / criteria F,C,W,I,X,R; this delta adds S,A + cases 8-11).
    - Run-condition caveat for results headers: post-refactor runs load the
      skill from the repo working tree; activation mechanics differ from the
      baseline's active-copy run; content is pinned either way.
    STOP GATE (soft): the four new case prompts + S/A criterion wording go in
    the SESSION REPORT for control-plane review; they harden only after
    review.

P6. Version + guard:
    - Bump personal-financial-strategy to 0.3.0. Two places move together:
      .claude-plugin/plugin.json version, and a "Version: 0.3.0" line at the
      top of the BODY of skills/financial-strategy/SKILL.md — body, not
      frontmatter, so the skill validator's schema is untouched. From this
      point every packaged .skill and serving copy answers "which release is
      this?" by inspection, and the release-log identifiers become
      cross-checks rather than the only evidence.
    - check.py assertion (new): when a SKILL.md body contains a "Version:"
      line, it must equal that plugin's plugin.json version; mismatch = check
      failure. (The version-bump gate validates plugin.json only; this closes
      the unguarded two-places invariant.)
    - check.py clean. Logical commits fine (spec / errata / restructure /
      rules / evals / version). Push state-modules; verify remote SHA.
      DO NOT merge to main.

P7. Eval run: execute cases 1-9 (Case 1 x3) in fresh contexts against the
    refactored working tree, no web retrieval, default household lens. Write
    transcripts to evals/transcripts/run-<date>/. Do NOT self-grade beyond
    provisional notes; grading happens in a separate session. Commit + push.

SESSION REPORT: standard template + PUSHED line + P5 STOP GATE content + 
provisional eval observations (labeled provisional).
