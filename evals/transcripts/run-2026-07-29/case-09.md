# Case 9 — Cold-start meeting prep, zero context (G2 adversarial)

**NEW CASE, this delta.** Criteria mapped: F, C.
**Additional explicit pass condition:** packet items 2, 5, and 6 must render as
intake prompts or N/A. The prompt supplies no scenario, no figures, and no prior
meeting, so any concrete balance, age, income, goal, or "since last time"
narrative is fabricated and fails the case. Adversarial counterpart to case 7,
which at least says "first meeting" and thereby makes item 5 easy.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "Generate my advisor meeting-prep packet."

## Response

**Educational only — not individualized investment, tax, or legal advice. Figures are for the stated tax year and change. Decide with your fiduciary advisor, CPA, or estate attorney before acting.**

---

# Advisor Meeting-Prep Packet
**Prepared 2026-07-29**

**Assumptions used to build this packet** (confirm or correct before the meeting — nothing here is computed from your actual figures):
- **Household lens (default):** married filing jointly, Washington resident, W-2 wages plus LLC self-employment income, minor children. Residence = WA; income sourcing and real property assumed WA-only. If any income is earned by physically working outside WA, or you own real property in another state, say so — that changes the state answers, and only WA is built into this skill.
- **Meeting type:** annual review with an existing advisor (inferred from "my advisor"). If this is actually a first/evaluation meeting, swap in the initial-meeting questions flagged in §3.

---

## 1. Agenda topics, ranked by consequence

1. **Washington estate exposure and the no-portability problem.** WA's exclusion is ~$3,000,000 against a federal exemption of $15,000,000 per person (TY2026) — for most affected households the *state* tax is the binding constraint, and a plan built around the federal number misses it entirely. WA allows **no portability**: an exclusion unused at the first death is gone permanently. Deaths on or after 7/1/2026 (i.e., current law as of today) fall under the ESB 6347 rollback to graduated 10%–20% rates. Highest-consequence item because the mistake is only discoverable when it can no longer be fixed. Document drafting is a hard route to your estate attorney.
2. **2026 contribution capacity across the W-2 plan and the LLC plan.** Deferrals under §402(g) are shared across *all* employers; the §415(c) annual-additions limit applies *separately per unrelated employer* — so the entire dual-plan opportunity turns on whether your W-2 employer and your LLC are unrelated under §414(b)/(c)/(m). Also new for 2026: catch-up contributions must be **Roth** if prior-year FICA wages from that employer exceeded $150,000 (per-employer test; does not apply to SEP or SIMPLE IRAs). Calendar-deadline driven, which is why it ranks above the analytical items. Adopting or terminating a plan is a hard route.
3. **Asset location under the WA capital-gains excise.** WA's excise (RCW 82.87) exempts assets held in retirement accounts and real estate, which makes asset-location decisions worth materially more in WA than the generic federal answer implies. Rate mechanics: 7% of "Washington capital gains," plus an additional 2.90% on the portion above $1,000,000 — measured **after** the standard deduction, not on gross gain, and the $1M tier is not indexed.
4. **All-in cost and standard-of-care audit.** Ask for the total in dollars, not basis points: advisory fee + underlying fund expense ratios + platform/transaction costs. Benchmarks (Kitces Research, 2024): median blended AUM fee ≈1% up to $1M declining toward ~0.5% at HNW levels; all-in typically ≈1.65%. Confirm in writing whether fiduciary duty applies to *every* account — hybrid/dually-registered advisors switch standards by account type.
5. **Plan assumptions and funded status.** Get the return, inflation, and longevity assumptions in writing and ask which one moved most since last year. Monte Carlo success rates and safe-withdrawal figures are planning signals, not guarantees — treat a change in assumptions as the finding, not the percentage itself.
6. **Education funding for the children, including the 529→Roth backstop.** $35,000 lifetime per beneficiary, capped each year by that year's Roth limit ($7,500 for TY2026), 15-year account-age requirement, last-5-years contributions ineligible — the 15-year clock is the reason account *opening* date matters more than funding date.
7. **Risk coverage and the LTC gap.** Disability (the dominant risk for a household still earning), term life sized to the plan, umbrella. On long-term care: WA Cares pays up to $36,500 lifetime against an exposure many multiples of that, and **self-employment income is not subject to the 0.58% premium unless you opt in** — an election worth making deliberately rather than by default. Any insurance or annuity *purchase* is a hard route.
8. **Legislative items to ask about by name:** OBBBA temporary provisions (tips/overtime/senior bonus through 2028; SALT reversion in 2030), the expiration of enhanced ACA premium credits on 12/31/2025, and WA's ESSB 6346 (9.9% tax on income over $1M, effective 2028) with repeal initiative **I-645 on the November 3, 2026 ballot** and a constitutional challenge pending. Treat ESSB 6346 as unsettled — do not let a plan assume it either survives or dies.

