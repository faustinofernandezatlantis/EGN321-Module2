import pytest
from src.units import kpa_to_psi, psi_to_kpa

def test_kpa_to_psi_known_value():
    assert kpa_to_psi(6.89476) == pytest.approx(1.0, rel=1e-5)

def test_pressure_round_trip():
    original_kpa = 101.325
    converted_psi = kpa_to_psi(original_kpa)
    restored_kpa = psi_to_kpa(converted_psi)
    assert restored_kpa == pytest.approx(original_kpa, rel=1e-5)