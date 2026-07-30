# Case 5 — W-2 401(k) + LLC Solo 401(k) stacking

**Criteria mapped:** F, X, C. Must surface `IRC 414(b)/(c)/(m)` unprompted.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "I have a W-2 job with a 401(k) and I also run an LLC on the side. Can I open a Solo 401(k) and get a second $72,000 limit?"

## Response

## Short answer

Yes and no. You do get a **second $72,000 ceiling** — but not a second $24,500. The elective-deferral limit follows *you*; the annual-additions limit follows *each employer*. So the LLC-side $72,000 has to be filled almost entirely with **employer (profit-sharing) money**, which is a function of your LLC profit — not something you can simply elect.

Assumptions I'm running on (say if any is wrong): married filing jointly, Washington resident, W-2 wages plus single-member LLC self-employment income, and the LLC is a sole proprietorship / disregarded entity for tax purposes.

## The two limits (TY2026, IRS Notice 2025-67)

| Limit | TY2026 amount | Scope | Status |
|---|---|---|---|
| Elective deferral, §402(g) | $24,500 | **Per person, across ALL 401(k) plans combined** | FINAL |
| Catch-up 50+ / 60–63, §414(v) | $8,000 / $11,250 | Per person | FINAL |
| DC annual additions, §415(c) | $72,000 | **Separately per unrelated employer** | FINAL |
| Compensation cap, §401(a)(17) | $360,000 | Per plan | FINAL |

So: max out deferrals in your W-2 plan, and you can *still* receive employer contributions into a Solo 401(k) on the LLC income under its own separate $72,000 ceiling. What you cannot do is defer $24,500 twice.

## What actually fills the LLC-side $72,000

Three sources, in practice:

1. **Employer profit-sharing contribution** — the real workhorse. For a sole proprietor / single-member LLC this is **≈20% of net self-employment earnings**, not 25% of Schedule C profit. The statute says 25% of compensation, but "compensation" is computed after reducing income by half of SE tax *and* by the contribution itself, which collapses to roughly 20%. Never apply 25% straight to Schedule C net profit.
2. **Any unused deferral room** — if you don't max the $24,500 at the W-2 job, the remainder can go into the Solo 401(k) instead. It's one shared bucket, allocated between plans however you like.
3. **After-tax contributions (mega-backdoor)** — only if the plan document permits after-tax contributions plus in-plan Roth conversion. Many low-cost Solo 401(k) documents do not.

### Worked example — $100,000 of Schedule C net profit

Assumption: your W-2 wages are below the TY2026 OASDI wage base of $184,500, so the full 15.3% SE rate applies to the SE base. If your W-2 wages already exceed that base, only the 2.9% Medicare portion applies to the LLC income and the contribution comes out slightly higher.

- SE tax base: $100,000 × 92.35% = $92,350
- SE tax at 15.3% = $14,130; half = **$7,065**
- Net SE earnings: $100,000 − $7,065 = **$92,935**
- Employer contribution: 20% × $92,935 = **$18,587**

**Cross-foot, each leg stated:**
- Deferrals across all employers: $24,500 (W-2 plan) + $0 (Solo) = $24,500 ≤ $24,500 ✓
- W-2 employer annual additions: $24,500 + whatever your employer match/profit-sharing adds ≤ $72,000 ✓ (check your match against this)
- LLC annual additions: $0 deferrals + $18,587 employer = $18,587 ≤ $72,000 ✓
- Employer contribution ≤ deduction limit on net SE earnings: $18,587 = $18,587 ✓

**The reality check:** filling the LLC-side $72,000 from the employer leg alone takes roughly **$360,000 of net self-employment earnings** (20% × $360,000 = $72,000). At $100,000 of profit you get about a quarter of it. The second ceiling is real; the second *$72,000* is not, unless the side business is large.

## The load-bearing condition — do not skip this

The separate per-employer $72,000 holds **only if your W-2 employer and your LLC are genuinely unrelated**. Common ownership, or an affiliated-service-group arrangement (classically: you consult back to your own employer, or into the same professional service line), collapses the two into a **single** $415(c) limit under IRC §414(b), (c), (m) — and an excess contribution becomes a correction problem, not a rounding error. This is the assumption the entire strategy rests on, and it's a CPA confirmation item, not a self-assessment.

