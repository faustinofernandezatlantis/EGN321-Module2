"""
units.py

Reusable unit conversion module for EGN 321.
Applies the principle of converting at the boundary and maintaining
an explicit, consistent internal unit system.
"""

# Named Constants
INCHES_PER_FOOT = 12.0
GALLONS_PER_CUBIC_FOOT = 7.48052
PSI_PER_KPA = 0.14503773773020923


def inches_to_feet(inches: float) -> float:
    """
    Convert length from inches to feet.

    Parameters
    ----------
    inches : float
        Length in inches.

    Returns
    -------
    float
        Equivalent length in feet.
    """
    return inches / INCHES_PER_FOOT


def feet_to_inches(feet: float) -> float:
    """
    Convert length from feet to inches.

    Parameters
    ----------
    feet : float
        Length in feet.

    Returns
    -------
    float
        Equivalent length in inches.
    """
    return feet * INCHES_PER_FOOT


def cubic_feet_to_gallons(cubic_feet: float) -> float:
    """
    Convert volume from cubic feet to gallons.

    Parameters
    ----------
    cubic_feet : float
        Volume in cubic feet.

    Returns
    -------
    float
        Equivalent volume in gallons.
    """
    return cubic_feet * GALLONS_PER_CUBIC_FOOT


def gallons_to_cubic_feet(gallons: float) -> float:
    """
    Convert volume from gallons to cubic feet.

    Parameters
    ----------
    gallons : float
        Volume in gallons.

    Returns
    -------
    float
        Equivalent volume in cubic feet.
    """
    return gallons / GALLONS_PER_CUBIC_FOOT


def kpa_to_psi(kpa: float) -> float:
    """
    Convert pressure from kilopascals (kPa) to pounds per square inch (psi).

    Parameters
    ----------
    kpa : float
        Pressure in kPa.

    Returns
    -------
    float
        Equivalent pressure in psi.
    """
    return kpa * PSI_PER_KPA


def psi_to_kpa(psi: float) -> float:
    """
    Convert pressure from pounds per square inch (psi) to kilopascals (kPa).

    Parameters
    ----------
    psi : float
        Pressure in psi.

    Returns
    -------
    float
        Equivalent pressure in kPa.
    """
    return psi / PSI_PER_KPA