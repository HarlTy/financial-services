# Case 4 — Roth conversion at 63

**Criteria mapped:** F, I, S. Criterion I requires every applicable interaction
check: IRMAA two-year lookback (63+), NIIT, WA capital-gains excise, ACA (pre-65),
Social Security taxation.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "I'm 63 and thinking about converting $150,000 to a Roth this year. What should I be checking before I do it?"

## Response

## Assumptions I'm using (correct any that are wrong before this drives a decision)

Per the default household lens: **married filing jointly, Washington resident, W-2 wages plus LLC self-employment income.** You gave me an age and a dollar amount, so everything below is a checklist and a framework rather than a computed result — I don't have your filing status, other 2026 income, account balances by tax bucket, or whether either of you has started Social Security or Medicare. I've flagged where each missing input changes the answer.

Two facts about you specifically that reorder the usual checklist:

- **At 63, this conversion year is an IRMAA lookback year for your first Medicare years.** 2026 Medicare IRMAA is based on 2024 MAGI (two-year lookback) — so a 2026 conversion prices your 2028 Part B and Part D, right around when you turn 65.
- **If you were born in 1960 or later, your RMD age is 75, not 73** (SECURE 2.0). At 63 that's roughly a 12-year conversion window ahead of you. That materially weakens the case for doing $150,000 in a single year and strengthens a ladder.

---

## 1. Sizing: bracket headroom

The method is: target bracket ceiling minus projected 2026 taxable income = conversion capacity.

TY2026 figures I can verify:
- Standard deduction **$32,200 MFJ** (FINAL). You do **not** yet get the additional 65+ deduction ($1,650 per qualifying spouse MFJ, FINAL) or the OBBBA senior bonus deduction ($6,000 per person 65+, TY2025–2028) — both require age 65.
- Bracket structure 10/12/22/24/32/35/37%, permanent under OBBBA (FINAL). The 37% bracket begins ~$768,700 MFJ (**VERIFY** exact threshold against Rev. Proc. 2025-32).

**A gap you should know about:** the exact TY2026 dollar thresholds where the 22%, 24%, and 32% brackets begin for MFJ are **not in my reference tables**. I won't estimate them. Before anyone sizes $150,000 against a "fill the 24% bracket" target, those thresholds need to come off Rev. Proc. 2025-32 directly. Ask your CPA to confirm the 24% ceiling for MFJ in 2026 — that number is the whole sizing exercise.

## 2. IRMAA, two years forward — the check most often missed at 63

- IRMAA is assessed **per person** and every tier is a **cliff**: $1 over triggers the full surcharge for the year.
- 2026 first tier begins at MAGI **$109,000 single / $218,000 MFJ** (FINAL). Your 2028 tier thresholds will be different and aren't in my tables — treat the 2026 numbers as the shape of the thing, not your actual test.
- 2026 Part B standard premium is **$202.90/month** (FINAL). Surcharges add **$81.20–$487.00/month** for Part B and **$14.50–$91.00/month** for Part D (both **VERIFY** — secondary source only, exact dollars unconfirmed).
- **Filing jointly means one spike surcharges both of you.** The conversion lands on one person's 1099-R, but joint MAGI sets each spouse's surcharge independently. If your spouse is older and already on Medicare, the cost roughly doubles — and if they're already enrolled, check whether an earlier lookback year is also in play.
- The first four tiers are indexed; the fifth is frozen until 2028 (FINAL).

Because the determination runs on a rolling two-year lookback, a single-year spike hits a single determination year rather than becoming permanent. That can make a knowing one-year surcharge a rational toll — but confirm the mechanics and the tier arithmetic with your advisor before treating it as cheap.

## 3. ACA marketplace premiums — urgent if you're pre-65 and not on employer coverage

**Enhanced premium tax credits expired December 31, 2025** and were not extended as of my last verification (2026-07-28; politically live, VERIFY current status). Subsidy cliffs are back. If you're bridging to 65 on a marketplace plan, a $150,000 conversion can cost you the entire credit — frequently a larger, more immediate hit than the IRMAA surcharge two years out. If you're on employer or retiree group coverage instead, this check drops out entirely.

## 4. Social Security benefit taxation — only if someone is claiming

