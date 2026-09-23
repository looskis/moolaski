# moolaski

One skill, `financial-analyst`, published on [skills.sh](https://www.skills.sh/). The promise: install it and you have an analyst at your disposal. Every change is judged against that.

## Layout

```
skills/financial-analyst/
  SKILL.md                  how the analyst works, and which guide to read for which request
  references/
    core/                   conventions every model shares: layout, timing, balances, returns, review
    real-estate/            one guide per model, plus its formula sheets
    project-finance/
    investment-banking/
    corporate-finance/
templates/model-guide.template.md
scripts/check_skill.py      validates the skill (CI runs it)
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
