"""
Data models for acrylic composition calculations.
Similar to eCut plugin functionality for liquid acrylic solutions.
"""

from dataclasses import dataclass, field
from typing import Optional, Dict


@dataclass
class AcrylicFormula:
    """
    Represents a liquid acrylic solution formula with component ratios.

    Standard formulas for signage work typically consist of:
    - Thinner: Controls viscosity and drying time
    - Glue (Binder): Provides adhesion and film formation
    - Color (Pigment): Provides color and opacity
    """

    name: str
    thinner_ratio: float  # Percentage (0-100)
    glue_ratio: float     # Percentage (0-100)
    color_ratio: float    # Percentage (0-100)
    coverage_ml_per_sqft: float = 30.0  # ml of solution per square foot
    description: str = ""

    def __post_init__(self):
        """Validate formula ratios."""
        total = self.thinner_ratio + self.glue_ratio + self.color_ratio
        if abs(total - 100.0) > 0.01:
            raise ValueError(
                f"Component ratios must sum to 100%. "
                f"Current total: {total:.2f}% "
                f"(thinner: {self.thinner_ratio}%, glue: {self.glue_ratio}%, color: {self.color_ratio}%)"
            )

        if self.thinner_ratio < 0 or self.glue_ratio < 0 or self.color_ratio < 0:
            raise ValueError("All component ratios must be non-negative")

        if self.coverage_ml_per_sqft <= 0:
            raise ValueError("Coverage rate must be positive")

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "thinner_ratio": self.thinner_ratio,
            "glue_ratio": self.glue_ratio,
            "color_ratio": self.color_ratio,
            "coverage_ml_per_sqft": self.coverage_ml_per_sqft,
            "description": self.description
        }


@dataclass
class AcrylicComposition:
    """Represents the calculated composition of acrylic solution."""

    formula_name: str
    surface_area_sqft: float
    total_solution_ml: float
    thinner_ml: float
    glue_ml: float
    color_ml: float
    num_coats: int
    waste_factor: float

    # Converted to liters for convenience
    @property
    def total_solution_liters(self) -> float:
        return self.total_solution_ml / 1000.0

    @property
    def thinner_liters(self) -> float:
        return self.thinner_ml / 1000.0

    @property
    def glue_liters(self) -> float:
        return self.glue_ml / 1000.0

    @property
    def color_liters(self) -> float:
        return self.color_ml / 1000.0

    def to_dict(self) -> Dict:
        """Convert to dictionary for easy display."""
        return {
            "formula_name": self.formula_name,
            "surface_area_sqft": round(self.surface_area_sqft, 2),
            "num_coats": self.num_coats,
            "waste_factor": round(self.waste_factor, 2),
            "composition": {
                "total_solution": {
                    "ml": round(self.total_solution_ml, 2),
                    "liters": round(self.total_solution_liters, 3)
                },
                "thinner": {
                    "ml": round(self.thinner_ml, 2),
                    "liters": round(self.thinner_liters, 3)
                },
                "glue": {
                    "ml": round(self.glue_ml, 2),
                    "liters": round(self.glue_liters, 3)
                },
                "color": {
                    "ml": round(self.color_ml, 2),
                    "liters": round(self.color_liters, 3)
                }
            }
        }

    def __str__(self) -> str:
        """String representation."""
        return (
            f"\n{'='*60}\n"
            f"ACRYLIC COMPOSITION REPORT\n"
            f"{'='*60}\n\n"
            f"Formula: {self.formula_name}\n"
            f"Surface Area: {self.surface_area_sqft:.2f} sq ft\n"
            f"Number of Coats: {self.num_coats}\n"
            f"Waste Factor: {self.waste_factor:.0%}\n\n"
            f"{'='*60}\n"
            f"SOLUTION COMPOSITION\n"
            f"{'='*60}\n\n"
            f"Total Solution Required:\n"
            f"  {self.total_solution_ml:.2f} ml ({self.total_solution_liters:.3f} L)\n\n"
            f"Component Breakdown:\n"
            f"  Thinner: {self.thinner_ml:.2f} ml ({self.thinner_liters:.3f} L)\n"
            f"  Glue:    {self.glue_ml:.2f} ml ({self.glue_liters:.3f} L)\n"
            f"  Color:   {self.color_ml:.2f} ml ({self.color_liters:.3f} L)\n"
            f"{'='*60}\n"
        )


# Pre-defined standard formulas commonly used in signage
STANDARD_FORMULAS = {
    "standard": AcrylicFormula(
        name="Standard Mix",
        thinner_ratio=30.0,
        glue_ratio=45.0,
        color_ratio=25.0,
        coverage_ml_per_sqft=30.0,
        description="General purpose formula for most signage applications"
    ),
    "high_gloss": AcrylicFormula(
        name="High Gloss",
        thinner_ratio=25.0,
        glue_ratio=55.0,
        color_ratio=20.0,
        coverage_ml_per_sqft=35.0,
        description="Higher binder content for glossy finish"
    ),
    "matte": AcrylicFormula(
        name="Matte Finish",
        thinner_ratio=35.0,
        glue_ratio=40.0,
        color_ratio=25.0,
        coverage_ml_per_sqft=28.0,
        description="More thinner for matte appearance"
    ),
    "heavy_coverage": AcrylicFormula(
        name="Heavy Coverage",
        thinner_ratio=20.0,
        glue_ratio=45.0,
        color_ratio=35.0,
        coverage_ml_per_sqft=40.0,
        description="Higher pigment load for opaque coverage"
    ),
    "thin_coat": AcrylicFormula(
        name="Thin Coat",
        thinner_ratio=40.0,
        glue_ratio=40.0,
        color_ratio=20.0,
        coverage_ml_per_sqft=20.0,
        description="Lighter application for translucent effects"
    ),
    "outdoor": AcrylicFormula(
        name="Outdoor/UV Resistant",
        thinner_ratio=25.0,
        glue_ratio=50.0,
        color_ratio=25.0,
        coverage_ml_per_sqft=35.0,
        description="Enhanced durability for outdoor signage"
    )
}
