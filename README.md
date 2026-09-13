# EGN 321 - Module 2 Assignment 2.1: Unit Conversion Module

## Overview
This repository contains a reusable Python unit conversion library (`units.py`) built for EGN 321. The module establishes a clean boundary layer for unit conversions, ensuring that internal calculations maintain a single, consistent unit state throughout engineering workflows.

All conversion factors and test cases are verified against `UNIT_CONVERSIONS_reference.xlsx`.

## Project Structure
```text
.
├── units.py        # Core conversion functions and named constants
├── test_units.py   # Automated test suite (T01-T14 reference data)
├── AI_LOG.md       # AI usage log
└── README.md       # Documentation

Implemented Conversions
Length
inches_to_feet(inches) / feet_to_inches(feet) (1 ft = 12 in)

Volume
cubic_feet_to_gallons(cubic_feet) / gallons_to_cubic_feet(gallons) (1 ft³ ≈ 7.48052 US gal)

Pressure
kpa_to_psi(kpa) / psi_to_kpa(psi) (1 psi ≈ 6.89476 kPa)

Temperature
fahrenheit_to_celsius(fahrenheit) / celsius_to_fahrenheit(celsius)

Flow
gpm_to_lpm(gpm) / lpm_to_gpm(lpm) (1 US gal ≈ 3.785411784 L)

Running Tests
To execute the test suite:

Bash
python -m pytest