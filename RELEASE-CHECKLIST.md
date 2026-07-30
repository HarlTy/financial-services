# Release Checklist

How work moves from this repo to the two things that actually serve it. Written
down because the serving paths drift silently — a merge that skips the release
step leaves `main` correct and both audiences stale, with nothing failing to
tell you.

## Branch discipline

| Branch | Role |
|---|---|
| `main` | The release line. Released, marketplace-served. Every commit here is expected to be complete and verified. |
| `state-modules` | In-progress work. Phase work lands here continuously. |

**Merge at verified milestones only.** A milestone means the work is complete
*and* its verification has run — for Phase 0, that its post-refactor eval run
matches [`evals/baseline-v1.0-wa-only.md`](./evals/baseline-v1.0-wa-only.md).
Not "the code looks done."

## Distribution model

The repo is the source of truth. It reaches two audiences by two independent
paths, and they do not update each other:

```
repo (source of truth)
  └── main (release line)
        ├── marketplace  ──►  the public fork's audience installs from here
        └── .skill upload ──►  claude.ai, serves Tyler's runtime sessions
```

The plugin is deliberately **not** installed locally on the maintainer's
machine. The claude.ai upload already serves that runtime; installing the
marketplace copy too would put two copies of the same skill in front of desktop
sessions, and duplicate-trigger ambiguity is a failure class worth avoiding
outright. The marketplace clone is the *published artifact*, not what this
machine runs.

## Every merge to main ends with a release step

Non-optional. Two serving paths, so two actions — skip either and that audience
silently keeps the old version:

- [ ] **Merge** `state-modules` → `main`, and push `main`. Pass the merge message
      with `-F <file>`, not `-F -` — unlike `git commit`, `git merge` does not
      read a message from stdin and fails with `could not read file '-'`.
- [ ] **Marketplace:** `claude plugin marketplace update harlty-financial-services`
- [ ] **Verify marketplace:** installed copy at `~/.claude/plugins/marketplaces/HarlTy-financial-services`
      is content-identical to `main`. Diff with `--strip-trailing-cr` — the clone
      is CRLF and the repo is LF, so a raw `diff -r` reports every line of every
      file as changed and buries any real difference.
- [ ] **.skill artifact:** repackage and re-upload to claude.ai.
- [ ] **Confirm the version moved.** If `.claude-plugin/plugin.json` `version` did
      not change, already-installed users receive nothing regardless of what you
      pushed. The pre-commit gate normally handles this (see
      [README](./README.md#plugin-versions-are-enforced-not-remembered)).
- [ ] **Record it in the release log below** — version, date, `main` SHA, artifact
      `sha256`, and what was uploaded or deliberately skipped, with the reason.

## Release log

One line per release. This exists because the `.skill` artifact carries no
version marker of its own — `version` lives in `.claude-plugin/plugin.json`,
which is not part of the skill package — so an uploaded skill cannot be
identified by inspection. Until artifacts are self-identifying, this log is the
external record that tells you which release a serving copy corresponds to.

Two identifiers per entry, because they answer different questions:

- **Skill tree** — the git tree object of the skill folder. Content-addressed and
  reproducible anywhere, forever. This is what you verify *content* against.
- **Artifact sha256** — the hash of the `.skill` bytes actually uploaded. Use it
  to confirm a specific file is the one that went out. **Do not** expect a
  rebuild to reproduce it: ZIP stores per-entry mtimes, so repackaging identical
  content after a fresh clone yields a different hash (verified — same eight
  files, mtimes shifted, hash changed completely). A mismatch here means
  "different build", not "different content".

```bash
# content check -- reproducible, this is the authoritative one
git rev-parse <main-sha>:plugins/vertical-plugins/personal-financial-strategy/skills/financial-strategy

# identify a particular .skill file you have on disk
sha256sum dist/financial-strategy.skill
```

- **0.2.0** — 2026-07-29 — `main` @ `88bbca4` — skill tree `f0e5d71d` —
  `financial-strategy.skill` sha256
  `0b2cdc36f275994144a2340d16284bd7905100670e2608d98afc456faf850d8c` —
  **claude.ai upload: not performed**; serving copy verified content-identical
  (skill folder unchanged `1055500` → `88bbca4`; app copy previously verified
  byte-identical at `1055500`). Marketplace: verified at `88bbca4`, tree-object
  match. The merge carried only repo-level files — checklist, hook, README,
  CLAUDE.md, check.py, eval files — nothing inside the skill folder, whose tree
  object is `f0e5d71d` at both commits. Content drift for this release: zero, so
  a re-upload would have been a no-op.

### Why this list exists

The gate that was supposed to enforce version bumps was a silent no-op on
Windows for its entire life: it probed only `python3` (absent on this machine)
and exited 0, and separately fed backslashed paths into a git `<rev>:<path>`
spec, which failed in a way that read as "plugin is new, nothing to bump." Both
defects failed *open* — reporting success while enforcing nothing. Meanwhile the
marketplace clone sat on an orphaned commit from a rewritten `main`, missing the
recovered authority layer entirely.

Nothing alerted anyone. That is the shape of this failure class: the drift is
invisible from inside the repo, because the repo is fine. Only an explicit,
checked step at merge time catches it.
