# DCF mechanics

Notation: `N` = forecast horizon in years, `w` = WACC, `g` = terminal growth, `[flag]` = a 1/0 row on the timing sheet. Year 0 is the valuation date and carries no cash flow.

## Unlevered free cash flow

| Row | Formula |
|---|---|
| EBIT | from the forecast × `[forecast]` |
| Tax on EBIT | `−tax rate × MAX(0, EBIT)` |
| NOPAT | `EBIT + tax on EBIT` |
| plus D&A | from the forecast |
| less capex | `−capex` |
| less increase in NWC | `−(NWC − prior NWC)` |
| **UFCF** | sum of the above |

A loss-making year gets no tax benefit unless you model NOLs; `MAX(0, …)` states that choice explicitly.

## Discount rate and factors

| Item | Formula |
|---|---|
| Cost of equity | `rf + β × ERP` (add a size or country premium as its own input if used) |
| After-tax cost of debt | `pre-tax rate × (1 − tax rate)` |
| WACC | `(1 − Wd) × cost of equity + Wd × after-tax cost of debt`, `Wd` = target debt weight |
| Discount exponent | `[forecast] × (year − 0.5 × mid-year switch)` |
| Discount factor | `[forecast] × (1 + w)^−exponent` |
| PV of forecast | `SUM(UFCF × discount factor)` |

To relever a beta from comparables: `βL = βU × (1 + (1 − tax) × D/E)`. Keep `βU` and the target `D/E` as inputs, not buried in the formula.

## Terminal value

| Item | Formula |
|---|---|
| Perpetuity growth | `UFCF(N) × (1 + g) / (w − g)`, guarded by `IF(w <= g, 0, …)` |
| Exit multiple | `EBITDA(N) × multiple` |
| Terminal discount factor | `(1 + w)^−N` |
| PV of terminal value | `TV × terminal discount factor` |
| Implied exit multiple | `TV / EBITDA(N)` |
| Implied growth | `(TV × w − UFCF(N)) / (TV + UFCF(N))` |
| TV share of EV | `PV(TV) / EV` |

`UFCF(N)` and `EBITDA(N)` come from `INDEX(row, 1, N + 1)` when year 0 sits in the first column — that way the horizon stays an input rather than a hardcoded column.

The implied-growth formula is the perpetuity rearranged; it tells you what growth an exit multiple is really assuming.

## Bridge

| Item | Sign |
|---|---|
| Enterprise value | `PV(forecast) + PV(terminal)` |
| Less debt (all drawn facilities, plus leases if capitalized) | − |
| Plus cash and equivalents (less any restricted or operating cash) | + |
| Less minority interest, preferred stock, unfunded pensions | − |
| Plus associates and investments | + |
| **Equity value** | |
| Value per share | `equity / diluted shares` |

Use balances at the valuation date, which is year 0 — `INDEX(row, 1, 1)` — not the terminal year.

## Sensitivity cell

For WACC `w` down the rows and growth `g` across the columns:

```
=IF(w <= g, "n/a",
    (SUMPRODUCT(UFCF_row, forecast_flag_row, (1 + w)^-exponent_row)
     + INDEX(UFCF_row, 1, N + 1) * (1 + g) / (w - g) * (1 + w)^-N
     - net debt) / shares)
```

For an exit-multiple grid, replace the terminal term with `INDEX(EBITDA_row, 1, N + 1) * multiple * (1 + w)^-N`.

`SUMPRODUCT` with `(1 + w)^−exponent_row` discounts the whole row elementwise, which is what makes each cell a real recomputation. The centre cell should reproduce the model's own value per share exactly; check it.
