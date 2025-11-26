"""
Core signage analyzer functionality.
"""

import math
from typing import List, Optional
from .models import Material, MaterialUsage, AnalysisResult


class SignageAnalyzer:
    """Analyzes signage dimensions and calculates material usage per square foot."""

    def __init__(
        self,
        height: float,
        width: Optional[float] = None,
        shape: str = "rectangle",
        waste_factor: float = 1.1
    ):
        """
        Initialize the signage analyzer.

        Args:
            height: Height of signage in inches (or diameter for circle)
            width: Width of signage in inches (required for rectangle)
            shape: Shape type - "rectangle" or "circle"
            waste_factor: Waste/overage multiplier (1.1 = 10% waste)
        """
        self.height = height
        self.width = width
        self.shape = shape.lower()
        self.waste_factor = waste_factor
        self.materials: List[Material] = []

        self._validate_inputs()

    def _validate_inputs(self):
        """Validate initialization inputs."""
        if self.height <= 0:
            raise ValueError("Height must be positive")

        if self.shape not in ["rectangle", "circle"]:
            raise ValueError("Shape must be 'rectangle' or 'circle'")

        if self.shape == "rectangle" and (self.width is None or self.width <= 0):
            raise ValueError("Width must be positive for rectangular signage")

        if self.waste_factor < 1.0:
            raise ValueError("Waste factor must be >= 1.0")

    def add_material(self, material: Material):
        """
        Add a material to the analysis.

        Args:
            material: Material object to add
        """
        if not isinstance(material, Material):
            raise TypeError("material must be a Material instance")
        self.materials.append(material)

    def calculate_area(self) -> float:
        """
        Calculate the total area of the signage in square inches.

        Returns:
            Area in square inches
        """
        if self.shape == "rectangle":
            return self.height * self.width
        elif self.shape == "circle":
            radius = self.height / 2
            return math.pi * radius * radius
        else:
            raise ValueError(f"Unsupported shape: {self.shape}")

    def calculate_material_usage(self, material: Material, total_area_sqin: float) -> MaterialUsage:
        """
        Calculate usage for a specific material.

        Args:
            material: Material to calculate
            total_area_sqin: Total signage area in square inches

        Returns:
            MaterialUsage object with calculations
        """
        # Determine actual coverage area
        if material.coverage_type == "full":
            coverage_area_sqin = total_area_sqin
        else:  # partial
            if material.coverage_area is not None:
                coverage_area_sqin = material.coverage_area
            elif material.coverage_percentage is not None:
                coverage_area_sqin = total_area_sqin * (material.coverage_percentage / 100.0)
            else:
                raise ValueError(f"Invalid partial coverage for material: {material.name}")

        # Convert to square feet
        coverage_area_sqft = coverage_area_sqin / 144.0

        # Apply waste factor
        area_with_waste_sqft = coverage_area_sqft * self.waste_factor

        # Calculate cost
        total_cost = area_with_waste_sqft * material.cost_per_sqft

        return MaterialUsage(
            material_name=material.name,
            total_area_sqft=coverage_area_sqft,
            area_with_waste_sqft=area_with_waste_sqft,
            cost_per_sqft=material.cost_per_sqft,
            total_cost=total_cost,
            waste_factor=self.waste_factor,
            coverage_type=material.coverage_type
        )

    def analyze(self) -> AnalysisResult:
        """
        Perform complete analysis of the signage project.

        Returns:
            AnalysisResult object with complete breakdown
        """
        if not self.materials:
            raise ValueError("No materials added. Add at least one material before analyzing.")

        # Calculate total area
        total_area_sqin = self.calculate_area()
        total_area_sqft = total_area_sqin / 144.0

        # Calculate usage for each material
        material_usages = []
        total_cost = 0.0

        for material in self.materials:
            usage = self.calculate_material_usage(material, total_area_sqin)
            material_usages.append(usage)
            total_cost += usage.total_cost

        return AnalysisResult(
            signage_width=self.width,
            signage_height=self.height,
            shape=self.shape,
            total_area_sqin=total_area_sqin,
            total_area_sqft=total_area_sqft,
            material_usages=material_usages,
            total_cost=total_cost,
            waste_factor=self.waste_factor
        )

    def get_summary(self) -> str:
        """
        Get a formatted summary report.

        Returns:
            Formatted string with analysis results
        """
        result = self.analyze()
        return str(result)

    def get_cost_per_sqft(self) -> dict:
        """
        Get cost breakdown per square foot of signage.

        Returns:
            Dictionary with per-square-foot costs
        """
        result = self.analyze()
        total_area_sqft = result.total_area_sqft

        per_sqft_breakdown = {
            "total_signage_area_sqft": total_area_sqft,
            "materials": []
        }

        for usage in result.material_usages:
            per_sqft_breakdown["materials"].append({
                "name": usage.material_name,
                "cost_per_sqft_of_signage": usage.total_cost / total_area_sqft,
                "material_cost_per_sqft": usage.cost_per_sqft,
                "coverage_type": usage.coverage_type
            })

        per_sqft_breakdown["total_cost_per_sqft_of_signage"] = result.total_cost / total_area_sqft

        return per_sqft_breakdown
