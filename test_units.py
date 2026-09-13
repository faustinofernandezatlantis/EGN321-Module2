import pytest
from units import (
    inches_to_feet,
    feet_to_inches,
    cubic_feet_to_gallons,
    gallons_to_cubic_feet,
    kpa_to_psi,
    psi_to_kpa,
    fahrenheit_to_celsius,
    celsius_to_fahrenheit,
    gpm_to_lpm,
    lpm_to_gpm,
)

# --- Length Tests ---

def test_t01_inches_to_feet_known():
    assert inches_to_feet(12) == pytest.approx(1.0)

def test_t02_inches_to_feet_normal():
    assert inches_to_feet(36) == pytest.approx(3.0)

def test_t03_feet_to_inches_non_integer():
    assert feet_to_inches(2.5) == pytest.approx(30.0)

def test_t04_feet_to_inches_zero():
    assert feet_to_inches(0) == pytest.approx(0.0)


# --- Volume Tests ---

def test_t05_cubic_feet_to_gallons_known():
    assert cubic_feet_to_gallons(1) == pytest.approx(7.48052)

def test_t06_gallons_to_cubic_feet_reverse():
    assert gallons_to_cubic_feet(7.48052) == pytest.approx(1.0)


# --- Pressure Tests ---

def test_t07_kpa_to_psi_known():
    assert kpa_to_psi(6.89476) == pytest.approx(1.0)

def test_t08_kpa_to_psi_realistic():
    assert kpa_to_psi(100) == pytest.approx(14.503768, rel=1e-5)

def test_t09_psi_to_kpa_reverse():
    assert psi_to_kpa(50) == pytest.approx(344.738, rel=1e-5)


# --- Temperature Tests ---

def test_t10_fahrenheit_to_celsius_freezing():
    assert fahrenheit_to_celsius(32) == pytest.approx(0.0)

def test_t11_fahrenheit_to_celsius_boiling():
    assert fahrenheit_to_celsius(212) == pytest.approx(100.0)

def test_t12_celsius_to_fahrenheit_ambient():
    assert celsius_to_fahrenheit(25) == pytest.approx(77.0)


# --- Flow Tests ---

def test_t13_gpm_to_lpm_known():
    assert gpm_to_lpm(1) == pytest.approx(3.785412, rel=1e-5)

def test_t14_lpm_to_gpm_reverse():
    assert lpm_to_gpm(3.785412) == pytest.approx(1.0, rel=1e-5)


# --- Additional Round-Trip Tests ---

def test_pressure_round_trip():
    original = 420.0
    psi = kpa_to_psi(original)
    result = psi_to_kpa(psi)
    assert result == pytest.approx(original)

def test_temperature_round_trip():
    original = 98.6
    celsius = fahrenheit_to_celsius(original)
    result = celsius_to_fahrenheit(celsius)
    assert result == pytest.approx(original)