# moolaski

Financial modeling skills for AI agents, published on [skills.sh](https://www.skills.sh/).

## Layout

```
skills/<category>/<skill-name>/SKILL.md   one folder per skill
  core/                 fm-*   conventions every model shares (layout, formatting, checks, timing)
  real-estate/          re-*   acquisitions, development, waterfalls, ...
  project-finance/      pf-*   CFADS, sculpting, reserves, ...
  investment-banking/   ib-*   LBO, merger, comps, DCF, ...
  corporate-finance/    cf-*   3-statement, budgeting, ...
templates/              SKILL.md template
scripts/check_skills.py validates skills and regenerates CATALOG.md
```

## Rules that keep the catalog navigable

- **One job per skill.** A skill covers one model or one technique (e.g. `re-development-model`, `pf-debt-sculpting`), never a whole domain.
- **Name = `<prefix>-<topic>`**, prefix from the category table above. Names are globally unique and lowercase-hyphenated.
- **The description is the router.** It says what the skill builds and when to use it, with the words a user would actually say ("LBO", "sources and uses", "promote"). An agent picks a skill from descriptions alone.
- **No `SKILL.md` directly in a category folder** — the skills CLI lets a shallower `SKILL.md` shadow everything below it.
- **Shared conventions live in `core/`**, referenced by name from domain skills rather than copied.
- Long material goes in the skill's own `references/` folder and is linked from `SKILL.md`, which stays short.
- After adding or renaming a skill, run `python3 scripts/check_skills.py` (writes `CATALOG.md`).

## Publishing

skills.sh installs straight from GitHub: `npx skills add <owner>/moolaski --list` shows every skill and `--skill <name>` installs one.
