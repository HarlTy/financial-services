# Personal Financial Strategy (plugin)

Client-side personal planning skill: retirement, tax, estate coordination, Washington-specific rules (capital gains excise, estate tax, community property, WA Cares), business-owner retirement plans (W-2 + LLC), and advisor-meeting preparation. Educational only — hard-routes security selection, product purchases, document drafting, and tax positions to a fiduciary advisor, CPA, or attorney.

Distinct from the upstream `wealth-management` vertical plugin, which is advisor-side (client reviews, proposals, reporting). This one is the client's side of the table.

## Install location in this repo
`plugins/vertical-plugins/personal-financial-strategy/`

## marketplace.json entry to add
```json
{
  "name": "personal-financial-strategy",
  "displayName": "Personal Financial Strategy",
  "source": "./plugins/vertical-plugins/personal-financial-strategy",
  "description": "Client-side personal planning: retirement, tax, WA-specific rules, business-owner plans, and advisor-meeting prep (educational)"
}
```

## Maintenance
Annual data refresh each November–December (IRS/SSA/CMS release cycle) plus a WA legislative check — protocol and open VERIFY flags in `skills/financial-strategy/references/guardrails.md`.
