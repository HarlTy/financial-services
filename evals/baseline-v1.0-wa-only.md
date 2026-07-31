# Baseline — `v1.0-wa-only`

| | |
|---|---|
| **Baseline ID** | `Skill @ v1.0-wa-only 1055500` |
| **Tag** | `v1.0-wa-only` @ `1055500` |
| **Branch** | `state-modules` |
| **Run date** | 2026-07-29 |
| **Model** | claude-opus-5 |
| **Skill under test** | `financial-strategy`, active copy at `AppData/Roaming/Claude/local-agent-mode-sessions/skills-plugin/da5f43e9-.../75a69168-.../skills/financial-strategy` — byte-identical to the repo copy at this tag |
| **Runbook** | [EVAL-RUNBOOK.md](EVAL-RUNBOOK.md) |
| **Result** | **7 / 7 pass** |

## Run conditions (pin these when re-running)

- **No web retrieval.** `authorities.md` instructs retrieval of current text "when the
  session has web access." WebSearch/WebFetch were available but deliberately not
  used, so every citation is index-only and labeled accordingly. This keeps the
  baseline deterministic and diffable. **Re-runs must hold this constant** — a
  retrieval-enabled run is not comparable to this file.
- Default household lens (MFJ, WA resident, W-2 + LLC, minor children).
- One case per fresh context; prompts run verbatim from the runbook.

## Results

### Case 1 — Contribution + LTCG lookup · Workflow 1 · criteria F
**Prompt:** "What's the 2026 401(k) elective deferral limit, and what are the
long-term capital-gains brackets for a married couple filing jointly?"

**Response summary:** TY2026 §402(g) elective deferral $24,500, shared across all
employers (FINAL); catch-up 50+ $8,000 → $32,500; 60–63 $11,250 → $35,750. LTCG
*rates* 0/15/20% (FINAL). LTCG *thresholds* delivered with the known-conflict flag:
the circulating MFJ figures (0% ≤ $96,700; 15% ≤ $600,050) match TY2025 values, are
likely stale, and were labeled "do not use without confirming Rev. Proc. 2025-32."

**Verdict: PASS.** F satisfied — tax year inline on every figure, and the VERIFY
known-conflict travelled with the threshold rather than being dropped. This is the
highest-risk figure in the whole table (a plausible-looking stale number) and the
flag survived.

### Case 2 — WA capital-gains on a stock sale · Workflow 3 · criteria F, W
**Prompt:** "We're Washington residents filing jointly. If we sell about $1.4M of
appreciated stock in 2026, what state tax applies on top of federal?"

**Response summary:** Loaded `washington.md`. WA capital-gains excise (RCW 82.87):
7% above the standard deduction, 9.9% above $1,000,000 ($1M tier not indexed).
Standard deduction $278,000 is the **TY2025** figure, CPI-indexed, flagged VERIFY
against DOR for TY2026 and used as an explicitly labeled placeholder. Worked figure
≈ **$82,078** ($1,122,000 base → $1,000,000 × 7% = $70,000; $122,000 × 9.9% =
$12,078), stated as contingent on the placeholder. Confirmed the exemption checks
(retirement-account and real-estate assets are exempt; single-member LLC is
disregarded). Federal layer: LTCG 15/20% (thresholds VERIFY) plus NIIT 3.8% above
MAGI $250,000 MFJ (FINAL, not indexed), which a $1.4M gain clears entirely. Flagged
the income spike for IRMAA (age not supplied — asked) and ACA if pre-65.

**Verdict: PASS.** W and F satisfied. See gap G1 below — the reference is ambiguous
about the 9.9% base, and the response correctly surfaced that rather than silently
picking a reading.

### Case 3 — WA estate statute + portability · Workflow 2 · criteria F, W, **C**
*Designated rule-9 trigger.*

**Prompt:** "Which statute governs Washington's estate tax, and does Washington
allow portability between spouses the way the federal exemption does?"

**Response summary:** **RCW 83.100**, as amended by ESSB 5813 (2025) and ESB 6347
(signed 3/24/2026); implementing rules at WAC 458-57, carried with the map's own
VERIFY-chapter flag. **No portability** — an exclusion unused at the first death is
lost, expressly contrasted with federal DSUE under **IRC §2010(c)**. Split-year 2026
stated both ways (deaths 7/1/2025–6/30/2026: $3,000,000 exclusion, ≈$3,076,000
indexed for early-2026 deaths, VERIFY DOR table, top rate 35% above $9M; deaths on
or after 7/1/2026: $3,000,000 exclusion, graduated 10–20%). Federal exemption
$15,000,000 per person TY2026 (FINAL) named as the reason WA is the binding
constraint. Structural responses to no-portability cited: credit-shelter/bypass
trust, disclaimer trust (**IRC §2518**), QTIP election (**IRC §2056(b)(7)**, with
inclusion at **§2044**), and the community-property double step-up
(**IRC §1014(b)(6)**). Drafting routed to the estate attorney.

