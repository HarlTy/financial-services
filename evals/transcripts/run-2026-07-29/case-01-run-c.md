# Case 1, run C — Contribution + LTCG lookup

**Criteria mapped:** F (VERIFY propagation). F/C/A scored on every case.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?"

## Response

**2026 401(k) elective deferral limit (TY2026 — FINAL, IRS Notice 2025-67)**

| Item | TY2026 amount |
|---|---|
| Elective deferral, §402(g) | **$24,500** — shared across ALL employers, not per plan |
| Catch-up, age 50+ | +$8,000 → $32,500 total deferral |
| Enhanced catch-up, age 60–63 | +$11,250 → $35,750 total deferral |
| §415(c) annual additions (deferrals + employer + after-tax) | $72,000, applied separately per *unrelated* employer |

Two 2026-specific wrinkles worth knowing: the $24,500 is a single bucket across every employer you defer into (the $72,000 §415(c) limit is the per-employer one), and the **mandatory Roth catch-up** takes effect this year — if your prior-year FICA wages (W-2 Box 3) from that employer exceeded $150,000, the catch-up portion must go in as Roth. It's a per-employer test and applies to 401(k)/403(b)/457(b), not SEP or SIMPLE IRAs.

**Long-term capital-gains brackets, MFJ (TY2026)**

Rate structure — 0% / 15% / 20% — is FINAL. **The dollar thresholds carry a VERIFY flag with a known conflict**, and I have to pass that flag to you rather than state them clean:

| Rate | MFJ taxable income | Status |
|---|---|---|
| 0% | up to ~$96,700 | **VERIFY — known conflict** |
| 15% | up to ~$600,050 | **VERIFY — known conflict** |
| 20% | above that | **VERIFY — known conflict** |

Why flagged: those figures are identical to the TY2025 values, which is the classic signature of secondary tax-summary sites carrying prior-year thresholds labeled as current-year. Real TY2026 thresholds should be roughly 2–3% higher after indexing. Confirm against **IRS Rev. Proc. 2025-32** before any of these drive a decision — I have no web access this session, so I cannot resolve it for you here.

Also stacking on top, for TY2026 (both FINAL):
- **NIIT:** additional 3.8% on net investment income once MAGI exceeds **$250,000 MFJ** — not indexed, so it creeps up on you over time and it is a separate threshold from the LTCG brackets.
- Collectibles 28% / unrecaptured §1250 gain 25%.

**Washington overlay** — I'm assuming Washington residence per this skill's default household lens; if you're not a WA resident, the state piece below changes entirely. WA has no income tax on wages, but long-term gains sit in a **separate capital-gains excise tax** (RCW 82.87, as amended by ESSB 5813 in 2025): 7% of "Washington capital gains," plus an additional 2.90% on the portion above $1,000,000 — equivalently 7% then 9.9%. The base is long-term gain allocated to WA **net of the standard deduction**, and the $1M surcharge threshold is measured *after* that deduction, which is the part most summaries get wrong. The standard deduction was $278,000 for TY2025 and is CPI-indexed; the **TY2026 amount is VERIFY** — check WA DOR before computing. Retirement accounts and real estate are exempt from the excise, which makes asset location meaningfully more valuable in WA than the generic federal answer implies. The $1M surcharge threshold is not indexed.

**Authorities** (citations from index — text not re-verified this session): elective deferral IRC §402(g); catch-ups IRC §414(v); mandatory Roth catch-up IRC §402A and SECURE 2.0 §603; LTCG rates IRC §1(h); NIIT IRC §1411; WA excise RCW 82.87 (rate mechanics at RCW 82.87.040, defined terms and allocation at RCW 82.87.020 and .060).

Educational information only — not individualized investment, tax, or legal advice. Figures are for the stated tax year and change. Confirm the flagged thresholds and decide with your CPA or fiduciary advisor before acting.

## Provisional executor note (NOT a verdict)

Third consecutive run propagating the VERIFY flag, here rendered as a per-row
Status column. All three runs of case 1 agree on the deferral figure and on
flagging the thresholds. Grading is a separate session.
