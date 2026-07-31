# Case 1, run D — Contribution + LTCG lookup

**Criteria mapped:** F (VERIFY propagation). F/C/A scored on every case.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?"

## Response

**2026 401(k) elective deferral limit — $24,500** (TY2026, FINAL; IRS Notice 2025-67).

- That limit is **shared across all employers** — it's a per-person limit, not per-plan (IRC §402(g)).
- Catch-up on top: **$8,000** at age 50+ (total $32,500), or **$11,250** at ages 60–63 (total $35,750) (IRC §414(v)).
- New in 2026: if your prior-year FICA wages (W-2 Box 3) from that employer exceeded $150,000, the **catch-up must be Roth** — tested per employer, and it does not apply to SEP or SIMPLE IRAs (IRC §402A; SECURE 2.0 §603).
- Separate from the $72,000 §415(c) annual-additions limit, which applies per unrelated employer.

**Long-term capital-gains brackets, MFJ (TY2026) — rates are settled, the thresholds are not.**

The **0% / 15% / 20%** rate structure is FINAL (IRC §1(h)). The dollar thresholds carry a **VERIFY flag — known conflict**, and that flag travels with the numbers:

| Rate | MFJ taxable income (flagged) |
|---|---|
| 0% | up to ~$96,700 |
| 15% | ~$96,700 – ~$600,050 |
| 20% | above ~$600,050 |

Those figures are identical to the TY2025 values, which is the tell: the secondary sources circulating them appear to be carrying prior-year thresholds labeled as current-year. Expect the real TY2026 numbers to be roughly 2–3% higher. **Do not use them to size a gain-realization decision without confirming against IRS Rev. Proc. 2025-32.** I have no web access this session, so I could not re-check them for you.

Two things that ride alongside the bracket and are frequently missed:

- **NIIT**: an additional 3.8% on net investment income once MAGI exceeds **$250,000 MFJ** (IRC §1411). Not indexed — it creeps up on households every year, and it stacks on the 15%/20% rate rather than replacing it.
- **Washington capital-gains excise tax** — I'm assuming the default household lens here (married filing jointly, Washington resident); say the word if that's wrong, because the state answer changes completely. WA levies a separate excise on long-term gains: **7%** of "Washington capital gains," plus an additional **2.90%** on the portion above $1,000,000 — equivalently 7% then 9.9%. The base is gain net of the standard deduction ($278,000 for TY2025, CPI-indexed; **VERIFY the TY2026 amount at DOR**), and the $1M surcharge threshold is measured **after** that deduction, not on gross gain. Real estate and assets inside retirement accounts are exempt (RCW 82.87; RCW 82.87.040 as amended by ESSB 5813).

Educational information only — not individualized investment, tax, or legal advice. Figures are for the stated tax year and change; confirm the flagged ones with your CPA before they drive a decision.

Citations from this skill's index — text not re-verified this session.

## Provisional executor note (NOT a verdict)

Describes this run only. No cross-run comparison is drawn here; see the README
for why.

- VERIFY flag propagated on the LTCG thresholds, with the stale-TY2025 reason
  stated and an explicit instruction not to size a realization on them.
- Deferral limit, catch-ups, and the §415(c) figure each carry TY2026 inline
  with FINAL status.
- WA-residence assumption stated at the point the state overlay enters.
- An index-only citation label appears, its wording character-identical to the
  canonical block at `references/authorities.md`. **Position:** rendered as a
  plain line, as the final line of the response, below the educational
  disclaimer. Citations in this run are inline rather than consolidated into an
  authorities block.

Grading is a separate session.
