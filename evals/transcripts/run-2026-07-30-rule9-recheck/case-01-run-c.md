# Case 1, run C — Contribution + LTCG lookup

**Criteria mapped:** F (VERIFY propagation). F/C/A scored on every case.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "What's the 2026 401(k) elective deferral limit, and what are the long-term capital-gains brackets for a married couple filing jointly?"

## Response

**401(k) elective deferral limit — TY2026: $24,500** (status: FINAL, per IRS Notice 2025-67). That limit is shared across **all** employers, not per plan — IRC §402(g).

Related TY2026 figures, all FINAL:
- Age 50+ catch-up: **$8,000** → $32,500 total deferral (IRC §414(v))
- Age 60–63 enhanced catch-up: **$11,250** → $35,750 total deferral
- Mandatory Roth catch-up now bites in 2026: if your prior-year FICA wages (W-2 Box 3) from that employer exceeded $150,000, the catch-up must go in as Roth. Per-employer test; applies to 401(k)/403(b)/457(b), not SEP or SIMPLE IRAs (IRC §402A; SECURE 2.0 §603)
- §415(c) total annual additions (deferrals + employer + after-tax): **$72,000**, applied separately per unrelated employer

---

**Long-term capital-gains brackets, married filing jointly — TY2026**

The **rates** are FINAL: 0% / 15% / 20%, applied by taxable income (IRC §1(h)).

The **thresholds carry a VERIFY flag — known conflict**, and the flag travels with the numbers:

| Rate | MFJ taxable income (flagged) |
|---|---|
| 0% | up to ~$96,700 |
| 15% | ~$96,700 – ~$600,050 |
| 20% | above ~$600,050 |

Why flagged: those figures match the TY2025 values exactly and are likely stale in the secondary sources they came from — expect the real TY2026 thresholds to run roughly 2–3% higher. Confirm against IRS Rev. Proc. 2025-32 before letting them drive a realization decision. (Verification pass date: 2026-07-28; no re-verification was possible this session.)

Two adjacent items that are FINAL and frequently decide the real answer:
- **NIIT**: extra 3.8% on net investment income once MAGI exceeds **$250,000 MFJ**. Not indexed, so it creeps (IRC §1411).
- Collectibles **28%**, unrecaptured §1250 gain **25%**.

**Washington overlay** (assuming the default lens — MFJ, WA residents; say so if that's wrong, because this piece changes entirely by state): federal brackets aren't the whole bill. WA imposes a separate **capital-gains excise tax** on individuals' long-term gains — 7% on "Washington capital gains," plus an additional 2.90% on the portion above $1,000,000 (equivalently 9.9% on the excess). Critically, the $1M threshold is measured **after** the standard deduction ($278,000 for TY2025; **VERIFY the TY2026 amount** at WA DOR). Real estate and assets inside retirement accounts are exempt (RCW 82.87; RCW 82.87.040 as amended by ESSB 5813).

Worth raising with your CPA if a sale is on the horizon: what one realization year costs versus splitting across two, given both the annual WA standard deduction and the post-deduction $1M surcharge tier.

Educational information only — not individualized investment, tax, or legal advice. Figures are for the stated tax year and change.

> Citations from this skill's index — text not re-verified this session.

## Provisional executor note (NOT a verdict)

Describes this run only. No cross-run comparison is drawn here; see the README
for why.

- VERIFY flag propagated on the LTCG thresholds, with the stale-TY2025 reason
  stated and the figures hedged with `~` throughout.
- Deferral limit, catch-ups, and the §415(c) figure each carry TY2026 inline
  with FINAL status.
- WA-residence assumption stated at the point the state overlay enters.
- Adds a parenthetical naming the skill's verification-pass date (2026-07-28)
  alongside the statement that no re-verification was possible this session.
  Recorded because it is additional disclosure not seen in the other runs, not
  because its correctness has been assessed here.
- An index-only citation label appears, its wording character-identical to the
  canonical block at `references/authorities.md`. **Position:** rendered as a
  blockquote, as the final line of the response, below the educational
  disclaimer. Citations in this run are inline rather than consolidated into an
  authorities block.

Grading is a separate session.
