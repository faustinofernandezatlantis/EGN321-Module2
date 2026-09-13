# EGN 321 - Module 2 Assignment 2.1: Unit Conversion Module

## Overview
This repository contains a reusable Python unit conversion library (`units.py`) built for EGN 321. The module establishes a clean boundary layer for unit conversions, ensuring that internal calculations maintain a single, consistent unit state throughout multi-step engineering pipelines.

## Project Structure
```text
.
├── units.py        # Core conversion functions and constants
├── test_units.py   # Unit test suite using pytest
├── AI_LOG.md       # AI usage documentation
└── README.md       # Project documentation

Implemented Conversions

Length
inches_to_feet(inches) / feet_to_inches(feet)

Converts between inches and feet.

Constant: INCHES_PER_FOOT = 12.0

Volume
cubic_feet_to_gallons(cubic_feet) / gallons_to_cubic_feet(gallons)

Converts between cubic feet and US liquid gallons.

Constant: GALLONS_PER_CUBIC_FOOT = 7.48052

Pressure
kpa_to_psi(kpa) / psi_to_kpa(psi)

Converts between kilopascals (kPa) and pounds per square inch (psi).

Constant: PSI_PER_KPA = 0.14503773773020923

Design Principles Applied
Explicit Naming: Every function name clearly indicates source and target units (source_to_target).

Boundary Conversions: Conversions are kept separate from engineering calculations and input validation.

Named Constants: All physical factors are stored in uppercase named constants to avoid magic numbers.

Focused Responsibilities: Each function performs a single mathematical conversion without embedded business rules.

Running Tests
To run the automated test suite, ensure pytest is installed and execute:

python -m pytest

Test Coverage Summary

The test suite in test_units.py contains 10 automated tests covering:

Known-value conversions: Verifies conversions against standard engineering constants.

Reverse conversions: Validates inverse functionality.

Round-trip tests: Confirms that converting back and forth preserves original values.

Zero-value tests: Confirms mathematical behavior at zero.