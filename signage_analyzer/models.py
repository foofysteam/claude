"""
Data models for signage material analysis.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Material:
    """Represents a material used in signage construction."""

    name: str
    cost_per_sqft: float
    coverage_type: str = "full"  # "full" or "partial"
    coverage_area: Optional[float] = None  # in square inches for partial coverage
    coverage_percentage: Optional[float] = None  # percentage of total area for partial coverage

    def __post_init__(self):
        """Validate material data."""
        if self.cost_per_sqft < 0:
            raise ValueError("Cost per square foot must be non-negative")

        if self.coverage_type not in ["full", "partial"]:
            raise ValueError("Coverage type must be 'full' or 'partial'")

        if self.coverage_type == "partial":
            if self.coverage_area is None and self.coverage_percentage is None:
                raise ValueError("Partial coverage requires either coverage_area or coverage_percentage")

            if self.coverage_area is not None and self.coverage_area < 0:
                raise ValueError("Coverage area must be non-negative")

            if self.coverage_percentage is not None:
                if not 0 <= self.coverage_percentage <= 100:
                    raise ValueError("Coverage percentage must be between 0 and 100")


@dataclass
class MaterialUsage:
    """Represents the calculated usage of a material."""

    material_name: str
    total_area_sqft: float
    area_with_waste_sqft: float
    cost_per_sqft: float
    total_cost: float
    waste_factor: float
    coverage_type: str

    def to_dict(self):
        """Convert to dictionary for easy display."""
        return {
            "material_name": self.material_name,
            "total_area_sqft": round(self.total_area_sqft, 2),
            "area_with_waste_sqft": round(self.area_with_waste_sqft, 2),
            "cost_per_sqft": round(self.cost_per_sqft, 2),
            "total_cost": round(self.total_cost, 2),
            "waste_factor": round(self.waste_factor, 2),
            "coverage_type": self.coverage_type
        }

    def __str__(self):
        """String representation."""
        return (
            f"{self.material_name}:\n"
            f"  Coverage: {self.coverage_type}\n"
            f"  Area: {self.total_area_sqft:.2f} sq ft\n"
            f"  Area with waste: {self.area_with_waste_sqft:.2f} sq ft\n"
            f"  Cost/sq ft: ${self.cost_per_sqft:.2f}\n"
            f"  Total cost: ${self.total_cost:.2f}"
        )


@dataclass
class AnalysisResult:
    """Complete analysis result for a signage project."""

    signage_width: float
    signage_height: float
    shape: str
    total_area_sqin: float
    total_area_sqft: float
    material_usages: list
    total_cost: float
    waste_factor: float

    def to_dict(self):
        """Convert to dictionary for easy display."""
        return {
            "dimensions": {
                "width_inches": round(self.signage_width, 2) if self.signage_width else None,
                "height_inches": round(self.signage_height, 2),
                "shape": self.shape
            },
            "area": {
                "total_square_inches": round(self.total_area_sqin, 2),
                "total_square_feet": round(self.total_area_sqft, 2)
            },
            "materials": [usage.to_dict() for usage in self.material_usages],
            "total_cost": round(self.total_cost, 2),
            "waste_factor": round(self.waste_factor, 2)
        }

    def __str__(self):
        """String representation."""
        result = f"\n{'='*60}\n"
        result += "SIGNAGE MATERIAL ANALYSIS REPORT\n"
        result += f"{'='*60}\n\n"

        result += f"Dimensions: {self.signage_height:.2f}\" H"
        if self.signage_width:
            result += f" x {self.signage_width:.2f}\" W"
        result += f" ({self.shape})\n"
        result += f"Total Area: {self.total_area_sqft:.2f} sq ft ({self.total_area_sqin:.2f} sq in)\n"
        result += f"Waste Factor: {self.waste_factor:.1%}\n\n"

        result += f"{'='*60}\n"
        result += "MATERIAL BREAKDOWN\n"
        result += f"{'='*60}\n\n"

        for usage in self.material_usages:
            result += str(usage) + "\n\n"

        result += f"{'='*60}\n"
        result += f"TOTAL PROJECT COST: ${self.total_cost:.2f}\n"
        result += f"{'='*60}\n"

        return result
