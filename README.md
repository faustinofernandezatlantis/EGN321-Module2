# Pump Performance Validation Tool

## Purpose
This tool performs differential head, hydraulic power, brake horsepower, and flow margin calculations for centrifugal pump configurations. It replaces the legacy Excel workbook `PUMP_HEAD_rev6.xlsx` by implementing a validated, unit-safe calculation tool in Python.

## External Inputs

| Input Parameter | Variable Name | External Unit | Internal Canonical Unit |
|---|---|---|---|
| Suction Pressure | `suction_pressure_kpa` | kPa | psi |
| Discharge Pressure | `discharge_pressure_kpa` | kPa | psi |
| Flow Rate | `flow_rate_gpm` | gpm | gpm |
| Rated Flow Rate | `rated_flow_gpm` | gpm | gpm |
| Specific Gravity | `specific_gravity` | ratio | ratio |
| Pump Efficiency | `pump_efficiency_pct` | % | fraction |

## Unit Boundary
Unit conversion occurs strictly once at the entry point of the `calculate_pump_performance()` function using dedicated functions from `src/units.py`. Raw pressure values in kilopascals (kPa) are converted to pounds per square inch (psi) before any downstream calculations take place. Intermediate step calculations operate exclusively on canonical internal variables (`suction_pressure_psi`, `discharge_pressure_psi`), preventing duplicate conversion errors.

## Calculation Chain
1. **Suction Pressure Conversion (`suction_pressure_psi`):** Converts external suction pressure from kPa to psi ($\text{kPa} / 6.89476$).
2. **Discharge Pressure Conversion (`discharge_pressure_psi`):** Converts external discharge pressure from kPa to psi ($\text{kPa} / 6.89476$).
3. **Differential Pressure (`differential_pressure_psi`):** Calculates net pressure lift ($P_{\text{discharge}} - P_{\text{suction}}$).
4. **Total Dynamic Head (`pump_head_ft`):** Computes differential head in feet ($\Delta P \times 2.31 / \text{SG}$).
5. **Hydraulic Power (`hydraulic_hp`):** Computes water horsepower delivered to the fluid ($(Q \times H \times \text{SG}) / 3960$).
6. **Efficiency Fraction (`efficiency_fraction`):** Converts percentage efficiency to decimal fraction ($\text{pct} / 100$).
7. **Brake Horsepower (`brake_hp`):** Computes total shaft power required ($\text{hydraulic\_hp} / \text{efficiency\_fraction}$).
8. **Flow Margin (`flow_margin_gpm`):** Computes remaining flow capacity ($Q_{\text{rated}} - Q_{\text{actual}}$).

## Validation Rules

### Individual Rules
- `suction_pressure_kpa`: Must be greater than or equal to 0 kPa.
- `discharge_pressure_kpa`: Must be greater than or equal to 0 kPa.
- `flow_rate_gpm`: Must be strictly greater than 0 gpm.
- `rated_flow_gpm`: Must be strictly greater than 0 gpm.
- `specific_gravity`: Must be strictly greater than 0.
- `pump_efficiency_pct`: Must be strictly greater than 0% and less than or equal to 100%.

### Combination Rules
- **Discharge vs Suction:** `discharge_pressure_kpa` must be strictly greater than `suction_pressure_kpa`.
- **Requested vs Rated Flow:** `flow_rate_gpm` cannot exceed `rated_flow_gpm`.

## Supported Ranges
- **Pressures:** Non-negative gauge pressures ($\ge 0\text{ kPa}$).
- **Flow Rates:** Active positive flow up to the pump's rated capacity ($0 < Q \le Q_{\text{rated}}$).
- **Fluids:** Positive specific gravity ($> 0$).
- **Efficiency:** Standard real-world range ($0\% < \eta \le 100\%$).

## Rejection Behavior
The system raises a `ValueError` with clear descriptive messages:
- Individual failure: `ValueError: suction_pressure_kpa must be >= 0; received -10.0`
- Combination failure (pressure): `ValueError: discharge_pressure_kpa (100.0) must be greater than suction_pressure_kpa (150.0)`
- Combination failure (capacity): `ValueError: flow_rate_gpm (200.0) cannot exceed rated_flow_gpm (180.0)`

## Verification
Calculations are verified against reference cases from `PUMP_HEAD_rev6.xlsx`:
- **RC-1:** 110 kPa suction, 420 kPa discharge, 145 gpm flow, 180 gpm rated, 1.0 SG, 72% efficiency $\rightarrow$ Head: $103.86\text{ ft}$, BHP: $5.28\text{ hp}$.
- **RC-2:** 95 kPa suction, 360 kPa discharge, 120 gpm flow, 160 gpm rated, 0.92 SG, 75% efficiency $\rightarrow$ Head: $96.51\text{ ft}$, BHP: $3.59\text{ hp}$.
- **RC-3:** 150 kPa suction, 510 kPa discharge, 150 gpm flow, 190 gpm rated, 1.1 SG, 68% efficiency $\rightarrow$ Head: $109.65\text{ ft}$, BHP: $6.72\text{ hp}$.

## Running the Tests

```bash
pytest