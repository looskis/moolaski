# moolaski

One skill, `moolaski-financial-analyst`, published on [skills.sh](https://www.skills.sh/). The promise: install it and you have an analyst at your disposal. Every change is judged against that.

## Layout

```
skills/moolaski-financial-analyst/
  SKILL.md                  how the analyst works, and which guide to read for which request
  references/
    core/                   conventions every model shares: layout, timing, balances, returns, review
    real-estate/            one guide per model, plus its formula sheets
    project-finance/
    investment-banking/
    corporate-finance/
  scripts/check_workbook.py recalculates a workbook and reports what the analyst checks
templates/model-guide.template.md
scripts/check_skill.py      validates the skill (CI runs it)
scripts/test_check_workbook.py  regression test for the skill's workbook checker (CI runs it)
```

## Rules

- **One skill.** A new model is a new guide under `references/<domain>/`, never a new skill. The checker fails on any second `SKILL.md`, since the skills CLI lets a shallower one shadow the rest.
- **SKILL.md is the analyst, not the textbook.** It holds how the analyst works (scope, inputs, build, check, answer) and the routing table. Model knowledge lives in the guides.
- **Every guide is in the routing table**, with the words a user would actually say ("LBO", "sources and uses", "promote"). The frontmatter description carries the broadest of those words: an agent decides to load the skill from its description alone, and it has 1024 characters.
- **Guides are named for the model**: `<model>.md`, with long material beside it as `<model>-<topic>.md` (formulas, waterfall, mechanics). SKILL.md links every file directly, so none sits more than one hop away.
- **Shared conventions live in `core/`**, and guides link to them rather than copying them.
- When a guide lands, move its model out of *Not in the playbook yet* in SKILL.md and into the README's coverage table.
- Run `python3 scripts/check_skill.py` before committing.

## Publishing

skills.sh installs straight from GitHub: `npx skills add looskis/moolaski` installs the skill. A skill appears on skills.sh once someone installs it.

## Being found

Agents find skills with `npx skills find <query>`, which asks skills.sh's search. What that search sees:

- **The name and the description are indexed; the SKILL.md body is not.** A word a user might search for has to be in one of those two. The repo name (`moolaski`) is matched too.
- **Results rank by installs.** `npx skills find` keeps the top 20 matches and sorts them by install count, and the skills.sh leaderboard is installs only.
- **The name must be unique.** It is the install folder (`.claude/skills/<name>/`), so two skills with one name overwrite each other, and in search a shared name sorts below the one with more installs. Several skills are already called `financial-analyst`; ours is `moolaski-financial-analyst`. Don't rename it again: skills.sh keys entries as `owner/repo/name`, so a renamed skill is a new entry that starts from zero installs.
