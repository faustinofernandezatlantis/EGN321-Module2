# Validation Matrix

| Scenario | Inputs | Individually Valid? | Combination Valid? | Expected Behavior | Error Message / Result |
|---|---|---|---|---|---|
| Normal | S=110, D=420, Q=145, Qr=180, SG=1, Eff=72 | Yes | Yes | Calculate | Head: 103.86 ft, BHP: 5.28 hp |
| Invalid suction pressure | S=-10, D=420, Q=145, Qr=180, SG=1, Eff=72 | No | No | Reject | `ValueError: suction_pressure_kpa must be >= 0` |
| Invalid flow | S=110, D=420, Q=0, Qr=180, SG=1, Eff=72 | No | No | Reject | `ValueError: flow_rate_gpm must be > 0` |
| Discharge <= suction | S=200, D=150, Q=145, Qr=180, SG=1, Eff=72 | Yes | No | Reject combination | `ValueError: discharge_pressure_kpa must be greater than suction_pressure_kpa` |
| Requested flow > rated flow | S=110, D=420, Q=200, Qr=180, SG=1, Eff=72 | Yes | No | Reject combination | `ValueError: flow_rate_gpm cannot exceed rated_flow_gpm` |
| Boundary case | S=0, D=100, Q=180, Qr=180, SG=1, Eff=100 | Yes | Yes | Calculate | Valid (Flow margin = 0 gpm) |

## Rule Notes
- **Suction/Discharge $\ge 0$ kPa:** Protects against unsupported gauge pressure conditions in the current simplified fluid model.
- **Flow / Rated Flow $> 0$ gpm:** Prevents non-physical negative flow and division-by-zero errors.
- **Specific Gravity $> 0$:** Prevents division by zero in the differential head equation.
- **Efficiency $0 < \eta \le 100\%$:** Enforces physical conservation of energy limits.
- **Discharge > Suction:** Enforces energy input requirement by the pump (pump adds pressure to fluid).
- **Requested Flow $\le$ Rated Flow:** Enforces physical equipment operating capacity limits.