# Case 3 — WA estate statute + portability

**Criteria mapped:** F, S, C. Designated rule-9 trigger: a response that does not
name `RCW 83.100` fails on C alone.
**Run conditions:** see [README.md](README.md). No web retrieval.

## Prompt

> "Which statute governs Washington's estate tax, and does Washington allow portability between spouses the way the federal exemption does?"

## Response

## The statute

**RCW 83.100** — Washington's Estate and Transfer Tax Act — is the controlling authority, as amended by **ESSB 5813 (2025)** and **ESB 6347 (2026)**. Implementing rules sit at **WAC 458-57** (chapter number carries a VERIFY flag), and the Department of Revenue administers it. *Citations from index — text not re-verified this session (no web access here); pull current RCW text at app.leg.wa.gov/rcw before relying on it in a document.*

## Portability: no

**Washington allows no portability between spouses.** An exclusion unused at the first death is simply lost — there is no Washington analogue to the federal deceased spousal unused exclusion (DSUE) election under **IRC §2010(c)**, which lets a surviving spouse pick up the first spouse's unused federal exemption via a timely Form 706. Federal: yes. Washington: no.

That asymmetry is the single most consequential difference for a married Washington household, because the exclusion amounts are two orders of magnitude apart:

| | Exclusion | Top rate |
|---|---|---|
| Federal (TY2026) | $15,000,000 per person / $30M per couple, indexed after 2026 — FINAL | 40% |
| WA, deaths 7/1/2025 – 6/30/2026 | $3,000,000, CPI-indexed (≈$3,076,000 for early-2026 deaths — **VERIFY** against the DOR table) | 35% above $9M |
| WA, deaths on/after 7/1/2026 | $3,000,000, Seattle-area CPI indexed | graduated 10%–20% |

So for most affected Washington households the **state** tax is the binding constraint, and it is the one with no spousal carryover. A plan built around the $15M federal number can leave the WA exposure entirely unaddressed — a closely held business interest pushes an estate past $3M quickly.

## What fills the gap instead

Because there is no portability, both exclusions have to be preserved structurally rather than by election. The standard mechanisms:

- **Credit-shelter / bypass trust** funded at the first death up to the WA exclusion
- **Disclaimer trust** for post-mortem flexibility — IRC §2518
- **QTIP election planning** — IRC §2056(b)(7), with inclusion at IRC §2044

Washington's community property regime is a separate advantage that is easy to conflate with this one: both halves of community property get a full basis step-up at the first death (**IRC §1014(b)(6)**, the "double step-up"). That is an income-tax benefit; it does nothing to preserve the estate exclusion. Community property agreements under **RCW 26.16.120** can also interact with a credit-shelter design rather than sit alongside it neatly.

Drafting any of these is a hard route to your estate attorney — the analysis above is the input to that conversation, not a substitute for it.

## Worth raising with the attorney

1. Washington gives us no portability under RCW 83.100. Does our current plan actually preserve both exclusions — credit-shelter, §2518 disclaimer, or QTIP — and does the answer change depending on whether the first death falls before or after 7/1/2026?
2. Would a community property agreement under RCW 26.16.120 strengthen or conflict with the trust design we have, given we want to keep the §1014(b)(6) double step-up?
3. Given the $3M WA exclusion versus the $15M federal one, is lifetime gifting sized to the state constraint rather than the federal one — and how does the closely held business interest get valued for that?

Two flags on the figures: the WA exclusion's 2026 indexation carries a VERIFY, and WA's capital-gains and estate statutes both changed within the last 13 months, so re-verify the DOR exclusion and rate tables in any session where they drive a number. Whether Washington imposes any separate *inheritance* tax on beneficiaries (as distinct from the estate-level tax above) has not been researched against a primary source in this skill — I can't report "none."

Educational information only — not individualized legal or tax advice. Figures are for the tax years stated and change. Decide with your estate attorney and CPA before acting.

## Provisional executor note (NOT a verdict)

RCW 83.100 named; no-portability stated affirmatively with the federal §2010(c)
contrast. Notable new behavior: the response volunteers that the *inheritance*
tax question is unresearched and declines to report "none" — the `VERIFY` cell
from `_index.md` surfacing in an answer rather than being silently filled.
Grading is a separate session.
