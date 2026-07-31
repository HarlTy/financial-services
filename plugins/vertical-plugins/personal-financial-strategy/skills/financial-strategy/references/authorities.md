# Primary Authority Map & Retrieval Protocol

Last verified: 2026-07-28. **This file is a finding aid, not an authority.** Its job: (1) tell you which statute, regulation, or agency issuance controls a topic, (2) tell you where the current official text lives, and (3) turn authorities into the questions that make a meeting with a CPA, estate attorney, or fiduciary advisor maximally productive. It exists to prepare that conversation, never to substitute for it.

## Retrieval protocol

- **Hierarchy when sources disagree:** constitution/statute → regulations → agency guidance (Rev. Rul., Rev. Proc., Notices; CMS rules; SSA POMS; WA DOR ETAs and Special Notices) → publications, instructions, and FAQs (persuasive only, not authority). Say which level a rule comes from whenever the distinction could matter.
- **When a conclusion turns on a legal rule and the session has web access:** retrieve the current text from the official source below before citing, and append the retrieval date.
- **Canonical index-only label (single source of truth).** When any cited authority was not re-verified against current text this session, end the citation block — or the response, if citations are inline — with this text **verbatim**:

  > Citations from this skill's index — text not re-verified this session.

  Do not paraphrase or shorten it. It is stored here and nowhere else so the wording cannot drift between the skill, the rubric, and the answers. Retrieved citations are the exception, and they carry their retrieval date individually; one index-only citation anywhere in the response triggers the label.
