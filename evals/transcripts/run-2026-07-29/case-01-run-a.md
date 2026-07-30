# Case 1, run A — Contribution + LTCG lookup

**Criteria mapped:** F (VERIFY propagation). F/C/A scored on every case.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?"

## Response

**401(k) elective deferral limit — TY2026: $24,500** (IRC §402(g); IRS Notice 2025-67). Status: FINAL.

- That $24,500 is a **per-person limit shared across all employers**, not per plan.
- Age 50+ catch-up: **+$8,000** → $32,500 total deferral. Ages 60–63 enhanced catch-up: **+$11,250** → $35,750. Both FINAL.
- New for 2026: if your prior-year FICA wages (W-2 Box 3) from that employer exceeded $150,000, your **catch-up must go in as Roth**. It's a per-employer test, applies to 401(k)/403(b)/457(b), and does not apply to SEP or SIMPLE IRAs.
- Separate limit worth knowing if employer or after-tax contributions are in play: §415(c) annual additions cap is **$72,000** for 2026, and that one applies separately per unrelated employer.

**Long-term capital-gains brackets, MFJ — TY2026: rates are settled, the thresholds are not.**

The **rate structure is 0% / 15% / 20%** (FINAL), plus 25% on unrecaptured §1250 gain and 28% on collectibles (FINAL).

The **dollar thresholds carry a VERIFY flag with a known conflict**, and the flag has to travel with the numbers: the figures circulating in secondary sources (0% up to $96,700 MFJ; 15% up to $600,050 MFJ) are **identical to the TY2025 values**, which is the signature of stale data — TY2026 thresholds should be roughly 2–3% higher. Do not use those numbers for a decision until they're confirmed against **IRS Rev. Proc. 2025-32**. I don't have web access in this session, so I can't re-verify them for you here; treat them as a placeholder range, not a figure.

Two things that ride along with MFJ gains and are FINAL:

- **NIIT:** additional 3.8% on net investment income once MAGI exceeds **$250,000 MFJ**. Not indexed, so it creeps.
- **WA capital-gains excise tax** — flagging this because my default assumption is that you're a Washington resident (say the word if that's wrong, since it changes this section entirely and nothing else in the answer): WA imposes 7% on "Washington capital gains," plus an additional 2.90% on the portion above $1,000,000 (RCW 82.87.040, as amended by ESSB 5813). The base is long-term gain allocated to WA **net of the standard deduction**, and the $1M surcharge threshold is measured **after** that deduction. The standard deduction was $278,000 for TY2025 and is CPI-indexed — **the TY2026 amount is VERIFY**; confirm at WA DOR before computing anything. Retirement accounts and real estate are outside this tax, which makes asset location worth more in WA than the generic federal answer suggests.

**Worth raising with your CPA:** which Rev. Proc. 2025-32 threshold applies to your projected 2026 taxable income before you time any realization, and — for a planned sale — what the WA excise costs realized in one tax year versus split across two, accounting for both the annual standard deduction and the post-deduction $1M tier.

Educational information only, not individualized investment, tax, or legal advice. Figures are for the stated tax year and change.

## Provisional executor note (NOT a verdict)

VERIFY flag propagated on the LTCG thresholds with the stale-TY2025 reason stated.
Deferral limit given with tax year and FINAL status. State assumption surfaced
explicitly rather than silently applied. Grading is a separate session.
