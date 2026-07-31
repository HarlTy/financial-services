# Case 1, run E — Contribution + LTCG lookup

**Criteria mapped:** F (VERIFY propagation). F/C/A scored on every case.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?"

## Response

**2026 401(k) elective deferral limit — TY2026, FINAL** (IRS Notice 2025-67)

- **Elective deferral (§402(g)): $24,500** — shared across ALL employers, not per plan.
- Catch-up, age 50+: **$8,000** → $32,500 total deferral.
- Enhanced catch-up, ages 60–63: **$11,250** → $35,750 total deferral.
- New for 2026: if your prior-year FICA wages (W-2 Box 3) from that employer exceeded $150,000, the **catch-up must be Roth**. Per-employer test; applies to 401(k)/403(b)/457(b), not SEP or SIMPLE IRAs.
- Separate from the §415(c) annual-additions limit of **$72,000**, which applies per unrelated employer.

**Long-term capital-gains brackets, MFJ — TY2026, VERIFY (known conflict)**

The rate structure is 0% / 15% / 20% by taxable income (FINAL). The **thresholds carry an unresolved verification flag**, and it travels with the figures:

| Rate | MFJ taxable income (flagged) |
|---|---|
| 0% | up to ~$96,700 |
| 15% | ~$96,700 – ~$600,050 |
| 20% | above ~$600,050 |

Those numbers **match the TY2025 values exactly** and are likely stale in the secondary sources this skill drew from — expect the true TY2026 figures to run roughly 2–3% higher. Do not use them to size a gain realization without confirming against IRS Rev. Proc. 2025-32. This session has no web access, so I could not re-verify them for you; that confirmation is a one-page check your CPA can do in a minute, or you can pull the Rev. Proc. from irs.gov directly.

Two related TY2026 figures that are FINAL: **NIIT** is 3.8% on net investment income above MAGI $250,000 MFJ (not indexed), and collectibles / unrecaptured §1250 gain run 28% / 25%.

**Washington overlay** (assuming the default lens — married filing jointly, Washington resident; tell me if that's wrong)

Washington has no income tax, so the federal LTCG brackets are the whole income-tax story — but a **separate capital-gains excise tax** applies to long-term gains and is easy to miss:

- **7%** of "Washington capital gains," plus an additional **2.90%** on the portion above **$1,000,000** (i.e., 9.9% on the excess). RCW 82.87.040 as amended by ESSB 5813 (2025).
- Critically, "Washington capital gains" is gain **net of the standard deduction**, and the $1M surcharge threshold is measured on that **post-deduction** figure. Standard deduction was **$278,000 for TY2025**, CPI-indexed — **VERIFY the TY2026 amount** at WA DOR before computing anything. The $1M threshold is not indexed.
- **Exempt:** real estate, assets inside retirement accounts, timber, livestock/agricultural assets, commercial fishing privileges. The retirement-account and real-estate carve-outs make asset location worth more in WA than the generic federal answer suggests.

If you're contemplating an actual large realization rather than just looking up the numbers, the checks that most often break an otherwise-correct analysis are: IRMAA two years forward (if either of you will be 63+ in the spike year), NIIT, the WA excise above, ACA marketplace premiums if pre-65, and Social Security benefit taxation if claiming. Happy to run that.

**Authorities in play:** elective deferral limit — IRC §402(g); catch-ups — IRC §414(v); mandatory Roth catch-up — IRC §402A and SECURE 2.0 §603; annual additions — IRC §415(c); LTCG rates — IRC §1(h); NIIT — IRC §1411; WA excise — RCW 82.87, rate mechanics at RCW 82.87.040.

> Citations from this skill's index — text not re-verified this session.

Educational information only — not individualized investment, tax, or legal advice. Figures are for the stated tax year and change.

## Provisional executor note (NOT a verdict)

Describes this run only. No cross-run comparison is drawn here; see the README
for why.

- VERIFY flag propagated on the LTCG thresholds — carried into the section
  heading itself ("TY2026, VERIFY (known conflict)") as well as the prose — with
  the stale-TY2025 reason stated.
- Deferral limit, catch-ups, and the §415(c) figure each carry TY2026 inline
  with FINAL status.
- WA-residence assumption stated at the point the state overlay enters.
- Volunteers the rule-3 interaction-check list (IRMAA 63+, NIIT, WA excise, ACA
  pre-65, Social Security taxation) and offers to run it, although the prompt
  describes no income-spike scenario. Recorded as a factual difference from the
  other runs, not assessed here.
- An index-only citation label appears, its wording character-identical to the
  canonical block at `references/authorities.md`. **Position:** rendered as a
  blockquote following a consolidated "Authorities in play" line, and preceding
  the closing educational disclaimer — it is not the final line of the response.

Grading is a separate session.
