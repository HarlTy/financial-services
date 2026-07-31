# State Index — resolution table and unbuilt-state flags

Last verified: 2026-07-29.

This is a **routing table, not a source of answers.** It exists so that state
resolution can (1) find the module for a resolved state, and (2) tell the user
what is missing when no module exists. Every substantive answer comes from the
module itself; a cell here is a pointer or a gap marker, never a citation.

## How to read it

- **`VERIFY`** — not researched against a primary source. It does **not** mean
  "no" or "none." An unbuilt state's row is `VERIFY` across the board because
  nothing has been checked, and a *built* state can still carry `VERIFY` in a
  cell its module does not address.
- **`UNBUILT`** — no module exists. Answer the federal layer, then emit the
  canonical fallback from `../guardrails.md`.
- **Flag lines.** Per SKILL.md rule 4, a cell marked `Yes` for an unbuilt state
  contributes one flag line to the fallback. `VERIFY` cells contribute nothing —
  a flag asserts a fact, and an unresearched cell has none to assert. Today no
  unbuilt state has a `Yes` cell, so the mechanism is dormant by construction and
  activates only as states are researched.
- **Rows refresh only when researched.** A row is never filled speculatively or
  from general knowledge, including for states whose treatment is widely known.
  Guessing right is indistinguishable from guessing wrong at the point of use.
- **Module paths** are relative to this file's directory
  (`references/states/`); the loader path is `references/states/<file>`.

| code | income tax | taxes retirement income | estate tax | inheritance tax | community property | local income taxes | LTC/auto-IRA program | module | last verified |
|---|---|---|---|---|---|---|---|---|---|
| AL | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| AK | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| AZ | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| AR | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| CA | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| CO | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| CT | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| DE | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| DC | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| FL | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| GA | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| HI | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| ID | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| IL | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| IN | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| IA | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| KS | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| KY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| LA | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| ME | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| MD | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| MA | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| MI | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| MN | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| MS | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| MO | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| MT | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| NE | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| NV | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| NH | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| NJ | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| NM | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| NY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| NC | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| ND | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| OH | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| OK | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| OR | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | in progress (Phase 1) | never |
| PA | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| RI | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| SC | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| SD | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| TN | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| TX | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| UT | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| VT | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| VA | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| WA | No — wages [1] | VERIFY [2] | Yes [3] | VERIFY [4] | Yes [5] | VERIFY [6] | LTC: Yes [7] · auto-IRA: VERIFY | `washington.md` | 2026-07-28 |
| WV | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| WI | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |
| WY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | VERIFY | UNBUILT | never |

51 rows: 50 states plus DC. One module built (WA), one in progress (OR), 49
`UNBUILT`.

## WA cell basis

Every WA cell is sourced to a named section of `washington.md` — the module, not
general knowledge. Where that file is silent the cell is `VERIFY`, which is why a
built state still shows four of them.

1. **No — wages.** Intro: "Washington has no state income tax on wages." The
   capital-gains levy is a separate **excise** tax (§1), not an income tax.
2. **VERIFY.** The module states no income tax *on wages* and exempts
   retirement-account assets from the capital-gains excise, but does not address
   how retirement *income* is treated. Concluding "not taxed" requires knowing no
   other income tax exists, which the module does not establish. Left unflagged
   until researched.
3. **Yes.** §2 — RCW 83.100, split-year 2026. Note there is **no portability
   between spouses**, which the module treats as the load-bearing fact.
4. **VERIFY.** The module does not mention an inheritance tax. Silence is not a
   "no."
5. **Yes.** §3 — community property, with full basis step-up on both halves at
   the first death.
6. **VERIFY.** The module does not address county, city, or transit-district
   income taxes. Per the sub-state layer convention in `_template.md`, an omitted
   section means "not looked," not "none."
7. **LTC: Yes.** §4 — WA Cares / LTSS Trust, RCW 50B.04. The module covers only
   the LTC program; it says nothing about a state-facilitated auto-IRA, so that
   half of the cell is `VERIFY`.

Pending, and deliberately not reflected in the WA row: ESSB 6346 would impose a
9.9% tax on income over $1M effective 2028, with a repeal initiative (I-645) on
the November 3, 2026 ballot and a constitutional challenge pending. The module
records it as unsettled; the row states current law.