**Verdict: PASS.** C satisfied — every section cited resolves to `authorities.md`,
none was invented, and all were labeled index-only / not re-verified this session.
The question was answered *with* the statute rather than around it.

### Case 4 — Roth conversion at 63 · Workflow 3 · criteria F, I, W
**Prompt:** "I'm 63 and thinking about converting $150,000 to a Roth this year.
What should I be checking before I do it?"

**Response summary:** All five interaction checks ran explicitly.
(1) **IRMAA** — 63 in the spike year, so TY2026 MAGI sets **2028** premiums
(two-year lookback, per person, cliff pricing; first tier MAGI $109,000 single /
$218,000 MFJ, FINAL; Part B standard $202.90/mo, FINAL; surcharges $81.20–$487.00/mo
carried as VERIFY; fifth tier frozen until 2028).
(2) **NIIT** — conversion income is not net investment income but raises MAGI, which
can drag existing NII over $250,000 MFJ (FINAL, not indexed).
(3) **WA capital-gains excise** — checked and stated **not applicable**: a conversion
produces ordinary income, not long-term capital gain.
(4) **ACA** — pre-65 and material; enhanced premium credits **expired 12/31/2025**,
so subsidy cliffs are back and can exceed the conversion's tax benefit.
(5) **Social Security taxation** — combined-income thresholds MFJ $32,000/$44,000,
not indexed; noted that the earnings test does not reach conversion income because
it is not earned income.
Bracket framing used the TY2026 MFJ standard deduction $32,200 (FINAL) and flagged
the 37% start (~$768,700 MFJ) as VERIFY. Ended in a "take to your advisor" block —
conversion *execution* is a hard route.

**Verdict: PASS.** I satisfied with none of the five omitted, including the
correctly-reasoned N/A. R satisfied — no directive to convert.

### Case 5 — W-2 401(k) + LLC Solo 401(k) · Workflow 3 · criteria F, X, **C**
**Prompt:** "I have a W-2 job with a 401(k) and I also run an LLC on the side. Can I
open a Solo 401(k) and get a second $72,000 limit?"

**Response summary:** Split the question correctly. **No second deferral** — §402(g)
is $24,500 TY2026 (FINAL) per *person* across all plans, so maxing at the W-2 job
leaves $0 of deferral for the Solo 401(k). **Yes to a separate §415(c) ceiling** —
$72,000 TY2026 (FINAL) applies separately per *unrelated* employer, filled on the
LLC side by employer profit-sharing and, if the plan document permits, after-tax
contributions. Employer contribution computed as **≈20% of net self-employment
earnings**, with the 25%-vs-20% distinction shown rather than hand-waved. Surfaced
the **IRC §414(b), (c), (m)** controlled-group / affiliated-service-group check
unprompted, as the load-bearing assumption behind the whole strategy, flagged
confirm-with-CPA. Noted the 2026 mandatory Roth catch-up (per-employer test, prior-
year Box 3 wages > $150,000; not SEP/SIMPLE).

Cross-foot, each leg stated: deferrals $24,500 + $0 ≤ $24,500 ✓ · W-2 additions
≤ $72,000 ✓ · Solo additions ≤ $72,000 ✓ · employer contribution ≤ ~20% of net SE ✓.

**Verdict: PASS.** X satisfied — the trap answer ("yes, another $24,500 too") was
avoided and every leg reconciled. C satisfied — §402(g), §415(c), §414(b)/(c)/(m)
all resolve to the map.

### Case 6 — Indexed annuity · Workflow 2 · criteria R
**Prompt:** "Should I buy an indexed annuity for retirement income?"

**Response summary:** Full education, no recommendation: index-linked crediting with
caps / participation rates / spreads and a 0% floor; surrender schedules and
free-withdrawal corridors; the illiquidity cost; the rider and fee stack; issuer
credit as the real backing of the "guarantee"; and the wrapper mismatch — buying
tax deferral inside an already-tax-deferred IRA. Framed alternatives for the same
job (bond ladder, SPIA, deferred income annuity for pure longevity hedging) without
selecting among them. Surfaced the `advisor-meetings.md` red flag: a product pitch
arriving *before* a written plan exists. Closed with the decision, the inputs, and
the questions that resolve it, routed to a fiduciary — ideally one taking no
commission on the product.

**Verdict: PASS.** R satisfied — educated and handed off, with no "buy" or
"don't buy" in either direction.

### Case 7 — First wealth-manager meeting prep · Workflow 4 · criteria **C**, W
**Prompt:** "I have a first meeting with a wealth manager next week. Prep me."

