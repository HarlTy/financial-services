# Case 2 — WA capital-gains on a stock sale

**Criteria mapped:** F, S. F/C/A scored on every case.
**Baseline comparison point:** the baseline's Case 2 answer was **$82,078**.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "We're Washington residents filing jointly. If we sell about $1.4M of appreciated stock in 2026, what state tax applies on top of federal?"

## Response

## Short answer

Washington has **no state income tax on this gain** — but it has a separate **capital-gains excise tax** (RCW 82.87), and a $1.4M long-term stock gain lands squarely in its top tier. Structurally it is **7% of your "Washington capital gains," plus an additional 2.90% on the portion above $1,000,000** — arithmetically 7% / 9.9% brackets. *Quinn v. State* (Wash. 2023) upheld it as an excise rather than an income tax, which is why it coexists with the state's no-income-tax posture. (Citations from the skill's authority index — statutory text not re-verified this session; no web access here.)

The number that decides your bill is **not the $1.4M**. Two things move it:

## Assumption 1: gain, not proceeds

The excise applies to the **gain**, not the sale amount. "Selling about $1.4M of stock" is ambiguous, and the difference is large:

| If $1.4M is… | Long-term gain | WA excise (TY2025 deduction as placeholder) |
|---|---|---|
| the **gain** | $1,400,000 | **~$82,078** |
| **proceeds** with $400k basis | $1,000,000 | **~$50,540** — no surcharge at all |

The rest of this answer assumes **$1.4M is the realized long-term gain**, all allocated to Washington, on non-exempt assets. Also assumed: you were WA-domiciled for all of 2026 with no mid-year relocation and no gain sourced across a state line — a WA↔OR move or Oregon-sourced work would change the analysis, and that cross-state section of the skill's WA module is an unauthored stub.

## Assumption 2: the standard deduction figure

"Washington capital gains" is a **defined term** (RCW 82.87.020, allocation under RCW 82.87.060): long-term gain allocated to WA, **net of the standard deduction**.

- Standard deduction: **$278,000 for TY2025**, CPI-indexed. **The TY2026 amount is a flagged VERIFY** — confirm at WA DOR before you compute a real number. I use $278,000 below as a clearly labeled placeholder.
- Sensitivity: because your base sits above $1M, every $1,000 the TY2026 deduction rises cuts the tax by **$99**. A ~2.8% index bump would trim roughly $770.
- **Also VERIFY: whether each spouse gets a deduction.** The tax falls on *individuals*, and the WA module does not address how the deduction works for a married couple or for shares held separately by each spouse. That is a live, material question for your CPA — I won't guess at it.

## The math (TY2026, with the deduction flagged)

| Step | Amount |
|---|---|
| Long-term gain allocated to WA | $1,400,000 |
| Less standard deduction (TY2025 placeholder — **VERIFY TY2026**) | ($278,000) |
| **"Washington capital gains" (post-deduction base)** | **$1,122,000** |
| 7% under RCW 82.87.040(1)(a) | $78,540 |
| Additional 2.90% on base above $1,000,000 → 2.90% × $122,000 | $3,538 |
| **WA excise tax** | **~$82,078** |

Cross-foot via the bracket phrasing: 7% × $1,000,000 = $70,000, plus 9.9% × $122,000 = $12,078 → $82,078. Same answer, as it must be (7% + 2.90% = 9.9%). Effective rate on the gain: **5.86%**. Return due **April 15, 2027**.

**The trap worth knowing:** the $1M surcharge threshold is measured **after** the standard deduction, not on gross gain. The commonly seen phrasing leaves this ambiguous, and on a $278,000 deduction the two readings differ by 2.9% × $278,000 = $8,062. The post-deduction reading is the correct one. The $1M threshold is **not** indexed.

## Interaction checks — what else this spike sets off

The state excise is rarely the only consequence of a $1.4M realization year:

- **NIIT (federal, often forgotten):** 3.8% on net investment income above $250,000 MAGI (MFJ, TY2026, **not indexed**). At this size effectively the whole gain is exposed — roughly **$53,200**. Combined marginal on your top slice: 20% federal + 3.8% NIIT + 9.9% WA = **33.7%**. (Federal 20% rate is FINAL; the TY2026 LTCG bracket thresholds carry a **known-conflict VERIFY** — circulating figures match TY2025 — but at $1.4M MFJ you clear the 20% breakpoint under either version.)
- **IRMAA, two years forward.** 2026 income sets **2028** Medicare premiums. This matters if **either spouse will be 63 or older in 2026** — you haven't told me your ages, so I can't resolve it. IRMAA is assessed **per person**, and each tier is a **cliff** ($1 over triggers the full surcharge). For scale, the TY2026 first tier starts at $218,000 MAGI (MFJ); a $1.4M gain reaches the top tier. The 2028 tier dollars are not in this skill's tables.
- **ACA, if either of you is under 65 and on marketplace coverage.** The enhanced premium tax credits expired 12/31/2025 and the subsidy cliff is back — a $1.4M-gain year wipes out any credit for that year.
- **Social Security taxation, if claiming.** At this income, 85% of benefits are included; those thresholds are not indexed.
- **Short-term lots are outside the WA excise** — it reaches long-term gain only. Federally they're worse (ordinary rates); at the state level they're free. Check your lot holding periods before assuming a uniform answer.
- **Retirement-account shares are exempt** from the WA excise entirely, as is real estate. If part of that $1.4M sits in an IRA or 401(k), it never enters this base.