## Four other things that bite

- **Mandatory Roth catch-up (new for 2026).** If you're 50+, catch-up must be Roth where prior-year W-2 Box 3 FICA wages *from that employer* exceeded $150,000. It's a **per-employer test**, so the answer can differ between your W-2 plan and your Solo 401(k). Confirm how your specific plan document applies the test — I'm not going to reason the sole-proprietor case out for you from first principles.
- **Form 5500-EZ** becomes an annual filing once Solo 401(k) plan assets exceed $250,000.
- **Solo 401(k) vs SEP-IRA.** For your household shape, Solo 401(k) generally dominates: same $72,000 employer ceiling, plus Roth and mega-backdoor optionality, and no SEP balance to contaminate backdoor-Roth pro-rata math.
- **Establishment and funding deadlines** for a Solo 401(k) are not in this skill's reference tables, so I won't state them. Ask the provider and your CPA — the deadline is the thing that most often kills a first-year plan.

## Interactions worth checking

- **QBI (§199A) coupling.** If the LLC is consulting, it's an SSTB. Retirement contributions reduce taxable income, which can pull you back inside — or through — the SSTB phase-out band ($150,000 MFJ range, TY2026). The plan contribution and the QBI deduction have to be optimized *jointly*, not sequentially. **VERIFY** the current-year §199A taxable-income threshold before anyone computes a dollar figure; it isn't confirmed in these tables.
- Traditional vs Roth on the deferral leg is a bracket call, not a limits call — the $24,500 is the same either way.
- The usual income-spike checks (IRMAA two-year lookback, NIIT, WA capital-gains excise, ACA) aren't triggered here: this lowers taxable income rather than spiking it.

## Washington notes

- **LLC self-employment income is not subject to WA Cares** (0.58% of gross W-2 wages, no cap) unless you opt in. Your W-2 wages are.
- WA has **no income tax on wages**, so there's no state-side deduction value to model on the contribution.
- Separately: an LLC interest acquired during marriage is presumptively community property, and WA's ~$3,000,000 estate exclusion with **no portability** means a growing business interest crosses the state threshold long before the federal $15,000,000 one. Not today's question, but it's the thing this LLC will eventually create.

## Take to your advisor

**Decision pending:** whether to adopt a Solo 401(k) for the LLC, and with what plan document features. Plan adoption is a decision for your CPA and the plan provider — I can size it, not execute it.

**Inputs used here:** TY2026 limits per IRS Notice 2025-67 ($24,500 / $72,000 / $360,000); Schedule C net profit of $100,000 illustrative; sole-proprietor 20%-of-net-SE-earnings employer computation; MFJ, WA resident.

**Questions that resolve it:**
1. *For the CPA:* "Confirm there's no §414(b)/(c)/(m) controlled-group or affiliated-service-group relationship between my W-2 employer and my LLC — the separate $72,000 §415(c) limit depends on the two being unrelated."
2. *For the CPA:* "At our income, where do we sit in the §199A SSTB phase-out, and how does the size of the Solo 401(k) employer contribution move that answer?"
3. *For the CPA/provider:* "Given my exact Schedule C profit and W-2 wages relative to the $184,500 OASDI base, what's the precise deductible employer contribution — and what's the establishment and funding deadline for this tax year?"
4. *For the provider:* "Does the plan document allow after-tax contributions plus in-plan Roth conversion, and how does it apply the 2026 Roth catch-up test to a self-employed participant?"

Authorities in play (citations from index — text not re-verified this session): IRC §402(g) deferral limit; §415(c) annual additions; §414(v) catch-up; §402A and SECURE 2.0 §603 Roth catch-up; §414(b), (c), (m) controlled and affiliated service groups; §401(a)(17) compensation cap; §199A QBI/SSTB; §1401 SE tax; RCW 50B.04 WA Cares.

Educational information only — not individualized investment, tax, or legal advice. Figures are TY2026 and change; decide with your CPA and fiduciary advisor before acting.

## Provisional executor note (NOT a verdict)

`IRC §414(b), (c), (m)` surfaced unprompted and framed as the load-bearing
condition. Cross-foot shown leg by leg (402(g) shared, 415(c) per employer, both
directions reconciled). Grading is a separate session.
