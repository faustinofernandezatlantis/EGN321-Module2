"""
EGN 321 - Module 2 Assignment 2.2
Validation Layer for Pump Calculations
"""

def validate_pump_inputs(
    suction_pressure_kpa: float,
    discharge_pressure_kpa: float,
    flow_rate_gpm: float,
    rated_flow_gpm: float,
    specific_gravity: float,
    pump_efficiency_pct: float
) -> None:
    """
    Validates individual pump parameters and relational combinations.
    Raises ValueError with descriptive context on failure.
    """
    # Individual Boundary Validations
    if suction_pressure_kpa < 0:
        raise ValueError(
            f"suction_pressure_kpa must be >= 0; received {suction_pressure_kpa}"
        )
    if discharge_pressure_kpa < 0:
        raise ValueError(
            f"discharge_pressure_kpa must be >= 0; received {discharge_pressure_kpa}"
        )
    if flow_rate_gpm <= 0:
        raise ValueError(
            f"flow_rate_gpm must be > 0; received {flow_rate_gpm}"
        )
    if rated_flow_gpm <= 0:
        raise ValueError(
            f"rated_flow_gpm must be > 0; received {rated_flow_gpm}"
        )
    if specific_gravity <= 0:
        raise ValueError(
            f"specific_gravity must be > 0; received {specific_gravity}"
        )
    if pump_efficiency_pct <= 0 or pump_efficiency_pct > 100:
        raise ValueError(
            f"pump_efficiency_pct must be in (0, 100]; received {pump_efficiency_pct}"
        )

    # Relational / Combination Validations
    if discharge_pressure_kpa <= suction_pressure_kpa:
        raise ValueError(
            f"discharge_pressure_kpa ({discharge_pressure_kpa}) must be greater than "
            f"suction_pressure_kpa ({suction_pressure_kpa})"
        )
    if flow_rate_gpm > rated_flow_gpm:
        raise ValueError(
            f"flow_rate_gpm ({flow_rate_gpm}) cannot exceed "
            f"rated_flow_gpm ({rated_flow_gpm})"
        )