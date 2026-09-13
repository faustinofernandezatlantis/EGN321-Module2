import pytest
from src.validation import validate_pump_inputs

def test_negative_suction_pressure_rejected():
    with pytest.raises(ValueError, match="suction_pressure_kpa must be >= 0"):
        validate_pump_inputs(
            suction_pressure_kpa=-10.0,
            discharge_pressure_kpa=400.0,
            flow_rate_gpm=100.0,
            rated_flow_gpm=150.0,
            specific_gravity=1.0,
            pump_efficiency_pct=75.0
        )

def test_zero_flow_rejected():
    with pytest.raises(ValueError, match="flow_rate_gpm must be > 0"):
        validate_pump_inputs(
            suction_pressure_kpa=100.0,
            discharge_pressure_kpa=400.0,
            flow_rate_gpm=0.0,
            rated_flow_gpm=150.0,
            specific_gravity=1.0,
            pump_efficiency_pct=75.0
        )

def test_discharge_not_above_suction_rejected():
    with pytest.raises(ValueError, match="discharge_pressure_kpa .* must be greater than"):
        validate_pump_inputs(
            suction_pressure_kpa=200.0,
            discharge_pressure_kpa=150.0,
            flow_rate_gpm=100.0,
            rated_flow_gpm=150.0,
            specific_gravity=1.0,
            pump_efficiency_pct=75.0
        )

def test_requested_flow_above_rating_rejected():
    with pytest.raises(ValueError, match="cannot exceed"):
        validate_pump_inputs(
            suction_pressure_kpa=100.0,
            discharge_pressure_kpa=400.0,
            flow_rate_gpm=180.0,
            rated_flow_gpm=150.0,
            specific_gravity=1.0,
            pump_efficiency_pct=75.0
        )