If either of you has claimed (possible from 62), a conversion of this size will push essentially all of the benefit into taxable territory. MFJ: 0% below $32,000 combined income, up to 50% taxable at $32,000–$44,000, up to 85% above $44,000. **These thresholds are not indexed** (FINAL). OBBBA did *not* exempt benefits from tax — the senior bonus deduction is a separate item.

Not claiming yet? Then this window (before Social Security starts, before RMDs at 75) is exactly the low-income runway the conversion playbook is built around, and it's larger than most people's.

## 5. NIIT

3.8% on net investment income above MAGI **$200,000 single / $250,000 MFJ**, not indexed (FINAL). The conversion itself isn't net investment income — but it raises MAGI, which can drag your dividends, interest, and realized gains over the gate.

## 6. Where the tax money comes from — and the Washington excise trap

Paying the conversion tax from taxable funds rather than from the converted dollars preserves more of the conversion's value. But if you sell appreciated taxable holdings to raise ~$30–50k of tax:

- **Washington's capital-gains excise tax** applies (RCW 82.87): **7%** of "Washington capital gains," plus an additional **2.90%** on the portion above **$1,000,000** — and the $1M threshold is measured **after** the standard deduction, not on gross gain. Standard deduction was **$278,000 for TY2025**, CPI-indexed; **the TY2026 amount must be verified at WA DOR before you compute anything** (VERIFY).
- Assets inside retirement accounts are **exempt** from the excise, as is real estate. So the conversion itself is outside it — the exposure comes only from the taxable-account sales you make to fund the tax.
- WA parameters changed in both 2025 and 2026. Re-verify the current DOR tables rather than relying on any figure more than a few months old.

## 7. Washington state income tax — what I can and can't tell you

Washington imposes **no state income tax on wages**, and the capital-gains levy is a separate *excise* tax rather than an income tax (*Quinn v. State*, Wash. 2023). But my Washington module **has not researched how retirement income — pension, IRA, or annuity distributions — is treated**, and I won't infer "not taxed" from the absence of a wage income tax. Treat the state-side cost of the conversion as **VERIFY**, and confirm it with your CPA.

Also pending and unsettled: **ESSB 6346** would impose a 9.9% Washington tax on income over $1M effective 2028, with repeal initiative **I-645** on the November 3, 2026 ballot and a constitutional challenge pending. Don't build a multi-year ladder that assumes it either survives or dies.

## 8. Washington estate tax — a reason a conversion can help here

WA exclusion is **$3,000,000** with **no portability between spouses** — an unused exclusion at the first death is simply lost (RCW 83.100). Rates are 10%–20% for deaths on/after 7/1/2026 (ESB 6347, signed 3/24/2026); the 35% top rate applied to deaths 7/1/2025–6/30/2026. Against a federal exemption of $15,000,000 per person, **Washington is the binding constraint** for most affected households, and a closely held LLC interest can push an estate over $3M fast.

Relevance to your conversion: tax paid from taxable funds leaves your estate, shrinking the WA-taxable estate while moving the same dollars into a Roth that grows tax-free for heirs. If your combined estate is anywhere near $3M, this is a point in favor of converting — and a point for coordinating it with your estate attorney rather than treating it as a standalone tax decision.

## 9. Competing uses for the same pre-tax dollars

**QCDs** become available at 70½ — up to **$111,000 per person (TY2026, indexed)**, direct from the IRA, excluded from AGI. An AGI *exclusion* beats a deduction for IRMAA and Social Security-taxation purposes. If you're charitably inclined, converting every pre-tax dollar now removes the best future vehicle for that giving. Size the conversion to leave the QCD runway intact.

---

## Three ways to shape this

**A — Convert $150,000 in 2026 as planned.**
Cleanest if you're on employer coverage (no ACA exposure), not claiming Social Security, and the RMD bulge at 75 is large enough that a single-year 2028 IRMAA surcharge is worth paying knowingly.
*Assumes: current marginal rate stays below your projected rate at 75+, and the 2028 IRMAA tier cost is quantified before you commit rather than discovered in 2028.*

