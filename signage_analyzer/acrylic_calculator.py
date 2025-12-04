"""
Acrylic Composition Calculator for Signage.
Similar to eCut plugin for CorelDRAW - calculates liquid acrylic solution composition.
"""

import math
from typing import Optional, Union
from .acrylic_models import AcrylicFormula, AcrylicComposition, STANDARD_FORMULAS


class AcrylicCompositionCalculator:
    """
    Calculates the composition of liquid acrylic solution based on signage surface area.

    This tool replicates the functionality of eCut plugin for CorelDRAW,
    providing accurate measurements for thinner, glue, and color components.
    """

    def __init__(
        self,
        height: float,
        width: Optional[float] = None,
        shape: str = "rectangle",
        unit: str = "inches"
    ):
        """
        Initialize the calculator with signage dimensions.

        Args:
            height: Height of signage (or diameter for circle)
            width: Width of signage (required for rectangle)
            shape: Shape type - "rectangle" or "circle"
            unit: Measurement unit - "inches", "feet", "cm", or "meters"
        """
        self.height = height
        self.width = width
        self.shape = shape.lower()
        self.unit = unit.lower()

        self._validate_inputs()

    def _validate_inputs(self):
        """Validate initialization inputs."""
        if self.height <= 0:
            raise ValueError("Height must be positive")

        if self.shape not in ["rectangle", "circle"]:
            raise ValueError("Shape must be 'rectangle' or 'circle'")

        if self.shape == "rectangle" and (self.width is None or self.width <= 0):
            raise ValueError("Width must be positive for rectangular signage")

        if self.unit not in ["inches", "feet", "cm", "meters"]:
            raise ValueError("Unit must be 'inches', 'feet', 'cm', or 'meters'")

    def _convert_to_sqft(self, area: float) -> float:
        """Convert area from current unit to square feet."""
        if self.unit == "inches":
            return area / 144.0
        elif self.unit == "feet":
            return area
        elif self.unit == "cm":
            # 1 sq ft = 929.0304 sq cm
            return area / 929.0304
        elif self.unit == "meters":
            # 1 sq ft = 0.092903 sq m
            return area / 0.092903
        else:
            raise ValueError(f"Unsupported unit: {self.unit}")

    def calculate_area(self) -> float:
        """
        Calculate the surface area of the signage.

        Returns:
            Area in the original unit squared
        """
        if self.shape == "rectangle":
            return self.height * self.width
        elif self.shape == "circle":
            radius = self.height / 2
            return math.pi * radius * radius
        else:
            raise ValueError(f"Unsupported shape: {self.shape}")

    def calculate_area_sqft(self) -> float:
        """
        Calculate the surface area in square feet.

        Returns:
            Area in square feet
        """
        area = self.calculate_area()
        return self._convert_to_sqft(area)

    def calculate(
        self,
        formula: Union[str, AcrylicFormula] = "standard",
        num_coats: int = 1,
        waste_factor: float = 1.1
    ) -> AcrylicComposition:
        """
        Calculate the acrylic solution composition for the signage.

        Args:
            formula: Formula name (string) or custom AcrylicFormula object
                    Available presets: "standard", "high_gloss", "matte",
                    "heavy_coverage", "thin_coat", "outdoor"
            num_coats: Number of coats to apply (default: 1)
            waste_factor: Waste/overage multiplier (1.1 = 10% waste, default: 1.1)

        Returns:
            AcrylicComposition object with calculated amounts
        """
        # Validate inputs
        if num_coats < 1:
            raise ValueError("Number of coats must be at least 1")

        if waste_factor < 1.0:
            raise ValueError("Waste factor must be >= 1.0")

        # Get formula
        if isinstance(formula, str):
            formula_key = formula.lower()
            if formula_key not in STANDARD_FORMULAS:
                available = ", ".join(STANDARD_FORMULAS.keys())
                raise ValueError(
                    f"Unknown formula: '{formula}'. "
                    f"Available formulas: {available}"
                )
            formula = STANDARD_FORMULAS[formula_key]

        # Calculate area in square feet
        area_sqft = self.calculate_area_sqft()

        # Calculate total solution needed
        base_solution_ml = area_sqft * formula.coverage_ml_per_sqft
        total_solution_ml = base_solution_ml * num_coats * waste_factor

        # Calculate component amounts based on ratios
        thinner_ml = total_solution_ml * (formula.thinner_ratio / 100.0)
        glue_ml = total_solution_ml * (formula.glue_ratio / 100.0)
        color_ml = total_solution_ml * (formula.color_ratio / 100.0)

        return AcrylicComposition(
            formula_name=formula.name,
            surface_area_sqft=area_sqft,
            total_solution_ml=total_solution_ml,
            thinner_ml=thinner_ml,
            glue_ml=glue_ml,
            color_ml=color_ml,
            num_coats=num_coats,
            waste_factor=waste_factor
        )

    def calculate_from_area(
        self,
        area_sqft: float,
        formula: Union[str, AcrylicFormula] = "standard",
        num_coats: int = 1,
        waste_factor: float = 1.1
    ) -> AcrylicComposition:
        """
        Calculate composition from a known area in square feet.

        Args:
            area_sqft: Surface area in square feet
            formula: Formula name or custom AcrylicFormula
            num_coats: Number of coats to apply
            waste_factor: Waste/overage multiplier

        Returns:
            AcrylicComposition object with calculated amounts
        """
        if area_sqft <= 0:
            raise ValueError("Area must be positive")

        if num_coats < 1:
            raise ValueError("Number of coats must be at least 1")

        if waste_factor < 1.0:
            raise ValueError("Waste factor must be >= 1.0")

        # Get formula
        if isinstance(formula, str):
            formula_key = formula.lower()
            if formula_key not in STANDARD_FORMULAS:
                available = ", ".join(STANDARD_FORMULAS.keys())
                raise ValueError(
                    f"Unknown formula: '{formula}'. "
                    f"Available formulas: {available}"
                )
            formula = STANDARD_FORMULAS[formula_key]

        # Calculate total solution needed
        base_solution_ml = area_sqft * formula.coverage_ml_per_sqft
        total_solution_ml = base_solution_ml * num_coats * waste_factor

        # Calculate component amounts
        thinner_ml = total_solution_ml * (formula.thinner_ratio / 100.0)
        glue_ml = total_solution_ml * (formula.glue_ratio / 100.0)
        color_ml = total_solution_ml * (formula.color_ratio / 100.0)

        return AcrylicComposition(
            formula_name=formula.name,
            surface_area_sqft=area_sqft,
            total_solution_ml=total_solution_ml,
            thinner_ml=thinner_ml,
            glue_ml=glue_ml,
            color_ml=color_ml,
            num_coats=num_coats,
            waste_factor=waste_factor
        )

    def get_summary(
        self,
        formula: Union[str, AcrylicFormula] = "standard",
        num_coats: int = 1,
        waste_factor: float = 1.1
    ) -> str:
        """
        Get a formatted summary report.

        Args:
            formula: Formula name or custom AcrylicFormula
            num_coats: Number of coats to apply
            waste_factor: Waste/overage multiplier

        Returns:
            Formatted string with composition results
        """
        result = self.calculate(formula, num_coats, waste_factor)
        return str(result)

    @staticmethod
    def list_formulas() -> dict:
        """
        List all available standard formulas.

        Returns:
            Dictionary of formula names and their descriptions
        """
        return {
            name: {
                "description": formula.description,
                "thinner": f"{formula.thinner_ratio}%",
                "glue": f"{formula.glue_ratio}%",
                "color": f"{formula.color_ratio}%",
                "coverage": f"{formula.coverage_ml_per_sqft} ml/sq ft"
            }
            for name, formula in STANDARD_FORMULAS.items()
        }

    @staticmethod
    def create_custom_formula(
        name: str,
        thinner_ratio: float,
        glue_ratio: float,
        color_ratio: float,
        coverage_ml_per_sqft: float = 30.0,
        description: str = ""
    ) -> AcrylicFormula:
        """
        Create a custom acrylic formula.

        Args:
            name: Name for the custom formula
            thinner_ratio: Thinner percentage (0-100)
            glue_ratio: Glue/binder percentage (0-100)
            color_ratio: Color/pigment percentage (0-100)
            coverage_ml_per_sqft: ml of solution per square foot
            description: Optional description

        Returns:
            Custom AcrylicFormula object

        Note:
            Ratios must sum to exactly 100%
        """
        return AcrylicFormula(
            name=name,
            thinner_ratio=thinner_ratio,
            glue_ratio=glue_ratio,
            color_ratio=color_ratio,
            coverage_ml_per_sqft=coverage_ml_per_sqft,
            description=description
        )