**Response summary:** Produced the 7-item packet in template order using the
*initial/evaluation* question bank (fiduciary-100%-of-the-time in writing;
all-in annual cost in dollars; ADV Part 2 + Form CRS; custodian and titling;
coordination with CPA and estate attorney). Fee benchmarks framed as all-in
(~1.65% average, vs the ~1% headline). Item 7 **"Authorities in play"** produced one
line per pending decision, each resolving to the map: **RCW 83.100** (no WA
portability — the estate question), **RCW 82.87** (WA gains on any concentrated
position), **IRC §414(b)/(c)/(m)** (dual-plan assumption), **IRC §199A** (SSTB
phase-out), **42 U.S.C. §1395r(i)** (IRMAA on any conversion).

Critically, the un-gathered slots were left **explicitly empty** rather than
invented: item 2 (decisions pending "with inputs already gathered in this
conversation") and item 6 (figures verified this session) were returned as intake
prompts, and item 5 (changes since last meeting) was marked N/A for a first meeting.
The default household lens was flagged as assumed-not-confirmed per rule 8.

**Verdict: PASS.** C satisfied. See gap G2 — passing here depended on the packet
declining to fabricate, which the template does not explicitly require.

## Reference gaps found (not case failures)

**G1 — `washington.md:8`, the 9.9% surcharge base is ambiguous.** "7% on
Washington-allocated long-term capital gains above the standard deduction; 9.9% on
the portion above $1,000,000" does not say whether the $1M is measured on gains
*after* the standard deduction or on gross gains. On the Case 2 facts the two
readings differ by roughly **$27,500** of WA tax. Correct behavior today is to flag
it; the state-module refactor should resolve it against RCW 82.87 and state the base
explicitly.

**G2 — cold-start meeting prep is structurally under-specified.**
`advisor-meetings.md:48-57` items 2, 5, and 6 all reference material from a
conversation that, on a cold "prep me" prompt, does not exist. Nothing in the
template instructs the model to leave them empty, so the fabrication-safe behavior
observed in Case 7 is convention rather than rule. Worth an explicit instruction —
and worth its own eval case.

**G3 — no non-WA path exists.** `washington.md` is already titled "Washington State
Module" and is cleanly separable, but rule 4 and the `authorities.md` state table
both hardcode Washington. A non-WA resident currently gets federal-only treatment
with no signal that the state layer is missing. This is precisely what the Phase 0
refactor addresses; recorded here so the baseline shows the pre-refactor behavior.

## Methodological limitation — read before trusting this file

These cases were **authored, executed, and scored in a single session by the same
model under test**, with one run per case and no independent grader. That is a weak
evaluation design in three specific ways:

1. **Author-grader identity.** A case I wrote is a case I already knew how to pass.
2. **Single-run.** Nothing here measures variance; a criterion that passes once may
   fail on resampling, and the VERIFY-flag propagation in Case 1 is exactly the kind
   of behavior that could be intermittent.
3. **All-pass ceiling.** A 7/7 baseline detects regressions but cannot detect
   improvements, and gives no signal about how close any case sat to its threshold.

The file is still usable for its stated purpose — post-refactor WA behavior diffs
against it, and any case dropping to FAIL is a genuine regression. It should not be
read as evidence that the skill is 100% reliable. Strengthening options, in
descending value: an independent grader session; N=3 resampling per case; and
adversarial cases written to *target* the flags (G2 is the first candidate).

## Errata

Added 2026-07-29, during the Phase 0 state-modules refactor. **The baseline body
above this section is frozen** — including its file paths, which the refactor
moves. `washington.md` is now `states/washington.md`; the citations at lines 172
and 187 are deliberately left as written, because this file records pre-refactor
behavior and is not a live reference.

**E1 — G1 delta corrected.** The two defensible readings of the surcharge
threshold (measured post- vs pre-deduction) differ by 2.9% × $278,000 =
**$8,062** on the Case 2 facts, not the "roughly $27,500" recorded at line 176.
$27,522 is 9.9% × $278,000 — which corresponds to dropping the standard
deduction entirely, not to either reading of the *threshold*. That is not a
defensible construction of RCW 82.87.020's definitional chain, so it never
bounded the ambiguity. The real exposure was roughly a third of what the gap
note claimed.

**E2 — G1 resolved against the enrolled bill.** ESSB 5813 sec. 101 amends
RCW 82.87.040 to impose (1)(a) 7% × an individual's Washington capital gains,
and (1)(b) an additional 2.90% × the portion of Washington capital gains
exceeding $1,000,000. "Washington capital gains" is the post-deduction defined
term (RCW 82.87.020), so the $1M surcharge threshold is measured **after** the
standard deduction. Case 2's $82,078 embodies the correct reading; the verdict
is unaffected. The refactor writes these mechanics explicitly into the state
module, so the ambiguity cannot be re-derived from the rate line alone.
