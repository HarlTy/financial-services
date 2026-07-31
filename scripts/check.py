#!/usr/bin/env python3
"""
Lint all plugin + managed-agent manifests and verify cross-file references.

Checks:
  1. Every *.yaml under managed-agents/ parses.
  2. Every plugin.json / marketplace.json / steering-examples.json parses.
  3. Every <vertical>/agents/*.md has valid YAML frontmatter with name + description.
  4. Every system.file, skills[].path, callable_agents[].manifest in agent.yaml
     and subagent yamls resolves to an existing file/dir.
  5. Every managed-agents/<slug>/ has agent.yaml, README.md, steering-examples.json.

Exit 0 if clean, 1 otherwise. Requires: pyyaml.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGINS = ROOT / "plugins"
MANAGED = ROOT / "managed-agent-cookbooks"
errors: list[str] = []
checked = 0


def ensure_hooks_installed() -> None:
    """Point git at .githooks so the version-bump pre-commit runs.

    Native equivalent of Husky's `prepare`, piggybacked on the script
    everyone already runs before committing. Best-effort: never fatal.
    """
    want = ".githooks"
    try:
        cur = subprocess.run(
            ["git", "-C", str(ROOT), "config", "--get", "core.hooksPath"],
            capture_output=True, text=True,
        ).stdout.strip()
        if cur != want:
            subprocess.run(
                ["git", "-C", str(ROOT), "config", "core.hooksPath", want],
                check=True, capture_output=True,
            )
            print(f"[check.py] installed git hooks (core.hooksPath -> {want})")
    except (subprocess.SubprocessError, OSError):
        pass  # not a git checkout / git unavailable -- ignore


# Install hooks before anything that can exit early (e.g. missing pyyaml),
# so a fresh checkout still gets the version-bump hook wired up.
ensure_hooks_installed()

try:
    import yaml
except ImportError:
    print("ERROR: requires pyyaml (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)


def err(msg: str) -> None:
    errors.append(msg)


def rel(p: Path) -> str:
    return str(p.relative_to(ROOT))


# --- 1. YAML parse ----------------------------------------------------------
for yml in sorted(MANAGED.rglob("*.yaml")):
    checked += 1
    try:
        with open(yml) as f:
            yaml.safe_load(f)
    except yaml.YAMLError as e:
        err(f"YAML parse: {rel(yml)}: {e}")

# --- 2. JSON parse ----------------------------------------------------------
json_globs = [
    ".claude-plugin/marketplace.json",
    "plugins/**/.claude-plugin/plugin.json",
    "managed-agent-cookbooks/*/steering-examples.json",
]
for pat in json_globs:
    for jf in sorted(ROOT.glob(pat)):
        checked += 1
        try:
            json.loads(jf.read_text())
        except json.JSONDecodeError as e:
            err(f"JSON parse: {rel(jf)}: {e}")

# --- 3. agent.md frontmatter -----------------------------------------------
for md in sorted(PLUGINS.glob("agent-plugins/*/agents/*.md")):
    checked += 1
    text = md.read_text()
    if not text.startswith("---"):
        err(f"frontmatter: {rel(md)}: missing leading ---")
        continue
    try:
        _, fm, _ = text.split("---", 2)
        meta = yaml.safe_load(fm)
        for k in ("name", "description"):
            if k not in meta:
                err(f"frontmatter: {rel(md)}: missing '{k}'")
    except (ValueError, yaml.YAMLError) as e:
        err(f"frontmatter: {rel(md)}: {e}")


# --- 4. reference resolution -----------------------------------------------
def check_refs(yml: Path) -> None:
    try:
        data = yaml.safe_load(yml.read_text()) or {}
    except yaml.YAMLError:
        return  # already reported above
    base = yml.parent

    sys_spec = data.get("system")
    if isinstance(sys_spec, dict) and "file" in sys_spec:
        p = (base / sys_spec["file"]).resolve()
        if not p.is_file():
            err(f"ref: {rel(yml)}: system.file -> {sys_spec['file']} (not found)")

    for s in data.get("skills") or []:
        if isinstance(s, dict) and "path" in s:
            p = (base / s["path"]).resolve()
            if not p.exists():
                err(f"ref: {rel(yml)}: skills.path -> {s['path']} (not found)")
        if isinstance(s, dict) and "from_plugin" in s:
            p = (base / s["from_plugin"]).resolve()
            if not (p / "skills").is_dir():
                err(f"ref: {rel(yml)}: skills.from_plugin -> {s['from_plugin']} (no skills/ dir)")

    for c in data.get("callable_agents") or []:
        if isinstance(c, dict) and "manifest" in c:
            p = (base / c["manifest"]).resolve()
            if not p.is_file():
                err(f"ref: {rel(yml)}: callable_agents.manifest -> {c['manifest']} (not found)")


for yml in sorted(MANAGED.rglob("*.yaml")):
    check_refs(yml)

# --- 4b. agent-plugin bundled skills match vertical source -----------------
import filecmp  # noqa: E402
import re  # noqa: E402

src_by_name = {p.name: p for p in PLUGINS.glob("vertical-plugins/*/skills/*") if p.is_dir()}
for bundled in sorted(PLUGINS.glob("agent-plugins/*/skills/*")):
    if not bundled.is_dir():
        continue
    src = src_by_name.get(bundled.name)
    if not src:
        err(f"bundled-skill: {rel(bundled)}: no vertical-plugins source named '{bundled.name}'")
        continue
    cmp = filecmp.dircmp(src, bundled)
    if cmp.diff_files or cmp.left_only or cmp.right_only:
        err(
            f"bundled-skill: {rel(bundled)}: drifted from {rel(src)} "
            f"(run scripts/sync-agent-skills.py)"
        )

# --- 4b2. agent.md skill references exist in the agent's own bundle --------
for md in sorted(PLUGINS.glob("agent-plugins/*/agents/*.md")):
    slug = md.parents[1].name
    sk_dir = PLUGINS / "agent-plugins" / slug / "skills"
    bundle = {p.name for p in sk_dir.iterdir() if p.is_dir()} if sk_dir.is_dir() else set()
    for ref in set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", md.read_text())):
        if ref in src_by_name and ref not in bundle:
            err(
                f"agent-prose: {rel(md)}: references `{ref}` but "
                f"plugins/agent-plugins/{slug}/skills/{ref}/ is not bundled"
            )

# --- 4c. marketplace source paths resolve ----------------------------------
mp = ROOT / ".claude-plugin" / "marketplace.json"
for p in json.loads(mp.read_text()).get("plugins", []):
    src = (ROOT / p["source"]).resolve()
    if not (src / ".claude-plugin" / "plugin.json").is_file():
        err(f"marketplace: {p['name']} source -> {p['source']} (no plugin.json)")

# --- 4d. SKILL.md body version matches its plugin manifest -----------------
# A plugin's version lives in .claude-plugin/plugin.json, which is NOT part of
# the skill package -- so a packaged .skill or a serving copy cannot be
# identified by inspection. A skill may opt in to a `Version:` line at the top
# of its BODY (body, not frontmatter, so the skill validator's schema is
# untouched) to close that gap. Two copies then have to agree.
#
# The version-bump gate validates plugin.json only, so this is the assertion
# that closes the unguarded half. Conditional by design: a skill without the
# line has not opted in, and requiring one would fail 119 files.
#
# Helpers are imported rather than duplicated -- version_bump.py is the single
# source of truth for version mechanics, its main() is __name__-guarded so the
# import has no side effects, and scripts/ is sys.path[0] when this runs.
import version_bump  # noqa: E402

for pj in sorted(PLUGINS.glob("*/*/.claude-plugin/plugin.json")):
    try:
        manifest_version = json.loads(pj.read_text()).get("version")
    except json.JSONDecodeError:
        continue  # already reported by step 2
    for md in version_bump.skill_mds(version_bump.plugin_root(pj)):
        checked += 1
        declared = version_bump.read_skill_version(md)
        if declared is None:
            continue  # this skill has not opted in to a body version marker
        if declared != manifest_version:
            err(
                f"skill-version: {rel(md)}: body says 'Version: {declared}' but "
                f"{rel(pj)} says '{manifest_version}'. These two must move "
                f"together -- run scripts/version_bump.py --apply to sync."
            )

# --- 4e. skill reference paths resolve --------------------------------------
# Nothing else in this repo validates the `references/foo.md` paths written
# inside a skill, so moving a reference file silently breaks every mention of
# it. That is exactly what the state-modules restructure did to washington.md
# across six files, none of which any gate caught.
#
# TWO PATH CONVENTIONS, both live and both accepted: SKILL.md writes
# skill-root-relative (`references/authorities.md`) while files inside
# references/ write bare-sibling (`frameworks.md`). A token passes if it
# resolves against its own file's parent OR against the skill root. Forcing one
# style would churn files that are not broken; accepting both still catches the
# whole target class, since a stale path fails under both.
#
# REPO-INTERNAL ONLY. Tokens must end in .md, and anything carrying a URL
# scheme is skipped outright. This check makes NO network calls, so the
# authorities tables' source columns (app.leg.wa.gov, dor.wa.gov,
# oregonlegislature.gov, portland.gov) cannot fail it.
#
# PLANNED-REFERENCE CONVENTION: backticks or markdown-link syntax means "must
# resolve now"; a path written in plain prose may name a file that does not
# exist yet. That is how a module's forward reference to an unbuilt sibling
# (mirror: states/oregon.md) stays legible without tripping this gate, and how
# a template shows a deliberately-wrong example path. The convention costs
# nothing to enforce because the token pattern below only ever sees backticked
# and linked paths -- plain prose is invisible to it, so the input filter IS
# the exemption mechanism.
MD_REF_RE = re.compile(r"`([^`\n]+?\.md)`|\]\(([^)\s]+?\.md)\)")

# Enforced (fails the check) only for plugins that have adopted the convention;
# elsewhere findings are counted and reported. Five unrelated plugins carry
# pre-existing unresolved references, and a gate that fails on arrival across
# the whole repo blocks every commit -- which gets the gate deleted rather than
# the references fixed. The count is printed rather than dropped so the debt
# stays visible: silence would read as "everything resolves." Add a plugin here
# once its references resolve.
SKILL_REF_ENFORCED = {"personal-financial-strategy"}
skill_ref_unenforced = 0

for skill_md in sorted(PLUGINS.glob("*/*/skills/*/SKILL.md")):
    skill_dir = skill_md.parent
    enforced = skill_md.parents[2].name in SKILL_REF_ENFORCED
    for doc in sorted(skill_dir.rglob("*.md")):
        checked += 1
        try:
            text = doc.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            # Explicit UTF-8, unlike this file's other bare read_text() calls:
            # the Windows default is cp1252, under which 20 SKILL.md files in
            # this repo raise. A bare read here would traceback instead of
            # producing a clean FAIL.
            err(f"skill-ref: {rel(doc)}: not readable as UTF-8: {e}")
            continue
        for m in MD_REF_RE.finditer(text):
            tok = m.group(1) or m.group(2)
            # Not repo-internal, or not a reference at all:
            #   - URL schemes -- never fetched; this check makes no network calls
            #   - absolute paths (/mnt/skills/public/...) -- runtime-supplied
            #     skills that live outside the repo entirely
            #   - bracketed templates ([Company]_Report_[Date].md) -- output
            #     filenames a skill GENERATES, not files it reads
            if "://" in tok or tok.startswith(("http", "mailto:", "#", "/")):
                continue
            if "[" in tok or "]" in tok or "<" in tok:
                continue
            if (doc.parent / tok).is_file() or (skill_dir / tok).is_file():
                continue
            if not enforced:
                skill_ref_unenforced += 1
                continue
            err(
                f"skill-ref: {rel(doc)}: `{tok}` does not resolve (tried it "
                f"relative to the file and to the skill root). If the file is "
                f"planned but unbuilt, write the path in plain prose instead "
                f"of backticks."
            )

if skill_ref_unenforced:
    print(
        f"note: {skill_ref_unenforced} unresolved skill reference(s) in plugins "
        f"outside SKILL_REF_ENFORCED (pre-existing; not failing the check)."
    )

# --- 5. required files per managed-agent -----------------------------------
for d in sorted(MANAGED.iterdir()):
    if not d.is_dir():
        continue
    for req in ("agent.yaml", "README.md", "steering-examples.json"):
        if not (d / req).is_file():
            err(f"missing: {rel(d)}/{req}")

# --- 6. PowerShell scripts must be pure ASCII -------------------------------
# Windows PowerShell 5.1 -- still the default shell on managed Windows -- reads
# a .ps1 with no BOM using the machine's ANSI code page, not UTF-8. A smart dash
# or curly quote then decodes to mojibake that can contain a literal '"',
# which terminates a string mid-file and makes the whole script fail to PARSE.
# It is invisible on macOS and total on Windows, so gate it here.
ASCII_ONLY_SUFFIXES = {".ps1", ".psm1", ".psd1"}
for ps in sorted(ROOT.rglob("*.ps1")):
    if any(part in {".git", "node_modules"} for part in ps.parts):
        continue
    checked += 1
    raw = ps.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        continue  # an explicit BOM tells PS 5.1 it is UTF-8; then non-ASCII is fine
    for lineno, line in enumerate(raw.split(b"\n"), 1):
        bad = sorted({b for b in line if b > 0x7F})
        if bad:
            chars = ", ".join(f"0x{b:02x}" for b in bad[:5])
            err(
                f"non-ascii: {rel(ps)}:{lineno}: byte(s) {chars} in a .ps1 with no "
                f"UTF-8 BOM -- Windows PowerShell 5.1 will mis-decode this and may "
                f"fail to parse the file. Use ASCII (-- for an em dash) or add a BOM."
            )
            break

# --- report ----------------------------------------------------------------
if errors:
    print(f"FAIL -- {len(errors)} issue(s) across {checked} file(s):\n", file=sys.stderr)
    for e in errors:
        print(f"  x {e}", file=sys.stderr)
    sys.exit(1)
print(f"OK -- {checked} file(s) checked, 0 issues.")
