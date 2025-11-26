"""
Utility functions for signage analysis.
"""


def inches_to_feet(inches: float) -> float:
    """Convert inches to feet."""
    return inches / 12.0


def feet_to_inches(feet: float) -> float:
    """Convert feet to inches."""
    return feet * 12.0


def sqin_to_sqft(square_inches: float) -> float:
    """Convert square inches to square feet."""
    return square_inches / 144.0


def sqft_to_sqin(square_feet: float) -> float:
    """Convert square feet to square inches."""
    return square_feet * 144.0


def format_currency(amount: float) -> str:
    """Format a number as currency."""
    return f"${amount:,.2f}"


def format_area(area_sqft: float) -> str:
    """Format area with appropriate units."""
    if area_sqft < 1:
        return f"{area_sqft * 144:.2f} sq in"
    return f"{area_sqft:.2f} sq ft"
