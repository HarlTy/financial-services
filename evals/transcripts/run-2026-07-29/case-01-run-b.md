# Case 1, run B — Contribution + LTCG lookup

**Criteria mapped:** F (VERIFY propagation). F/C/A scored on every case.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?"

## Response

## 2026 401(k) elective deferral limit — TY2026, FINAL

**$24,500** (IRC §402(g)) — and that limit is shared across **all** employers, not per plan.

| Add-on | TY2026 | Total deferral |
|---|---|---|
| Catch-up, age 50+ | $8,000 | $32,500 |
| Enhanced catch-up, age 60–63 | $11,250 | $35,750 |

Two 2026-specific items worth knowing alongside it:
- **Mandatory Roth catch-up is now live (2026).** If your prior-year FICA wages (W-2 Box 3) from that employer exceeded $150,000, the catch-up must go in as Roth. Per-employer test; applies to 401(k)/403(b)/457(b), not SEP or SIMPLE IRAs. (IRC §402A; SECURE 2.0 §603)
- The separate **§415(c)** annual-additions limit is **$72,000** for TY2026 and applies per *unrelated* employer — that is the limit that governs employer contributions and after-tax/mega-backdoor room, not §402(g).

## Long-term capital-gains brackets, MFJ — rates FINAL, thresholds VERIFY

**Rates: 0% / 15% / 20%** (IRC §1(h)) — FINAL for TY2026.

**Thresholds carry an open VERIFY flag, and I have to pass it to you rather than answer cleanly.** The MFJ figures in my reference tables are 0% up to $96,700 and 15% up to $600,050 (20% above), but those are flagged as a **known conflict**: they match the TY2025 values exactly, which is the signature of secondary sources carrying prior-year numbers as current. TY2026 thresholds should be roughly 2–3% higher. Do not use those two numbers for a decision without confirming them against **IRS Rev. Proc. 2025-32** — and I can't confirm them in this session, so they remain unverified as of my last verification date of 2026-07-28.

The single-filer figures ($48,350 / $533,400) carry the same flag for the same reason.

**Also in the MFJ capital-gains stack:**
- **NIIT: 3.8%** on net investment income once MAGI exceeds **$250,000 MFJ** — FINAL, and **not indexed**, so this threshold does not move with inflation the way the LTCG brackets do. It is a separate overlay on top of the 15%/20% rate, not a fourth bracket.
- Collectibles 28% / unrecaptured §1250 gain 25% — FINAL.

## State overlay — Washington (assumed)

I'm assuming a Washington-resident household per this skill's default lens; if you're in another state, the state answer below changes entirely and you should say so, because capital gains is exactly the topic where the state layer moves the number most.

WA has no income tax on wages, but it does levy a **capital-gains excise tax** (RCW 82.87), which sits on top of the federal brackets above:
- **7%** of "Washington capital gains," plus an **additional 2.90%** on the portion above **$1,000,000** — the commonly quoted "7% / 9.9%" phrasing is arithmetically identical.
- The base is long-term gain allocated to WA **net of the standard deduction**, and the **$1M surcharge threshold is measured after that deduction**, not on gross gain. The threshold is not indexed.
- Standard deduction was **$278,000 for TY2025** and is CPI-indexed — **the TY2026 amount is a VERIFY**; confirm at WA DOR before computing anything.
- **Gains inside retirement accounts and gains on real estate are exempt** — which is why asset-location decisions carry more weight in WA than the generic federal answer implies.

Note that WA amended both its capital-gains and estate statutes within the last 13 months, so any WA figure driving a decision deserves a fresh DOR check.

Authority citations above are from this skill's index — statutory text was not re-verified this session (no retrieval tool available).

Two things worth putting to your CPA: (1) confirm the TY2026 LTCG threshold and WA standard-deduction figures against Rev. Proc. 2025-32 and the DOR table before you size any gain realization, and (2) if you have both W-2 and self-employment income, confirm there's no §414(b)/(c)/(m) controlled-group relationship between the employer and your LLC — the separate $72,000 §415(c) limit depends on the two being unrelated.

Educational information only — not individualized investment, tax, or legal advice. Figures are for the stated tax year and change; decide with your fiduciary advisor or CPA before acting.

## Provisional executor note (NOT a verdict)

Same VERIFY propagation as run A, plus the index-only citation label ("text was
not re-verified this session"). Grading is a separate session.
