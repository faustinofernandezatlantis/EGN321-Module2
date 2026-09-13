"""
EGN 321 - Module 2 Assignment 2.2
Reusable Unit Conversion Module
"""

KPA_PER_PSI = 6.89476

def kpa_to_psi(kpa: float) -> float:
    """Convert pressure from kilopascals to pounds per square inch."""
    return kpa / KPA_PER_PSI

def psi_to_kpa(psi: float) -> float:
    """Convert pressure from pounds per square inch to kilopascals."""
    return psi * KPA_PER_PSI