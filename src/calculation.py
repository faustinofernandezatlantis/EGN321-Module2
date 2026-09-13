"""
EGN 321 - Module 2 Assignment 2.2
Validated Multi-Step Pump Calculation
"""

from typing import Dict
from src.units import kpa_to_psi
from src.validation import validate_pump_inputs

FT_HEAD_PER_PSI_WATER = 2.31
HP_CONSTANT = 3960.0

def calculate_pump_performance(
    suction_pressure_kpa: float,
    discharge_pressure_kpa: float,
    flow_rate_gpm: float,
    rated_flow_gpm: float,
    specific_gravity: float,
    pump_efficiency_pct: float
) -> Dict[str, float]:
    """
    Executes validated pump calculations using canonical internal units.
    Converts units once at the input boundary.
    """
    # 1. Validation step
    validate_pump_inputs(
        suction_pressure_kpa=suction_pressure_kpa,
        discharge_pressure_kpa=discharge_pressure_kpa,
        flow_rate_gpm=flow_rate_gpm,
        rated_flow_gpm=rated_flow_gpm,
        specific_gravity=specific_gravity,
        pump_efficiency_pct=pump_efficiency_pct
    )

    # 2. Boundary Conversion (once only)
    suction_pressure_psi = kpa_to_psi(suction_pressure_kpa)
    discharge_pressure_psi = kpa_to_psi(discharge_pressure_kpa)

    # 3. Intermediate Calculations using Canonical Internal Units
    differential_pressure_psi = discharge_pressure_psi - suction_pressure_psi
    pump_head_ft = (differential_pressure_psi * FT_HEAD_PER_PSI_WATER) / specific_gravity
    hydraulic_hp = (flow_rate_gpm * pump_head_ft * specific_gravity) / HP_CONSTANT
    efficiency_fraction = pump_efficiency_pct / 100.0
    brake_hp = hydraulic_hp / efficiency_fraction
    flow_margin_gpm = rated_flow_gpm - flow_rate_gpm

    # 4. Return Structured Intermediate and Final Quantities
    return {
        "suction_pressure_psi": suction_pressure_psi,
        "discharge_pressure_psi": discharge_pressure_psi,
        "differential_pressure_psi": differential_pressure_psi,
        "pump_head_ft": pump_head_ft,
        "hydraulic_hp": hydraulic_hp,
        "efficiency_fraction": efficiency_fraction,
        "brake_hp": brake_hp,
        "flow_margin_gpm": flow_margin_gpm
    }