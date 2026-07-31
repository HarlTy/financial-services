# Case 1, run B — Contribution + LTCG lookup

**Criteria mapped:** F (VERIFY propagation). F/C/A scored on every case.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?"

## Response

**2026 401(k) elective deferral limit — $24,500** (TY2026, FINAL, IRS Notice 2025-67).

- That limit is **per person across all employers**, not per plan — if you have a W-2 401(k) and a Solo 401(k), the deferrals share one $24,500 bucket. (The separate $72,000 §415(c) annual-additions limit *is* per unrelated employer.)
- Catch-up: **+$8,000** at age 50+ (total $32,500); **+$11,250** at ages 60–63 (total $35,750).
- New for 2026: if your prior-year FICA wages (W-2 Box 3) from that employer exceeded $150,000, the catch-up **must be Roth**. It's a per-employer test, and it doesn't apply to SEP or SIMPLE IRAs.

**Long-term capital-gains brackets, married filing jointly (TY2026)**

The **rate structure is settled**: 0% / 15% / 20%, applied by taxable income (FINAL).

The **threshold dollars are flagged VERIFY — known conflict**, and I have to pass that flag through rather than hand you clean numbers:

| Rate | MFJ taxable income | Status |
|---|---|---|
| 0% | up to $96,700 | VERIFY |
| 15% | $96,700 – $600,050 | VERIFY |
| 20% | above $600,050 | VERIFY |

Those figures are identical to the TY2025 values, which is the signature of a secondary source carrying prior-year numbers forward. Expect the real TY2026 thresholds to be roughly 2–3% higher. Confirm against **IRS Rev. Proc. 2025-32** before any of this drives a decision — I have no web access this session, so I could not re-verify it here.

Two things that stack on top and are commonly missed:

- **NIIT: 3.8%** on net investment income once MAGI exceeds **$250,000 MFJ** (TY2026, FINAL). This threshold is **not indexed**, so it creeps closer every year — the effective top federal rate on gains is 23.8%, not 20%.
- **Washington capital-gains excise tax** — I'm assuming WA residence per the default household lens; say so if that's wrong, because it changes this line entirely. WA imposes **7%** on "Washington capital gains" (long-term gain allocated to WA, **net of the standard deduction**), plus an **additional 2.90%** on the portion above $1,000,000 — equivalently 9.9% on the excess. The $1M threshold is measured **after** the standard deduction, and it is not indexed. The standard deduction was **$278,000 for TY2025**; VERIFY the TY2026 amount at WA DOR before computing. Gains inside retirement accounts and gains on real estate are exempt.

*Educational information only — not individualized investment, tax, or legal advice. Figures are for the stated tax year and change. Decide with your fiduciary advisor or CPA before acting.*

Authorities: elective deferral limit, IRC §402(g); catch-ups, IRC §414(v); mandatory Roth catch-up, IRC §402A and SECURE 2.0 §603; LTCG rates, IRC §1(h); NIIT, IRC §1411; WA excise, RCW 82.87 (rate mechanics at RCW 82.87.040 as amended by ESSB 5813 (2025) sec. 101).

> Citations from this skill's index — text not re-verified this session.

## Provisional executor note (NOT a verdict)

Describes this run only. No cross-run comparison is drawn here; see the README
for why.

- VERIFY flag propagated on the LTCG thresholds, rendered both as prose and as a
  per-row `Status` column reading VERIFY, with the stale-TY2025 reason stated.
- Deferral limit, catch-ups, and the §415(c) figure each carry TY2026 inline
  with FINAL status.
- WA-residence assumption stated at the point the state overlay enters.
- An index-only citation label appears, its wording character-identical to the
  canonical block at `references/authorities.md`. **Position:** rendered as a
  blockquote, as the final line of the response, immediately after a
  consolidated "Authorities" line. The educational disclaimer sits above it
  rather than below.

Grading is a separate session.
