#!/usr/bin/env python3
"""Validate the financial-analyst skill.

Checks:
  - exactly one SKILL.md in the repo (the skills CLI lets a shallower one shadow the rest)
  - frontmatter with a lowercase-hyphenated name matching its folder, and a description
  - every guide under references/ is linked from SKILL.md, so the agent can find it
  - every relative link in the skill resolves

Usage: python3 scripts/check_skill.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "financial-analyst"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")
MAX_DESCRIPTION = 1024
MAX_LINES = 500


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def links(path):
    return [(path.parent / t).resolve() for t in LINK_RE.findall(path.read_text()) if "://" not in t]


def main():
    errors = []
    skill_md = SKILL / "SKILL.md"

    others = [p.relative_to(ROOT) for p in ROOT.rglob("SKILL.md") if p != skill_md and ".git" not in p.parts]
    errors += [f"{p}: only one skill lives here; make it a guide under references/" for p in others]

    if not skill_md.exists():
        errors.append(f"{skill_md.relative_to(ROOT)} is missing")
    else:
        text = skill_md.read_text()
        fm = frontmatter(text)
        if fm is None:
            errors.append("SKILL.md: missing frontmatter")
        else:
            name, desc = fm.get("name", ""), fm.get("description", "")
            if name != SKILL.name or not NAME_RE.match(name):
                errors.append(f"SKILL.md: name '{name}' must be '{SKILL.name}'")
            if not desc:
                errors.append("SKILL.md: missing description")
            elif len(desc) > MAX_DESCRIPTION:
                errors.append(f"SKILL.md: description is {len(desc)} characters, over {MAX_DESCRIPTION}")
        if text.count("\n") > MAX_LINES:
            errors.append(f"SKILL.md: over {MAX_LINES} lines; move detail into a guide")

        linked = set(links(skill_md))
        guides = sorted((SKILL / "references").rglob("*.md"))
        for g in guides:
            if g.resolve() not in linked:
                errors.append(f"{g.relative_to(ROOT)}: not linked from SKILL.md")

        for md in [skill_md, *guides]:
            for target in links(md):
                if not target.exists():
                    errors.append(f"{md.relative_to(ROOT)}: broken link to {target.relative_to(ROOT)}")

    for e in errors:
        print(f"error: {e}", file=sys.stderr)
    guides = len(list((SKILL / "references").rglob("*.md"))) if SKILL.exists() else 0
    print(f"{SKILL.name}: {guides} guides, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