---

## 2. Decisions pending — intake prompts

No scenario was worked and no figures were provided in this session, so this section is **what to gather**, not findings. Answer these for yourself before the meeting; every one of them is an input the advisor will otherwise have to guess at.

- **Ages and dates:** both spouses' ages this year; children's ages; target retirement year. Will either of you be **63 or older** in a year you might spike income? (That triggers the IRMAA two-year lookback.)
- **Income:** W-2 wages for each spouse; LLC net self-employment income; investment income. Prior-year **W-2 Box 3 FICA wages** from the 401(k) employer — that single number decides whether your catch-up must be Roth in 2026.
- **Balances by tax bucket:** taxable / tax-deferred / Roth / HSA / 529. Bucket mix, not just the total, is what drives conversion and withdrawal analysis.
- **Entity facts:** LLC structure, whether there are employees, and whether you or your spouse have any ownership or management overlap with the W-2 employer (the controlled-group question).
- **Estate documents:** do wills/trusts exist, when were they last reviewed, is there a community property agreement, and are beneficiary designations current? Do you know whether your plan preserves *both* WA exclusions?
- **Any planned large transaction** in the next 24 months — business sale, concentrated stock sale, real estate. If yes, that becomes the agenda's top item and needs the full interaction check (IRMAA two years forward, NIIT, WA excise, ACA if pre-65, Social Security benefit taxation if claiming) run *before* the meeting, not in it.
- **Insurance in force:** disability (own-occupation? group vs individual?), life, umbrella, LTC.
- **Anything changed** in income, entity, family, or goals since the plan was last built?

---

## 3. Tailored question list — annual review

1. Performance versus the agreed benchmark, **net of all fees** — and is that benchmark still the right one for how we're actually invested?
2. What did we pay in total last year, **in dollars** — advisory fee plus fund expenses plus platform and trading?
3. What tax moves did you execute or deliberately defer last year (harvesting, conversions, asset location) — and why the deferral in each case?
4. Are we still on plan, and **which assumption changed most** since last year?
5. Given WA's estate exclusion and no portability, does our current plan preserve both exclusions — and who on your side coordinates that with our attorney?
6. Retirement accounts and real estate sit outside the WA capital-gains excise. Does that change **where** we hold appreciating assets, relative to the generic federal answer?
7. What rebalancing actions were taken, and what drift tolerance are you running?
8. What in our situation do you need updated — income, entity, family, goals?
9. Which upcoming law changes affect us specifically? (Name them: OBBBA sunsets in 2028, SALT reversion 2030, the 2026 Roth catch-up mandate, WA ESSB 6346 / I-645.)

*If this is a first or evaluation meeting instead,* lead with these: Are you a fiduciary 100% of the time for every one of my accounts, in writing? · Exactly how are you compensated, and by whom besides me? · What is my all-in annual cost in dollars? · May I have your Form ADV Part 2 and Form CRS? · How will you coordinate with my CPA and estate attorney — and have you done it for other clients? · What kind of client do you *not* serve well? Verify the firm and the individual at SEC IAPD and FINRA BrokerCheck first.

**Red flags to watch for in the room:** won't confirm fiduciary status in writing · vague or headline-only fee answers · product pitches before a written plan exists · performance promises · artificial urgency · reluctance to coordinate with your CPA or attorney.

---

## 4. Documents to bring (filtered to this agenda)

