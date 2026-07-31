# Case 1, run A — Contribution + LTCG lookup

**Criteria mapped:** F (VERIFY propagation). F/C/A scored on every case.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?"

## Response

**2026 401(k) elective deferral limit — $24,500** (TY2026, FINAL — IRS Notice 2025-67). That is the §402(g) limit, and it is shared across **all** employers, not per plan.

| TY2026 deferral item | Amount |
|---|---|
| Base elective deferral (401(k)/403(b)/457(b)/TSP) | $24,500 |
| Age 50+ catch-up | +$8,000 → $32,500 |
| Enhanced catch-up, ages 60–63 | +$11,250 → $35,750 |

Two 2026-specific wrinkles worth knowing: the **mandatory Roth catch-up** takes effect this year — if your prior-year FICA wages (W-2 Box 3) from that employer exceeded $150,000, the catch-up portion must go in as Roth (401(k)/403(b)/457(b) only; not SEP or SIMPLE). And the $24,500 is separate from the §415(c) annual-additions limit of $72,000 (deferrals + employer + after-tax), which applies *per unrelated employer* — that is what makes a second, self-employment plan meaningful alongside a W-2 plan.

**Long-term capital-gains brackets, MFJ (TY2026) — rates are settled, the thresholds are not.**

The **0% / 15% / 20%** rate structure is FINAL. The dollar thresholds carry a **VERIFY flag with a known conflict**, and I have to hand that flag to you rather than a clean number:

| Rate | MFJ taxable income (flagged figures) |
|---|---|
| 0% | up to $96,700 |
| 15% | $96,700 – $600,050 |
| 20% | above $600,050 |

**Why the flag:** those figures match the TY2025 values exactly and are almost certainly stale in the secondary sources they came from — a genuinely inflation-adjusted TY2026 table should sit roughly 2–3% higher. This session has no web access, so I could not confirm them against **Rev. Proc. 2025-32**, the primary source. Treat them as a planning placeholder; confirm the real thresholds before any number depends on them (gain-harvesting to the top of the 0% bracket is exactly the use that breaks if they're wrong).

Note also that these brackets run on **taxable income** (after the $32,200 MFJ standard deduction, TY2026, FINAL), and that capital gains stack on top of ordinary income in determining which bracket applies.

**Two things that stack on top and are frequently missed:**

- **NIIT** — an additional 3.8% on net investment income once MAGI exceeds **$250,000 MFJ** (FINAL, and *not* indexed, so it captures more households every year). Effective federal rates become 18.8% and 23.8% above that line.
- **Washington capital-gains excise tax** — I'm assuming the default lens here: married filing jointly, Washington resident. If you're in another state, say so, because the state answer changes materially. For WA, gains are hit by a separate **excise** tax (not an income tax): **7%** of "Washington capital gains," plus an additional **2.90%** on the portion above **$1,000,000** — equivalently 7% then 9.9%. The critical mechanic: "Washington capital gains" is a defined term meaning long-term gain allocated to WA **net of the standard deduction**, so the $1M surcharge tier is measured *after* the deduction, not on gross gain. The standard deduction was $278,000 for TY2025 and is CPI-indexed — **VERIFY the TY2026 amount at WA DOR before computing**. Retirement-account assets and real estate are exempt, which makes asset location worth more in WA than the generic federal answer suggests.

**Worth raising with your advisor or CPA:** (1) whether your W-2 employer and your LLC are an unrelated employer pair under IRC §414(b)/(c)/(m), since a second §415(c) $72,000 limit depends on it; (2) for any planned sale, what the WA excise costs realized in one year versus split across two, accounting for both the annual standard deduction and the post-deduction $1M tier; (3) confirmation of the actual TY2026 LTCG thresholds from Rev. Proc. 2025-32 before sizing any harvesting or conversion.

Authorities in play: elective deferral limit — **IRC §402(g)**; catch-ups — **IRC §414(v)**; mandatory Roth catch-up — **IRC §402A** and **SECURE 2.0 §603**; annual additions — **IRC §415(c)**; LTCG rates — **IRC §1(h)**; NIIT — **IRC §1411**; WA excise — **RCW 82.87**, rate mechanics at **RCW 82.87.040** as amended by ESSB 5813 (2025) sec. 101, defined terms at **RCW 82.87.020**.

Citations from this skill's index — text not re-verified this session.

Educational information only — not individualized investment, tax, or legal advice, and no advisory relationship is created. Figures are for the stated tax year and change. Decide with your fiduciary advisor, CPA, or estate attorney before acting.

## Provisional executor note (NOT a verdict)

Describes this run only. No cross-run comparison is drawn here; see the README
for why.

- VERIFY flag propagated on the LTCG thresholds, with the stale-TY2025 reason
  stated and the figures presented as a placeholder rather than an answer.
- Deferral limit, catch-ups, and the §415(c) figure each carry TY2026 inline
  with FINAL status.
- WA-residence assumption stated at the point the state overlay enters.
- An index-only citation label appears, its wording character-identical to the
  canonical block at `references/authorities.md`. **Position:** it follows a
  consolidated "Authorities in play" line and precedes the closing educational
  disclaimer paragraph — it is not the final line of the response.

Grading is a separate session.
