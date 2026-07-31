# Guardrails, Disclaimers, and Refresh Protocol

## Standing disclaimer (adapt to fit; include once per substantive session, not per message)
"Educational information only — not individualized investment, tax, or legal advice, and no advisory relationship is created. Figures are for the stated tax year and change. Decide with your fiduciary advisor, CPA, or estate attorney before acting."

## Hard routes — educate and analyze, then hand off; never end with "do X"
- Specific security or fund selection, or trade timing.
- Insurance or annuity product purchase decisions.
- Estate document drafting: wills, trusts, POAs, community property agreements, beneficiary language.
- Tax-return positions and elections.
- Executing irreversible or unforgiving moves: Roth conversion execution, NUA election, 72(t)/SEPP start, S-corp election, retirement-plan adoption or termination.

For each: full education, scenario math, and a "take to your advisor" block (the decision, the inputs used, the questions that resolve it) are in scope — the final call is not.

## Canonical unbuilt-state fallback (single source of truth)

When rule 4 resolves a state that has **no module** under `states/`, give the
federal analysis, then emit this text **verbatim**, substituting the state name.
It is stored here and nowhere else so that the wording cannot drift between the
skill, the eval rubric, and the module set:

> State-level rules for [State] are not yet built into this skill. The federal analysis above stands; before acting, verify with your advisor: [State]'s income tax treatment of this item, any estate or inheritance tax, and marital-property regime.

Then add **one flag line per `states/_index.md` cell marked `Yes`** for that
state. Cells marked `VERIFY` contribute **no** flag line — a flag asserts a fact,
and an unresearched cell has none to assert. Do not substitute a remembered fact
for a `VERIFY` cell to make the answer feel more complete; the fallback's value is
that it is honest about the boundary.

Do not soften, expand, or paraphrase the block above. "The federal analysis above
stands" is doing specific work: it tells the user what they *can* rely on, so the
fallback reads as a scoped limitation rather than a refusal.

## Figure-handling rules
- Every number carries its tax year. Numbers come from the reference tables, never model memory.
- FINAL vs VERIFY status travels with the figure into the answer.
- **Known conflicts / open verifications as of 2026-07-28** (do not present without the flag until re-verified):
  - TY2026 long-term capital-gains bracket thresholds — the circulating figures match TY2025 values; confirm Rev. Proc. 2025-32.
  - Medicare Part D national base beneficiary premium ($38.99) and exact IRMAA surcharge dollars — secondary-source.
  - OBBBA senior bonus deduction phase-out thresholds.
  - TY2026 annual gift exclusion ($19,000 reported unchanged).
  - WA capital-gains standard deduction for TY2026; WA estate exclusion indexation for early-2026 deaths.
  - HSA/Medicare retroactive-Part-A contribution stop rule.
  - AMT exemption amounts; exact 37%-bracket start points; 2026 SALT-cap dollar figures.
- If a needed figure is absent from the tables: say so, use a clearly labeled placeholder or range, and add it to the refresh list. Never invent a number, citation, or rule.
- Lesson encoded from the build's own verification pass: secondary tax-summary sites routinely carry prior-year thresholds labeled as current-year — for any inflation-indexed threshold, primary-source confirmation is the only acceptable basis.

## Authority-handling rules
- Citations come from `references/authorities.md`, from the skill's own reference tables (which carry their own source citations), or from text retrieved this session — never from unaided memory. A section number found in none of those places does not get cited.
- Hierarchy when sources disagree: statute → regulation → agency guidance (Rev. Proc./Notice, CMS rules, SSA POMS, WA DOR issuances) → publications and FAQs (persuasive only). Name the level when it matters.
- Pin-cite to the section; when text was retrieved, append the retrieval date. Paraphrase the operative rule; quote at most a sentence or two.
- Litigation posture (e.g., the ESSB 6346 challenge) is a moving target: check a docket source if one is available in the session; otherwise state the last-verified posture and its date.
- The map exists for conversational leverage, not self-help lawyering: authorities feed the "Authorities in play" packet section and the questions handed to the professional — the judgment call stays with the CPA, attorney, or fiduciary.

## Annual refresh checklist (run each November–December, or on request)
1. IRS: the new-year inflation-adjustment Rev. Proc. and the retirement-limits Notice → update income-tax and retirement tables; the spring Rev. Proc. → HSA table.
2. SSA fact sheet: COLA, wage base, earnings-test amounts.
3. CMS fact sheet: Part B premium and deductible, IRMAA tiers and surcharge dollars, Part D base premium.
4. **Per state module, one refresh stamp each.** For every module under `states/`, re-verify its figures at that state's revenue authority and update *that file's* own "Last verified" date — modules refresh independently, so a single repo-wide date would lie about all but one of them. Currently: **WA** (`states/washington.md`) — WA DOR capital-gains standard deduction, estate-tax exclusion and rate tables. The WA statute changed in both 2025 and 2026 — check every year without exception. Record each module's stamp below as modules are added.
   - `states/_index.md`: **rows refresh only when researched.** Clearing a `VERIFY` requires a primary-source check for that cell, not an inference from a neighbouring cell or from the module's other contents. A row left `VERIFY` after a refresh is a correct outcome; a row filled to look complete is a fabrication with a date on it.
5. Legislative watch: OBBBA temporary provisions (tips/overtime/senior bonus through 2028; SALT reversion 2030); IRMAA fifth-tier indexing resumption (2028); ACA premium-credit status (politically live); WA ESSB 6346 (9.9% tax on income over $1M, effective 2028) and initiative I-645 (November 3, 2026 ballot); WA Cares amendments.
6. Re-verify the authorities map: statute/WAC renumbering, new public laws, codification of P.L. 119-21 provisions still cited at the session-law level, and litigation posture (ESSB 6346 challenge; I-645 result).
7. Clear resolved VERIFY flags; update the "Last verified" date in every file.

## Scope honesty
This skill covers U.S. federal rules for a personal/household context, with a business-owner overlay, plus a **pluggable state layer**: a jurisdiction-neutral federal core and one module per state under `states/`. Washington is built; Oregon is in progress; every other state and DC is `UNBUILT`.

An unbuilt state is a **known, signposted gap, not silent federal-only treatment** — rule 4 requires the federal answer plus the canonical fallback above, so the user learns what is missing instead of receiving a national answer that reads as complete. Multi-state situations are in scope to the extent the relevant modules exist and their cross-state sections are authored; where they are stubs, say so.

Still out of depth regardless of module coverage: international assets, concentrated equity compensation, and special-needs planning. Sub-state (city, county, metro) rules are only as good as the resolved module's sub-state section, which may be `VERIFY`. Name the gap and route to the professional rather than stretch.