**B — Ladder it across the window to age 75, sized annually to a bracket ceiling and to stay under the next IRMAA tier.**
With a ~12-year runway (RMD age 75 for the 1960+ cohort), you likely don't need $150,000 in one year. Convert to a bracket target each year, re-testing the IRMAA cliff each time.
*Assumes: the bracket structure holds — it's permanent under OBBBA, so this is a weaker assumption than usual — and that income stays predictable enough to size each year in Q4.*

**C — Front-load now while pre-Medicare, then taper.**
If you're 63 in 2026 and won't be Medicare-enrolled until 2028, and you're *not* on a marketplace plan, 2026 may be your last year genuinely free of both the ACA cliff and any IRMAA consequence you can still see coming. Convert larger now, smaller after 65.
*Assumes: no marketplace coverage in 2026, and that you accept converting before you're eligible for the 65+ deductions.*

Note against C: once you're 65 (2028), you gain the additional 65+ standard deduction ($1,650/spouse MFJ) and the OBBBA senior bonus deduction ($6,000/person) — but that senior bonus phases out starting around **$150,000 MAGI MFJ** (**VERIFY** thresholds), so a large conversion in 2028 would destroy it, and the provision expires after 2028 regardless.

---

## Take to your advisor

**The decision:** whether to convert $150,000 in 2026, or ladder a smaller amount annually across the window to RMD age 75.

**Inputs I used:** age 63; $150,000 proposed conversion; assumed MFJ, WA resident, W-2 + LLC income. **Not supplied and required before sizing:** your 2026 projected taxable income before the conversion; balances split across taxable / tax-deferred / Roth / HSA; health coverage type in 2026–2027; whether either spouse has claimed Social Security or is already on Medicare; your spouse's age; combined estate value; charitable intent.

**Questions that resolve it:**

1. **CPA:** What is the TY2026 24%-bracket ceiling for MFJ per Rev. Proc. 2025-32, and what does $150,000 of conversion income do to our marginal rate and to NIIT exposure under IRC §1411?
2. **CPA:** How does Washington treat retirement-account distributions for state purposes? My reference material confirms no wage income tax but does not establish retirement-income treatment.
3. **Advisor:** Model this conversion against the IRMAA tiers under 42 U.S.C. §1395r(i) — two-year lookback, per person, cliff pricing — and show me the projected 2028 Part B and Part D cost for **both** of us at $150,000 versus at a tier-limited amount.
4. **Advisor/CPA:** If we're on a marketplace plan in 2026, what does this conversion cost us in premium tax credit under IRC §36B now that the enhanced credits have expired?
5. **CPA:** If we sell taxable holdings to pay the tax, what is the WA capital-gains excise cost under RCW 82.87 — using the confirmed TY2026 standard deduction, not the TY2025 $278,000 figure?
6. **CPA:** Confirm my RMD beginning age under IRC §401(a)(9) — 75 if born 1960 or later — so we know the true length of the conversion window.
7. **Estate attorney:** Given Washington's ~$3M exclusion and no portability under RCW 83.100, how does paying conversion tax from taxable assets interact with preserving both exclusions (credit-shelter, disclaimer under IRC §2518, or QTIP)?
8. **CPA:** Confirm the withdrawal-timing rules that attach to converted dollars before we assume this money is accessible.

*Authority citations above are from my index — text not re-verified this session (no retrieval tool available). The Part D IRMAA pin cite (42 U.S.C. §1395w-113(a)(7)) is itself flagged VERIFY.*

**On execution:** sizing and modeling are what I can do; pulling the trigger isn't. A Roth conversion is irreversible, and the withholding-versus-estimated-payment choice, in-kind versus cash, and intra-year timing all belong with your advisor and CPA.

Educational information only — not individualized investment, tax, or legal advice, and no advisory relationship is created. Figures are for the stated tax year and change; items marked VERIFY have not been confirmed against a primary source. Decide with your fiduciary advisor, CPA, or estate attorney before acting.

## Provisional executor note (NOT a verdict)

All five criterion-I checks present: IRMAA two-year lookback (63+), NIIT, WA
capital-gains excise, ACA pre-65, Social Security taxation. Each of the three
alternatives carries a one-line assumption at the decision point (relevant to
new criterion A). The WA retirement-income `VERIFY` cell surfaces as an explicit
refusal to infer. Grading is a separate session.
