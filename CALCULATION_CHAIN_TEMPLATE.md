```markdown
# Calculation Chain Map

| Step | Input / Quantity | External Unit | Operation | Output Variable | Internal Unit | Testable Separately? |
|---|---|---|---|---|---|---|
| 1 | Suction Pressure | kPa | `kpa_to_psi(suction_kpa)` | `suction_pressure_psi` | psi | Yes |
| 2 | Discharge Pressure | kPa | `kpa_to_psi(discharge_kpa)` | `discharge_pressure_psi` | psi | Yes |
| 3 | Differential Pressure | — | `discharge_psi - suction_psi` | `differential_pressure_psi` | psi | Yes |
| 4 | Total Dynamic Head | — | `(diff_psi * 2.31) / sg` | `pump_head_ft` | ft | Yes |
| 5 | Hydraulic Horsepower | — | `(flow * head * sg) / 3960` | `hydraulic_hp` | hp | Yes |
| 6 | Efficiency Fraction | % | `eff_pct / 100` | `efficiency_fraction` | ratio | Yes |
| 7 | Brake Horsepower | — | `hydraulic_hp / efficiency_fraction` | `brake_hp` | hp | Yes |
| 8 | Flow Margin | gpm | `rated_gpm - flow_gpm` | `flow_margin_gpm` | gpm | Yes |

## Unit Boundary
External units enter the Python program through arguments passed to `calculate_pump_performance()`.

## Conversion Point
`suction_pressure_kpa` and `discharge_pressure_kpa` are converted exactly once at the top of `calculate_pump_performance()` into `suction_pressure_psi` and `discharge_pressure_psi`.

## Duplicate-Conversion Risk
Duplicate conversion is avoided by using distinct variable names that explicitly contain the unit suffix (`_kpa` vs `_psi`) and ensuring downstream calculation steps use only `_psi` variables.

## Final Output
The function returns a dictionary containing all named intermediate and final performance values (`suction_pressure_psi`, `discharge_pressure_psi`, `differential_pressure_psi`, `pump_head_ft`, `hydraulic_hp`, `efficiency_fraction`, `brake_hp`, `flow_margin_gpm`).