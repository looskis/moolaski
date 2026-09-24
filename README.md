<p align="center">
  <img src="assets/moolaski-icon.png" alt="moolaski logo" width="128" height="128">
</p>

# moolaski

**A financial analyst for your AI agent.**

Install one skill and your agent works like a good analyst. It pins down the question, finds or asks for the inputs, builds a real Excel model, checks that it ties, and leads with the answer.

```bash
npx skills add looskis/moolaski
```

Works with Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot and the other agents the [skills CLI](https://www.skills.sh/) supports.

## Ask it what you'd ask an analyst

> What's Costco worth? Is the stock cheap at today's price?

> I can buy a rental for $320k. Rent is $2,400 a month and I'd put 25% down. Is it a deal?

> Build a three-statement model from last year's numbers and tell me when we'll need the revolver.

> Our sponsor sent this model. What's wrong with it?

## See it work

From a fresh install, asked the rental question above, unedited:

> **No — not on these numbers. It loses money monthly and returns ~4% a year.**
>
> The going-in cap rate is 5.2% and the mortgage costs 7.25%. Borrowing at 7.25% to buy a 5.2% yield is negative leverage — the debt makes the deal *worse*, not better. […] You'd need **$2,958 rent today** (+23%) just to break even on cash flow. […] Strip out appreciation and the IRR is **−4.3%**.
>
> **`rental-320k.xlsx`** — 8 sheets, live formulas, 0 failing checks, 6 warnings raised (all of them about the deal, not the model).

Then come the inputs that move it, the break-evens, and the assumptions it made for you to confirm.

## What comes back

**The answer first.** The number, the two or three inputs that move it most, the break-even where the conclusion flips, and the assumptions it made for you to confirm.

**A workbook you can hand to anyone.** Inputs in blue and formulas in black, one formula per row across every period, and no numbers buried inside formulas. Change an input and everything downstream follows, so the next question is a recalculation, not a rebuild.

**Proof that it ties.** A `Checks` sheet tests the model against itself: the balance sheet balances, sources equal uses, loans pay off, partner cash flows sum to the deal. Every check rolls up to one flag on the cover, and the analyst doesn't hand over a model whose checks fail. It recalculates and audits the workbook itself, even with no spreadsheet app installed, then ties the headline number out by a second route.

## What it covers today

| Area | Models |
|---|---|
| Valuation | DCF: WACC from CAPM, terminal value by growth and by exit multiple (each checked against the other), stub periods, the EV-to-equity bridge, implied IRR at the market price, live sensitivity grids. Trading and precedent-transaction comps: calendarized multiples, outlier switches, implied ranges, football field |
| Investment banking | LBOs: sources and uses, tranche-by-tranche cash sweep, revolver, PIK, credit stats, sponsor IRR and returns attribution. Merger models: cash/stock mix, purchase price allocation, synergies, EPS accretion/dilution and the breakeven price |
| Corporate finance | Three-statement forecasts: working capital on days, PP&E, a revolver that funds shortfalls, interest without circularity. Capital budgeting: incremental cash flows, tax on sale, NPV/IRR/MIRR, payback, replacement decisions, crossover rates. 13-week cash flows: direct-method receipts and disbursements, borrowing base, rolling variance, liquidity levers |
| Project finance | Solar, wind and infrastructure: construction funding, CFADS, debt sized and sculpted to a target DSCR, DSRA and maintenance reserves, lock-ups, LLCR/PLCR, project and equity IRR |
| Real estate | Ground-up development (construction loan with interest reserve, lease-up, yield on cost, sale or refi), GP/LP equity waterfalls with IRR hurdles and catch-up, single-family rentals (buy and hold, BRRRR, cash-out refi) and fix-and-flips |
| Scenarios | Base/upside/downside switches, live sensitivity grids, tornados and breakevens solved by formula, on any model |
| Model review | Audits of a model someone else built: hardcodes, broken rows, hidden circularity, checks that can't fail, graded findings and a verdict |

Coming next: multifamily and commercial acquisitions with a rent roll, 13-week cash flow, budgets and cap tables.

## License

[MIT](LICENSE). Contributing: see [CLAUDE.md](CLAUDE.md).

moolaski builds and explains models. It isn't investment advice: check the assumptions it lists before you rely on a number.
