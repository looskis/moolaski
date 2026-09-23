---
name: ib-dcf
description: Builds a discounted cash flow valuation in Excel on top of a forecast — unlevered free cash flow, WACC from CAPM, terminal value by perpetuity growth and by exit multiple with each cross-checked against the other, mid-year discounting, the enterprise-to-equity bridge, value per share, and live sensitivity grids. Use when the user asks for a "DCF", "unlevered free cash flow", "FCFF", "WACC", "terminal value", "intrinsic value", "what's this company worth", "EV to equity bridge", or a football-field input. Not for building the underlying forecast (use cf-three-statement) and not for LBO returns.
---

# Discounted cash flow

Values a business as the cash it can hand to all its capital providers, discounted at their blended required return. The arithmetic is easy; almost every wrong DCF is wrong for one of three reasons: the cash flow doesn't match the discount rate, the terminal value is never sanity-checked, or the bridge from enterprise value to per-share value quietly drops something.

## Before you build

- You need a forecast: EBIT, D&A, capex and the change in net working capital for each year (see `cf-three-statement`).
- Gather: risk-free rate, beta, equity risk premium, target capital structure, pre-tax cost of debt, tax rate, horizon, terminal growth and/or exit multiple, and the valuation date.
- For the bridge: debt, cash, and diluted share count at the valuation date, plus any minority interest, associates, pensions or preferred stock.
- Follow `fm-model-conventions`, `fm-time-series` and `fm-returns-metrics`.

## Build steps

1. **Unlevered free cash flow**: `EBIT × (1 − tax) + D&A − capex − increase in NWC`. Tax is on EBIT, not on profit before tax: the interest deduction belongs in the discount rate, not the cash flow. Never let interest, debt draws or dividends into this row.
2. **WACC**: cost of equity = risk-free + beta × ERP; after-tax cost of debt = pre-tax × (1 − tax); weight them by **target** capital structure, which keeps the discount rate independent of this year's balance sheet and out of any circular loop.
3. **Discounting**: exponent = year − 0.5 with mid-year convention, else year. Put the exponent on the timing sheet as its own row, so every discounting formula — including sensitivities — reads from one place.
4. **Terminal value, both ways, always**:
   - perpetuity growth: `UFCF(N) × (1 + g) / (WACC − g)`
   - exit multiple: `EBITDA(N) × multiple`
   One switch picks which drives the answer. Show the other alongside, plus the **implied** counterpart: the exit multiple implied by your growth rate, and the growth implied by your multiple. If the implied figures are absurd, the assumption is absurd.
   Discount the terminal value at the end of year N even under mid-year convention, unless you have a reason to do otherwise, and say which you used.
5. **Bridge**: enterprise value = PV(forecast) + PV(terminal). Equity value = EV − debt + cash − minority interest − preferred + associates. Value per share = equity / diluted shares. List every bridge item, even when zero, so nothing is silently missing.
6. **Sensitivities**: a WACC × growth grid and a WACC × multiple grid. Build them as formulas that rediscount the UFCF row — `SUMPRODUCT(UFCF, forecast flag, (1 + w)^−exponent)` plus the discounted terminal value at that cell's inputs. They then survive a rebuild, work without Excel's what-if tables, and can be checked: **the centre cell must equal the model's own value per share.** Make that a check.

## Checks

- Centre of each sensitivity grid = the DCF's value per share.
- WACC > terminal growth (otherwise the perpetuity is meaningless).
- EV = PV(forecast) + PV(terminal), and the equity bridge ties.
- Forecast horizon fits the grid.
- Warnings: terminal value above ~75–80% of EV; implied exit multiple or implied growth outside a sane band; terminal-year ROIC below WACC while growth is positive, which values growth that destroys value.

## Common mistakes

- Taxing EBT instead of EBIT, so the interest shield is counted twice: once in the cash flow and again in the WACC.
- Levered free cash flow discounted at WACC, or unlevered discounted at the cost of equity.
- A terminal growth rate above long-run GDP growth, or above WACC, which produces a finite-looking number from a divergent series.
- Mid-year discounting applied to the explicit period but silently not to the terminal value, or vice versa.
- A bridge that forgets minority interest, preferred stock or leases, or that uses a basic rather than diluted share count.
- Discount rate built from the current capital structure, which moves as the model's debt moves and can loop.
- Sensitivity tables pasted as values, which go stale the moment a driver changes.
- Terminal value at 90% of enterprise value, treated as a result rather than a warning that the horizon is too short.

## References

- [references/mechanics.md](references/mechanics.md) — formulas for UFCF, WACC, discount factors, both terminal values and their implied counterparts, the bridge, and sensitivity cells