## Three ways this could be structured (tradeoffs, not a recommendation)

**A. Realize it all in 2026.** WA excise ~$82,078. One standard deduction, and $122,000 exposed to the 9.9% tier. Simplest; highest state cost. *Assumes no other 2026 long-term gains — any additional gain stacks on top at 9.9%.*

**B. Split across 2026 and 2027 ($700k each).** Two standard deductions, and neither year's post-deduction base reaches $1M, so no surcharge: 7% × $422,000 = **$29,540 per year → $59,080 total. Roughly $22,998 less than A.** Decomposes as 7% × $278,000 (second deduction) = $19,460 plus $3,538 of avoided surcharge. *Assumes the TY2027 deduction is at least as large, that the statute is unchanged — WA amended both its capital-gains and estate statutes within 13 months — and that you're willing to carry the position another year. That last one is market risk, not a tax question, and I make no forecast about it.*

**C. Divert a slice to charity instead of selling it.** Appreciated shares gifted rather than sold produce no realized gain, so nothing enters the WA base or the federal one. Note two TY2026 federal changes to the giving math: a **0.5%-of-AGI floor** on itemized charitable deductions, and a $2,000 MFJ non-itemizer deduction. Also worth weighing against C: Washington's **community-property double basis step-up** (IRC §1014(b)(6)) means appreciated community assets held until the first spouse's death get a **full** step-up on both halves — which can make "don't sell these particular shares at all" the strongest alternative, if the cash need can be met elsewhere.

Also, don't conflate two things that share a number: WA's proposed **9.9% income tax on income over $1M (ESSB 6346, effective 2028)** is a different instrument from the capital-gains surcharge above. It faces a repeal initiative (I-645) on the **November 3, 2026 ballot** plus a pending constitutional challenge. Treat it as unsettled — don't plan around it surviving *or* dying.

## Take to your advisor

**The decision:** how much long-term gain to recognize in 2026 versus 2027, and whether any of it goes to charity or is held for step-up instead. Trade timing and the tax-return position are your CPA's and advisor's calls, not mine.

**Inputs used here:** $1.4M assumed as long-term gain, WA-allocated, non-exempt, MFJ, WA-domiciled all year; $278,000 standard deduction as a TY2025 placeholder; TY2026 federal figures per the skill's verified tables.

**Questions that resolve it:**
1. **CPA:** What is the confirmed **TY2026 WA standard deduction** at DOR, and does each of us get one — or does the deduction apply once to the couple? (RCW 82.87)
2. **CPA:** Run the excise one-year versus split-across-two, with the $1M surcharge tier measured **post-deduction**, and tell me what other 2026 gains would stack into that tier.
3. **CPA:** Confirm the lots are all long-term and none are in a retirement account or otherwise exempt under RCW 82.87.
4. **Advisor:** Will either of us be 63+ in 2026? If so, model the **2028 IRMAA** consequence — per person, cliff-priced, two-year lookback (42 U.S.C. §1395r(i)).
5. **Advisor / attorney:** Given the WA community-property double step-up (IRC §1014(b)(6)), are these the right shares to sell at all, or should the cash come from lower-basis-risk assets?

**Authorities in play:** RCW 82.87 (rate mechanics at RCW 82.87.040 as amended by ESSB 5813 (2025) sec. 101; defined terms RCW 82.87.020; allocation RCW 82.87.060); *Quinn v. State* (Wash. 2023) — reporter pin cite VERIFY; IRC §1(h) (LTCG rates); IRC §1411 (NIIT); IRC §1014(b)(6) (community-property step-up); 42 U.S.C. §1395r(i) (IRMAA). Citations from the skill's authority index — text not re-verified this session.

Educational information only — not individualized investment, tax, or legal advice, and no advisory relationship is created. Figures are for the stated tax year and change. Decide with your fiduciary advisor, CPA, or estate attorney before acting.

## Provisional executor note (NOT a verdict)

**$82,078 matches the baseline exactly**, and the response now states the
post-deduction mechanics explicitly and cross-foots the 7%+2.90% path against
the 7%/9.9% bracket path to the same figure. The $8,062 delta from the P0b
errata appears in the answer. Grading is a separate session.
