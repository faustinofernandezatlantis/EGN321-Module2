# Assignment 2.2 Test Plan

| Test Name | Category | Inputs | Expected Result | Evidence Source | Why It Matters |
|---|---|---|---|---|---|
| `test_reference_case_1` | Known-correct | S=110, D=420, Q=145, Qr=180, SG=1, Eff=72 | Head $\approx 103.86$, BHP $\approx 5.28$ | Workbook Reference Cases | Confirms agreement with Excel legacy tool. |
| `test_reference_case_2` | Known-correct | S=95, D=360, Q=120, Qr=160, SG=0.92, Eff=75 | Head $\approx 96.51$, BHP $\approx 3.59$ | Workbook Reference Cases | Verifies calculation with varying SG and efficiency. |
| `test_negative_suction_pressure_rejected` | Individual rejection | S=-10, D=420, Q=145, Qr=180, SG=1, Eff=72 | `ValueError` | Operating Limits | Prevents unsupported negative pressure inputs. |
| `test_zero_flow_rejected` | Individual rejection | S=110, D=420, Q=0, Qr=180, SG=1, Eff=72 | `ValueError` | Operating Limits | Prevents non-physical zero flow calculations. |
| `test_discharge_not_above_suction_rejected` | Combination rejection | S=200, D=150, Q=145, Qr=180, SG=1, Eff=72 | `ValueError` | Operating Limits | Enforces positive net pressure generation requirement. |
| `test_boundary_case` | Boundary | S=0, D=100, Q=180, Qr=180, SG=1, Eff=100 | Hydraulic HP == Brake HP | Operating Limits | Tests model behavior at maximum capacity limits. |
| `test_unit_boundary_integration` | Unit integration | S=0, D=68.9476, Q=100, Qr=100, SG=1, Eff=100 | Diff $\text{psi} = 10.0$, Head $\approx 23.1\text{ ft}$ | Calculation chain | Validates unit conversion correctness. |

## Minimum New Tests
- 2 known-correct calculation tests
- 2 individual rejection tests
- 1 combination rejection test
- 1 boundary test
- 1 unit/conversion integration test