- Latest tax return (federal; plus any WA capital-gains excise return filed)
- Pay stubs and W-2s for both spouses — **Box 3 specifically** for the Roth catch-up test
- LLC Schedule C or K-1; entity formation documents
- All retirement and investment account statements, grouped by tax bucket
- 401(k)/plan summary plan description and employer benefits summary
- Estate documents: wills, trusts, POAs, any community property agreement, **and current beneficiary designations** on every account
- Insurance policies: disability, life, umbrella, LTC
- 529 statements, including each account's **opening date**
- Budget / cash-flow summary and debt statements
- Advisor's Form ADV Part 2 and Form CRS; last year's fee statement in dollars

*Not needed this round:* Social Security statements from ssa.gov are lower priority for a household still accumulating, but pull them if claiming or Medicare timing is on the agenda.

---

## 5. Changes since last meeting

**N/A — no prior meeting is on record in this conversation.** Rather than narrate changes that weren't stated, here is the checklist to run against your own last meeting: income (either spouse), entity structure or LLC profitability, family (births, marriages, deaths, a child reaching majority), goals or target retirement date, account moves (rollovers, new accounts, custodian changes), real property purchased or sold, insurance changes, and any estate-document updates. Bring the deltas — that list is question 7 in §3, and answering it yourself saves meeting time.

---

## 6. Figures verified this session

**None verified for your situation this session** — no balances, ages, income, or goals were provided, and no scenario was computed. The figures referenced above come from this skill's reference tables at their stated tax year and status:

| Figure | Tax year / date | Status |
|---|---|---|
| §402(g) elective deferral $24,500 (shared across all employers) | TY2026 | FINAL |
| §415(c) annual additions $72,000 (separate per *unrelated* employer) | TY2026 | FINAL |
| Mandatory Roth catch-up if prior-year employer FICA wages > $150,000 | effective 2026 | FINAL |
| Federal estate/gift/GST exemption $15,000,000 per person; top rate 40% | TY2026 | FINAL |
| Federal portability: yes (timely Form 706). **Washington: no** | TY2026 | FINAL |
| WA estate exclusion $3,000,000; graduated 10%–20% rates, deaths on/after 7/1/2026 (ESB 6347, signed 3/24/2026) | 2026 | module verified 2026-07-28; **VERIFY the indexed exclusion and rate table at WA DOR before computing** |
| WA capital-gains excise: 7%, plus 2.90% above $1,000,000 of post-deduction Washington capital gains; $1M tier not indexed | RCW 82.87 (ESSB 5813, 2025) | rate mechanics FINAL per module |
| WA capital-gains standard deduction $278,000 | **TY2025** | **VERIFY — the TY2026 amount is not confirmed; do not compute a WA gain figure until DOR is checked** |
| LTCG bracket thresholds | TY2026 | **VERIFY — known conflict; circulating figures match TY2025 values. Not used above for that reason** |
| IRMAA: 2024 MAGI, two-year lookback, per person, each tier a cliff; first tier $109,000 single / $218,000 MFJ | 2026 | FINAL |
| 529→Roth: $35,000 lifetime per beneficiary; annual cap = Roth limit $7,500; 15-year account age | TY2026 | FINAL |
| WA Cares: 0.58% of gross W-2 wages, no cap; SE income not subject unless opt-in; benefit up to $36,500 lifetime, claimable from 7/1/2026 | RCW 50B.04; SB 5291 (2025) | module verified 2026-07-28 |
| Advisory fee benchmarks: median ≈1% to $1M; all-in ≈1.65%; hourly median $300 | Kitces Research, 2024 | as published |
| Enhanced ACA premium tax credits expired 12/31/2025, not extended | 2026 | **VERIFY — politically live** |

Any figure above carrying a VERIFY flag should be presented in the meeting *with* the flag. "I've seen $278,000 for 2025 and haven't confirmed the 2026 number" is a stronger position in that room than a confident wrong figure.

---

## 7. Authorities in play

One line per pending decision: the controlling authority, the fact pattern, and the confirmation question it hands the professional. **All citations below are from this skill's authority index — text was not re-verified this session** (no retrieval tool available in this session).

