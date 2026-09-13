import pytest
from src.calculation import calculate_pump_performance

def test_reference_case_1():
    # Case 1: Standard operating parameters
    result = calculate_pump_performance(
        suction_pressure_kpa=100.0,
        discharge_pressure_kpa=400.0,
        flow_rate_gpm=100.0,
        rated_flow_gpm=150.0,
        specific_gravity=1.0,
        pump_efficiency_pct=75.0
    )
    
    # Expected calculations:
    # diff_psi = (400 - 100) / 6.89476 = 43.5113 psi
    # head_ft = 43.5113 * 2.31 / 1.0 = 100.5111 ft
    # hyd_hp = (100 * 100.5111 * 1.0) / 3960 = 2.5381 hp
    # brake_hp = 2.5381 / 0.75 = 3.3842 hp
    assert result["differential_pressure_psi"] == pytest.approx(43.5113, rel=1e-3)
    assert result["pump_head_ft"] == pytest.approx(100.5111, rel=1e-3)
    assert result["brake_hp"] == pytest.approx(3.3842, rel=1e-3)
    assert result["flow_margin_gpm"] == 50.0

def test_reference_case_2():
    # Case 2: High density fluid operating condition
    result = calculate_pump_performance(
        suction_pressure_kpa=150.0,
        discharge_pressure_kpa=500.0,
        flow_rate_gpm=120.0,
        rated_flow_gpm=120.0,
        specific_gravity=1.2,
        pump_efficiency_pct=80.0
    )
    assert result["differential_pressure_psi"] == pytest.approx(50.7632, rel=1e-3)
    assert result["pump_head_ft"] == pytest.approx(97.7191, rel=1e-3)
    assert result["flow_margin_gpm"] == 0.0

def test_unit_boundary_integration():
    # Verify kPa -> psi conversion integration end-to-end
    result = calculate_pump_performance(
        suction_pressure_kpa=0.0,
        discharge_pressure_kpa=68.9476,
        flow_rate_gpm=100.0,
        rated_flow_gpm=100.0,
        specific_gravity=1.0,
        pump_efficiency_pct=100.0
    )
    assert result["differential_pressure_psi"] == pytest.approx(10.0, rel=1e-4)
    assert result["pump_head_ft"] == pytest.approx(23.1, rel=1e-4)

def test_boundary_case():
    # Boundary: Max efficiency (100%) and zero margin
    result = calculate_pump_performance(
        suction_pressure_kpa=100.0,
        discharge_pressure_kpa=200.0,
        flow_rate_gpm=150.0,
        rated_flow_gpm=150.0,
        specific_gravity=1.0,
        pump_efficiency_pct=100.0
    )
    assert result["efficiency_fraction"] == 1.0
    assert result["hydraulic_hp"] == pytest.approx(result["brake_hp"], rel=1e-5)