- **Anti-fabrication gate:** never cite a section number that is neither in this map, nor in the skill's own reference tables (which carry their own source citations), nor freshly retrieved. If the needed authority is in none of those places, retrieve first, cite second, and add it to the map at the next refresh.
- **Litigation posture** (e.g., the challenge to Washington's ESSB 6346) is a moving target: if a docket/case-law tool (such as a CourtListener connector) is available in the session, check it; otherwise state the last-verified posture with its date.
- **Quoting:** paraphrase the operative rule and pin-cite; quote at most a sentence or two even though statutes are public domain — precision and context economy both favor paraphrase.

### Oregon source slate — Phase 1 input

**Not yet researched.** This is a retrieval slate handed forward to the Oregon
module build, not a citation map: nothing below has been confirmed against
primary text in this session, and no figure here may be used in an answer. It is
recorded so the Phase 1 build starts from a scoped source list rather than a
search.

- **Statutes:** ORS ch. 316 (income) and ch. 118 (estate) at
  oregonlegislature.gov/bills_laws/ors/. Note ch. 118 was amended by 2025 c.577
  and c.595 — including ORS 118.145, a natural-resource exemption with a $15M cap.
- **Oregon DOR:** income, estate (OR-706), and the kicker.
- **Portland Revenue Division:** portland.gov/revenue/personal-tax — administers
  both Metro SHS and Multnomah PFA.
- **Multnomah County Code ch. 11 (PFA):** rate-increase delay to 1/1/2027; TY2026
  estimated-payment threshold moving $1,000 → $5,000.
- **Metro Code (SHS):** June 2025 changes; TY2026+ threshold inflation-indexing.
  **PFA thresholds are NOT indexed** — the two programs diverge here, so do not
  reason about one from the other.
- **OregonSaves** program rules.

Watch list to resolve at build: 2025 estate bills HB 2058, HB 2112, HB 2301,
HB 2362, HB 3737, and SB 380, SB 405, SB 648, SB 764 — disposition of each to be
recorded when the module is written. PFA 0.8% rate increase effective 1/1/2027 is
a pre-positioned VERIFY for the TY2027 refresh.

## Official current-text sources

| Body of law | Source |
|---|---|
| U.S. Code (IRC = Title 26; Social Security Act provisions = Title 42; ERISA = Title 29) | uscode.house.gov (Office of the Law Revision Counsel) |
| Federal regulations (26 C.F.R. Treasury; 42 C.F.R. CMS; 29 C.F.R. DOL) | ecfr.gov |
| Public laws (OBBBA = P.L. 119-21; SECURE 2.0 = Div. T of P.L. 117-328; SECURE Act = Div. O of P.L. 116-94) | congress.gov / govinfo.gov |
| IRS guidance (Rev. Procs., Rev. Ruls., Notices) | irs.gov — Internal Revenue Bulletin |
| SSA program rules | ssa.gov (Act text and handbook); POMS at secure.ssa.gov/poms |
| CMS premiums and rules | cms.gov newsroom; federalregister.gov |
| SEC adviser/broker rules and filings | sec.gov; adviserinfo.sec.gov (Form ADV); brokercheck.finra.org |
| Washington statutes and rules | app.leg.wa.gov/rcw and /wac; session laws at lawfilesext.leg.wa.gov |
| WA Dept. of Revenue guidance | dor.wa.gov (capital-gains and estate-tax pages; ETAs; Special Notices) |
| Convenience mirror only | law.cornell.edu (never cite as the source of truth) |

## Citation map by domain

**Federal only.** State authorities live in the state's own module under
`states/` — same two-column schema, so a state table and a federal table read the
same way and concatenate into a meeting-prep packet without reformatting. For
Washington, see `states/washington.md` §7. The retrieval endpoints above stay
here, because finding the current text is a retrieval concern rather than a
jurisdictional one.

### Retirement accounts and plans
| Topic | Controlling authority |
|---|---|
| Elective deferral limit (shared across employers) | IRC §402(g) |
| Designated Roth accounts; mandatory Roth catch-up (2026) | IRC §402A; SECURE 2.0 §603 |
| Catch-up contributions (50+; 60–63) | IRC §414(v) |
| DC annual-additions limit (per employer) | IRC §415(c) |
| DB benefit limit / compensation cap | IRC §415(b) / §401(a)(17) |
| **Controlled and affiliated service groups** (whether the W-2 employer and the LLC are "unrelated") | IRC §414(b), (c), (m) |
| RMDs; 10-year inherited rule; RMD excise; excess-contribution excise | IRC §401(a)(9) and §401(a)(9)(H); Treas. Reg. §1.401(a)(9) (2024 final regs); IRC §4974; IRC §4973 |
| IRAs / SEP / SIMPLE / Roth IRA / IRA deduction | IRC §408; §408(k); §408(p); §408A; §219 |
| QCDs | IRC §408(d)(8) |
| Early-distribution tax and SEPP exception | IRC §72(t) |
| Plan loans | IRC §72(p) |
| NUA on employer stock | IRC §402(e)(4) |
| Rollovers | IRC §402(c) |
| ERISA fiduciary duty (owner-only plans generally sit outside ERISA Title I) | 29 U.S.C. §1104 |
| 529 plans; 529→Roth rollovers | IRC §529, as amended by SECURE 2.0 §126 |

### Individual income tax
| Topic | Controlling authority |
|---|---|
| Rate structure (made permanent) | IRC §1; P.L. 119-21 |
| Standard deduction; additional deduction 65+ | IRC §63(c); §63(f) |
| Senior bonus deduction; tips and overtime deductions; charitable non-itemizer deduction and 0.5% AGI floor | P.L. 119-21 (IRC codification sections — VERIFY before pin-citing) |
| Child tax credit | IRC §24 |
| AMT | IRC §§55–59 |
| SALT cap | IRC §164(b)(6) |
| QBI deduction; SSTB rules | IRC §199A |
| Social Security benefit taxation | IRC §86 |
| NIIT | IRC §1411 |
| LTCG rates; wash sales; home-sale exclusion ($250k/$500k, not indexed) | IRC §1(h); §1091; §121 |
| Charitable deduction | IRC §170 (as amended by P.L. 119-21) |
| HSAs; no contributions once Medicare-entitled | IRC §223; §223(b)(7) |
| ACA premium tax credit (enhanced credits expired 12/31/2025) | IRC §36B |
| SE tax; FICA | IRC §1401; §§3101, 3111 |
| Trump accounts | P.L. 119-21 (codification — VERIFY before pin-citing) |

### Estate, gift, and inherited assets
| Topic | Controlling authority |
|---|---|
| Federal exemption and unified credit; portability (DSUE) | IRC §2010; §2010(c) |
| Annual gift exclusion | IRC §2503(b) |
| Marital deduction; QTIP (election and inclusion) | IRC §2056; §2056(b)(7); §2044 |
| Qualified disclaimers (disclaimer-trust flexibility) | IRC §2518 |
| Basis step-up at death; community property double step-up | IRC §1014; §1014(b)(6) |
| Income in respect of a decedent | IRC §691 |
| Charitable remainder trusts; valuation rates | IRC §664; §7520 |
| Installment payment of estate tax on closely held business | IRC §6166 |

### Social Security and Medicare
| Topic | Controlling authority |
|---|---|
| OASDI benefits; earnings test; COLA; FRA; wage base | 42 U.S.C. §402; §403; §415(i); §416(l); §430 |
| Part B premium; IRMAA | 42 U.S.C. §1395r; §1395r(i) |
| Part D IRMAA | 42 U.S.C. §1395w-113(a)(7) — VERIFY pin |
| Enrollment periods and penalties | 42 U.S.C. §§1395p–1395q; 42 C.F.R. pts. 406–408 (VERIFY pinpoint) |
| Medigap | 42 U.S.C. §1395ss |
| COBRA continuation (and why it doesn't extend the Medicare SEP) | 29 U.S.C. §1161 et seq. |

### Advisers and standards of care
| Topic | Controlling authority |
|---|---|
| Adviser fiduciary duty | Investment Advisers Act of 1940, 15 U.S.C. §80b-1 et seq. (antifraud basis §80b-6); SEC Commission Interpretation Regarding Standard of Conduct for Investment Advisers (2019) |
| Broker standard | Regulation Best Interest, 17 C.F.R. §240.15l-1 |
| Disclosures | Form ADV Part 2 and Form CRS (SEC rules — pin cites VERIFY); adviserinfo.sec.gov; brokercheck.finra.org |

## Authority → conversation

The pattern: **name the authority, state the fact pattern, and hand the professional the judgment call.** That is what turns a meeting from a briefing into a decision. Worked examples:

- **CPA (dual-plan strategy):** "Confirm there's no §414(b)/(c)/(m) controlled-group or affiliated-service-group relationship between my W-2 employer and my LLC — the separate $72,000 §415(c) limit for a Solo 401(k) depends on the two being unrelated."
- **Estate attorney (WA gap):** "Washington gives us no portability under RCW 83.100. Do we fund a credit-shelter trust, or rely on §2518 disclaimer flexibility — and does a community property agreement under RCW 26.16.120 conflict with that trust design?"
- **Advisor (conversion ladder):** "Model the proposed Roth conversions (§408A) against the IRMAA tiers under 42 U.S.C. §1395r(i) — two-year lookback, per person, cliff pricing — before we size any year."
- **CPA (entity + QBI coupling):** "At our income, where do we sit in the §199A SSTB phase-out, and how do retirement-plan deductions and an S-corp election move that answer?"

Every meeting-prep packet includes an "Authorities in play" section built this way (see `advisor-meetings.md`, packet item 7): one line per pending decision — the authority, the fact, the question.