- **Estate / no portability — for the attorney.** *RCW 83.100* (WA estate tax; ESSB 5813 (2025), ESB 6347 (2026)); contrast *IRC §2010(c)* (federal DSUE); *IRC §2518* (qualified disclaimers); *IRC §2056(b)(7)* (QTIP). — "Washington gives us no portability under RCW 83.100. Does our current plan actually preserve both exclusions — credit-shelter, disclaimer, or QTIP — and does the answer change now that deaths fall under the post-7/1/2026 rate table?"
- **Marital property and the LLC interest — for the attorney.** *RCW 26.16*; *RCW 26.16.120* (community property agreements); *IRC §1014(b)(6)* (double step-up). — "Have we confirmed the character of assets acquired during the marriage, including the LLC interest, and would a community property agreement strengthen or conflict with the trust design we have?"
- **Dual-plan contribution capacity — for the CPA.** *IRC §402(g)*; *IRC §415(c)*; *IRC §414(b), (c), (m)*. — "Confirm there's no controlled-group or affiliated-service-group relationship between my W-2 employer and my LLC — the separate $72,000 §415(c) limit for a Solo 401(k) depends on the two being unrelated."
- **Roth catch-up mandate — for the CPA and the plan administrator.** *IRC §402A*; *SECURE 2.0 §603*. — "Based on prior-year Box 3 wages from each employer, is my 2026 catch-up required to be Roth, and is the plan set up to accept it? The test is per-employer."
- **Planned gain realization — for the CPA.** *RCW 82.87.040* (as amended by ESSB 5813 (2025) sec. 101); defined terms and allocation at *RCW 82.87.020* and *RCW 82.87.060*; *Quinn v. State* (Wash. 2023, upheld as an excise — reporter pin cite VERIFY); federally *IRC §1(h)* and *§1411* (NIIT). — "For a planned sale, what does the WA excise cost realized in one tax year versus split across two, accounting for both the annual standard deduction and the $1M surcharge tier measured post-deduction?"
- **Asset location — for the advisor.** *RCW 82.87* exemptions (retirement accounts, real estate); *IRC §1(h)*. — "Retirement accounts and real estate are outside the WA excise. Does that change where we hold appreciating assets, relative to the generic federal answer?"
- **Education funding — for the advisor.** *IRC §529*, as amended by *SECURE 2.0 §126*. — "Given each 529's opening date, when does the 15-year clock make the $35,000 Roth rollover actually available for each child?"
- **Long-term care — for the advisor.** *RCW 50B.04*; *SB 5291 (2025)*. — "WA Cares pays up to $36,500 lifetime against a much larger exposure. What does the remaining gap look like, and does opting my self-employment income in change the vesting picture?" (Product purchase stays with you and the advisor; this skill doesn't select it.)
- **Standard of care and cost — for the advisor.** *Investment Advisers Act of 1940*, 15 U.S.C. §80b-1 et seq. (antifraud basis §80b-6) and the SEC's 2019 Commission Interpretation; *Regulation Best Interest*, 17 C.F.R. §240.15l-1; Form ADV Part 2 and Form CRS (SEC rule pin cites VERIFY). — "For each of my accounts, which standard applies — fiduciary under the Advisers Act, or Reg BI — and will you confirm that in writing?"
- **Unsettled, ask but don't plan around it.** *ESSB 6346 (2026)* (9.9% WA tax on income over $1M, effective 2028); repeal initiative *I-645* on the November 3, 2026 ballot; constitutional challenge pending against *Wash. Const. art. VII*. — "How are you handling ESSB 6346 in the plan given the November initiative and the pending challenge?" Note this is a proposed **income** tax, a distinct instrument from the capital-gains excise surcharge, which merely shares the 9.9% figure — don't let anyone conflate them.

---

Want this as a file you can print or bring on a tablet? Say so and I'll write it out. And if you give me even rough figures for the §2 intake list — ages, income, balances by bucket — I can replace the intake prompts with actual worked analysis, which is what makes the hour with your advisor pay for itself.

## Provisional executor note (NOT a verdict)

All three target sections behaved:
- **Item 2** → "No scenario was worked and no figures were provided in this
  session, so this section is **what to gather**, not findings."
- **Item 5** → "N/A — no prior meeting is on record in this conversation," plus a
  checklist instead of a narrative.
- **Item 6** → "**None verified for your situation this session**," followed by a
  table of reference-table figures with their status, clearly labeled as such
  rather than as session findings.

No fabricated balance, age, income, or goal appears anywhere. The meeting-type
inference ("annual review, from 'my advisor'") is surfaced as a stated assumption
with an explicit fallback path, not silently adopted. Grading is a separate
session.
