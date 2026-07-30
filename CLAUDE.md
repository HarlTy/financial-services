# Financial Services Plugins

Cowork plugins and Claude Managed Agent templates for financial services. Each named agent ships two ways from one source.

## Repository Structure

```
├── plugins/
│   ├── agent-plugins/               #   named agents — one self-contained plugin each
│   │   └── <slug>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── agents/<slug>.md     #   ← canonical system prompt (one source, two wrappers)
│   │       └── skills/              #   ← bundled copies, synced from vertical-plugins/
│   ├── vertical-plugins/            #   FSI verticals — skill sources, commands, MCPs
│   │   └── <vertical>/
│   │       ├── .claude-plugin/plugin.json
│   │       ├── commands/
│   │       ├── skills/
│   │       └── .mcp.json
│   └── partner-built/               #   partner plugins (LSEG, S&P Global)
├── managed-agent-cookbooks/         # CMA cookbooks (one dir per named agent)
│   └── <slug>/
│       ├── agent.yaml               #   system + skills → ../../plugins/agent-plugins/<slug>/...
│       ├── subagents/*.yaml         #   depth-1 leaf workers
│       ├── steering-examples.json
│       └── README.md                #   security tier + handoff notes
├── claude-for-msft-365-install/     # admin tooling for the Microsoft 365 add-in (separate from FSI plugins)
└── scripts/                         # deploy-managed-agent.sh, check.py, validate.py, orchestrate.py, sync-agent-skills.py
```

Run `python3 scripts/check.py` before committing — it lints every manifest, verifies all `system.file` / `skills.path` / `callable_agents.manifest` references resolve, fails if any `agent-plugins/<slug>/skills/` copy has drifted from its `vertical-plugins/` source, rejects non-ASCII bytes in a `.ps1` without a UTF-8 BOM, requires a `SKILL.md` body `Version:` line to equal its plugin's `plugin.json` version, and resolves the markdown reference paths written inside a skill.

**Two reference-path conventions are both valid**, because both are in active use: `SKILL.md` writes skill-root-relative (`references/authorities.md`) while files inside `references/` write bare-sibling (`frameworks.md`). A path passes if it resolves against either. **Backticks or link syntax mean "must resolve now"; a path in plain prose may name a file that does not exist yet** — that is how a state module's forward reference to an unbuilt sibling (`mirror: states/oregon.md`) stays legible without tripping the gate. URLs are skipped and never fetched; the check makes no network calls. Enforcement is per-plugin via `SKILL_REF_ENFORCED` in `check.py`: unadopted plugins carry pre-existing unresolved references, so their findings are counted and reported rather than failing the run. Add a plugin to the set once its references resolve.

**Keep `.ps1` files pure ASCII.** Windows PowerShell 5.1 — still the default shell on managed Windows — decodes a BOM-less `.ps1` using the machine's ANSI code page, not UTF-8. An em dash or curly quote becomes mojibake that can contain a literal `"`, which terminates a string and makes the whole script fail to *parse*. Write `--`, not `—`. This is invisible on macOS and fatal on Windows; `check.py` gates it. **Edit skills in `vertical-plugins/`**, then run `python3 scripts/sync-agent-skills.py` to propagate into the agent bundles.

`check.py` also self-installs a `pre-commit` hook (`git config core.hooksPath .githooks` — no Husky/Node). The hook patch-bumps any plugin's `.claude-plugin/plugin.json` `version` so a branch ends up exactly one patch ahead of `main` (bumped once, not per commit — a plugin's `version` gates update delivery to already-installed users). It also **syncs any `Version:` line in a `SKILL.md` body** to match that manifest, because the manifest is not part of the skill package and a packaged `.skill` would otherwise be unidentifiable by inspection. The line is only ever rewritten, never inserted, so a skill that has not opted in is untouched. Syncing is not cosmetic: bumping the manifest alone would leave the body stale and `check.py` would then reject the very commit the hook had just written — the gate would manufacture its own violation. The `version-bump` GitHub Action enforces both rules on PRs as a backstop. Bypass a single commit with `git commit --no-verify`; bump logic lives in `scripts/version_bump.py`. A missing Python interpreter **blocks** the commit rather than skipping the gate — a gate that fails open reports success while enforcing nothing.

**Branching and release.** `main` is the release line (marketplace-served); `state-modules` carries in-progress work and merges only at verified milestones. Every merge to `main` ends with a release step — marketplace update **and** `.skill` repackage/re-upload — because those two serving paths are independent and drift silently. See **[RELEASE-CHECKLIST.md](./RELEASE-CHECKLIST.md)**; do not skip it when merging.

## Key Files

- `marketplace.json`: Marketplace manifest - registers all plugins with source paths
- `plugin.json`: Plugin metadata - name, description, version, and component discovery settings
- `commands/*.md`: Slash commands invoked as `/plugin:command-name`
- `skills/*/SKILL.md`: Detailed knowledge and workflows for specific tasks
- `*.local.md`: User-specific configuration (gitignored)
- `mcp-categories.json`: Canonical MCP category definitions shared across plugins

## Development Workflow

1. Edit markdown files directly - changes take effect immediately
2. Test commands with `/plugin:command-name` syntax
3. Skills are invoked automatically when their trigger conditions match
