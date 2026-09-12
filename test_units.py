import pytest
from units import (
    inches_to_feet,
    feet_to_inches,
    cubic_feet_to_gallons,
    gallons_to_cubic_feet,
    kpa_to_psi,
    psi_to_kpa,
)

# 1. Known-value tests

def test_inches_to_feet_known():
    assert inches_to_feet(12.0) == pytest.approx(1.0)

def test_inches_to_feet_three_feet():
    assert inches_to_feet(36.0) == pytest.approx(3.0)

def test_cubic_feet_to_gallons_known():
    assert cubic_feet_to_gallons(1.0) == pytest.approx(7.48052)

def test_kpa_to_psi_known():
    # Class reference value: 110 kPa is approximately 15.954 psi
    assert kpa_to_psi(110.0) == pytest.approx(15.95415, abs=1e-3)


# 2. Reverse conversion tests

def test_feet_to_inches_known():
    assert feet_to_inches(2.0) == pytest.approx(24.0)

def test_gallons_to_cubic_feet_known():
    assert gallons_to_cubic_feet(7.48052) == pytest.approx(1.0)

def test_psi_to_kpa_known():
    assert psi_to_kpa(15.95415) == pytest.approx(110.0, abs=1e-3)


# 3. Round-trip tests

def test_inches_round_trip():
    original = 36.0
    feet = inches_to_feet(original)
    result = feet_to_inches(feet)
    assert result == pytest.approx(original)

def test_kpa_psi_round_trip():
    original = 420.0
    psi = kpa_to_psi(original)
    result = psi_to_kpa(psi)
    assert result == pytest.approx(original)


# 4. Zero-value tests

def test_zero_conversions():
    assert inches_to_feet(0.0) == pytest.approx(0.0)
    assert kpa_to_psi(0.0) == pytest.approx(0.0)