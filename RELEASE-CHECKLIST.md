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

- [ ] **Merge** `state-modules` → `main`, and push `main`.
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
