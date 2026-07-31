# [State] State Module — authoring template

**This file is a template, not a module.** It is never loaded to answer a
question, and it contains no state facts. Copy it to states/xx.md (two-letter
lowercase code), then fill every section in the order below.

The order is fixed on purpose: a reader who knows one module knows them all, and
a refresh can diff two modules structurally instead of reading both end to end.
Keep every heading even when a section is empty — write "None" or the applicable
`VERIFY` marker rather than deleting the heading, so a missing section always
means "not yet authored" and never "not applicable."

Last verified: (date of the most recent primary-source check on this file)
Sources: (every primary source consulted, named specifically enough to re-retrieve)

## Conventions a module inherits

**VERIFY.** Any figure or rule not confirmed against a primary source this
refresh carries a `VERIFY` marker inline, and the marker travels with the figure
into any answer that uses it. An unmarked figure asserts that it *was* verified.

Silence is not a flag. If a module does not address a topic, that state's
corresponding cell in `_index.md` stays `VERIFY` — it is never inferred from the
module's other contents. A module that discusses long-term-care insurance but
never mentions an auto-IRA program has said nothing about auto-IRA programs.

**Planned references.** A path written in backticks or markdown-link syntax must
resolve now; `scripts/check.py` enforces this. A path naming a file that does not
exist yet is written in plain prose instead — no backticks, no brackets — as in
mirror: states/oregon.md (Phase 1). Forward references to unbuilt modules stay
legible without breaking the link gate.

**Resolution base.** Backticked paths resolve relative to the file they appear
in, not to the skill root. From inside this directory the federal authority map
is `../authorities.md` and a sibling module is `washington.md`. The two natural
mistakes are writing references/authorities.md (correct only from SKILL.md) or
states/washington.md (correct only from the references/ root) — both shown here
in plain prose deliberately, since backticking a path asks the gate to resolve it
and these are examples of what *not* to write. This is the most common authoring
error the link gate catches.

## 1. Income tax

Wage income, investment income, and retirement income each stated separately —
a state can tax one and exempt another, and "no income tax" is not a safe
shorthand for any of the three. Include: rate structure or its absence; whether
brackets and any standard deduction are inflation-indexed; treatment of capital
gains (as ordinary income, at a preferential rate, or under a separate excise);
filing deadlines where they diverge from federal.

## 2. Estate & inheritance

Two distinct taxes — say which of them the state imposes, and never let one
answer stand in for the other. Include: exclusion amount and whether it is
indexed; rate schedule; **portability between spouses, explicitly** (its absence
drives trust design); the gap between the state exclusion and the federal one,
since the smaller number is the binding constraint; situs rules for real property
owned by a nonresident.

## 3. Marital property

Community-property or common-law, and the planning consequence rather than the
label alone — basis step-up treatment at the first death, any statutory
agreement mechanism, and how character is determined for assets acquired during
marriage. Note the interaction with trust-based estate plans where one exists.

## 4. State programs

Payroll-funded or state-sponsored programs a household is enrolled in by default
or by employer mandate: long-term-care programs, paid family and medical leave,
auto-IRA or state-facilitated retirement savings. For each: who pays, on what
wage base, whether self-employment income is included, what the benefit is, and
whether opt-out is available or has closed.

## 5. Sub-state layer

**Required section.** County, metro, transit-district, and city income or payroll
taxes, each with the jurisdictional test that turns it on — residence, physical
work location, or employer location are three different tests and routinely give
three different answers for the same household.

State resolution must therefore return **state plus locality flags**, not a state
alone. A module whose sub-state layer says "none" is making a claim; a module that
omits the section has not looked.

## 6. Cross-state interactions

Bilateral content lives in the module of *each* state it concerns (per D1), not
in a shared file. Every item carries a **mirror note** naming its counterpart
module in plain prose, so a refresh on either side updates both:

> mirror: states/xx.md (status)

Cover, where applicable: nonresident taxation of income sourced to this state;
credits for taxes paid to another state, **including the case where no credit
mechanism can exist** because this state levies no comparable tax; part-year
residency and the relocation year; situs of real property held across a border.

## 7. Authorities

Same two-column schema as every table in `../authorities.md`, so a state table
and a federal table can be read the same way and concatenated into a
meeting-prep packet without reformatting:

| Topic | Controlling authority |
|---|---|
| | |

Cite the statute or regulation, not a summary page. Where a rule rests on
session law not yet codified, cite the bill and note it. Where litigation is
pending, say so with the last-verified posture and its date.

## 8. Advisor questions

Three to five questions this state's rules generate for the household's own
professional — the CPA, estate attorney, or fiduciary advisor. Each should be
answerable by that professional and specific to this state, not a generic
planning prompt. These feed the "Authorities in play" section of the prep packet
built per `../advisor-meetings.md`.

## 9. Legislative watch

Enacted-but-not-yet-effective changes, pending ballot measures, and live
constitutional or statutory challenges — each with its effective date or decision
date, and an explicit "treat as unsettled" where the outcome is genuinely open.
Pre-position a `VERIFY` marker for the refresh cycle that will need to resolve it.
Mirror anything with a household-planning consequence into `../guardrails.md`.
