"""Tests for Acrylic Composition Calculator."""

import math
import pytest
from signage_analyzer.acrylic_models import (
    AcrylicFormula,
    AcrylicComposition,
    STANDARD_FORMULAS
)
from signage_analyzer.acrylic_calculator import AcrylicCompositionCalculator


class TestAcrylicFormula:
    """Test AcrylicFormula class."""

    def test_valid_formula(self):
        """Test creating a valid formula."""
        formula = AcrylicFormula(
            name="Test Formula",
            thinner_ratio=30.0,
            glue_ratio=45.0,
            color_ratio=25.0,
            coverage_ml_per_sqft=30.0
        )
        assert formula.name == "Test Formula"
        assert formula.thinner_ratio == 30.0
        assert formula.glue_ratio == 45.0
        assert formula.color_ratio == 25.0

    def test_formula_ratios_must_sum_to_100(self):
        """Test that ratios must sum to 100%."""
        with pytest.raises(ValueError, match="ratios must sum to 100%"):
            AcrylicFormula(
                name="Invalid",
                thinner_ratio=30.0,
                glue_ratio=40.0,
                color_ratio=20.0  # Sum = 90%
            )

    def test_negative_ratio_raises_error(self):
        """Test that negative ratios raise ValueError."""
        with pytest.raises(ValueError, match="must be non-negative"):
            AcrylicFormula(
                name="Invalid",
                thinner_ratio=-10.0,
                glue_ratio=60.0,
                color_ratio=50.0
            )

    def test_zero_coverage_raises_error(self):
        """Test that zero coverage raises ValueError."""
        with pytest.raises(ValueError, match="Coverage rate must be positive"):
            AcrylicFormula(
                name="Invalid",
                thinner_ratio=30.0,
                glue_ratio=45.0,
                color_ratio=25.0,
                coverage_ml_per_sqft=0
            )

    def test_formula_to_dict(self):
        """Test formula to_dict method."""
        formula = AcrylicFormula(
            name="Test",
            thinner_ratio=30.0,
            glue_ratio=45.0,
            color_ratio=25.0
        )
        result = formula.to_dict()
        assert result["name"] == "Test"
        assert result["thinner_ratio"] == 30.0


class TestAcrylicComposition:
    """Test AcrylicComposition class."""

    def test_composition_properties(self):
        """Test composition liter conversion properties."""
        comp = AcrylicComposition(
            formula_name="Test",
            surface_area_sqft=10.0,
            total_solution_ml=1000.0,
            thinner_ml=300.0,
            glue_ml=450.0,
            color_ml=250.0,
            num_coats=1,
            waste_factor=1.1
        )

        assert comp.total_solution_liters == 1.0
        assert comp.thinner_liters == 0.3
        assert comp.glue_liters == 0.45
        assert comp.color_liters == 0.25

    def test_composition_to_dict(self):
        """Test composition to_dict method."""
        comp = AcrylicComposition(
            formula_name="Test",
            surface_area_sqft=10.0,
            total_solution_ml=1000.0,
            thinner_ml=300.0,
            glue_ml=450.0,
            color_ml=250.0,
            num_coats=2,
            waste_factor=1.1
        )

        result = comp.to_dict()
        assert result["formula_name"] == "Test"
        assert result["surface_area_sqft"] == 10.0
        assert result["num_coats"] == 2
        assert "composition" in result

    def test_composition_str(self):
        """Test composition string representation."""
        comp = AcrylicComposition(
            formula_name="Test Mix",
            surface_area_sqft=10.0,
            total_solution_ml=1000.0,
            thinner_ml=300.0,
            glue_ml=450.0,
            color_ml=250.0,
            num_coats=1,
            waste_factor=1.1
        )

        result = str(comp)
        assert "Test Mix" in result
        assert "Thinner" in result
        assert "Glue" in result
        assert "Color" in result


class TestStandardFormulas:
    """Test standard formulas."""

    def test_standard_formulas_exist(self):
        """Test that standard formulas are defined."""
        expected = ["standard", "high_gloss", "matte", "heavy_coverage", "thin_coat", "outdoor"]
        for name in expected:
            assert name in STANDARD_FORMULAS

    def test_standard_formulas_ratios_sum_to_100(self):
        """Test that all standard formula ratios sum to 100%."""
        for name, formula in STANDARD_FORMULAS.items():
            total = formula.thinner_ratio + formula.glue_ratio + formula.color_ratio
            assert abs(total - 100.0) < 0.01, f"Formula {name} ratios sum to {total}%"


class TestAcrylicCompositionCalculator:
    """Test AcrylicCompositionCalculator class."""

    def test_init_rectangle(self):
        """Test initializing calculator for rectangle."""
        calc = AcrylicCompositionCalculator(
            height=48,
            width=96,
            shape="rectangle",
            unit="inches"
        )
        assert calc.height == 48
        assert calc.width == 96
        assert calc.shape == "rectangle"

    def test_init_circle(self):
        """Test initializing calculator for circle."""
        calc = AcrylicCompositionCalculator(
            height=36,
            shape="circle",
            unit="inches"
        )
        assert calc.height == 36
        assert calc.shape == "circle"

    def test_invalid_height_raises_error(self):
        """Test that non-positive height raises ValueError."""
        with pytest.raises(ValueError, match="Height must be positive"):
            AcrylicCompositionCalculator(height=0, width=10)

    def test_invalid_shape_raises_error(self):
        """Test that invalid shape raises ValueError."""
        with pytest.raises(ValueError, match="Shape must be"):
            AcrylicCompositionCalculator(height=10, width=10, shape="triangle")

    def test_rectangle_without_width_raises_error(self):
        """Test that rectangle without width raises ValueError."""
        with pytest.raises(ValueError, match="Width must be positive"):
            AcrylicCompositionCalculator(height=10, shape="rectangle")

    def test_invalid_unit_raises_error(self):
        """Test that invalid unit raises ValueError."""
        with pytest.raises(ValueError, match="Unit must be"):
            AcrylicCompositionCalculator(height=10, width=10, unit="yards")

    def test_calculate_area_rectangle(self):
        """Test area calculation for rectangle."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        area = calc.calculate_area()
        assert area == 144.0

    def test_calculate_area_circle(self):
        """Test area calculation for circle."""
        calc = AcrylicCompositionCalculator(height=12, shape="circle", unit="inches")
        area = calc.calculate_area()
        expected = math.pi * 36  # pi * r^2 where r=6
        assert abs(area - expected) < 0.01

    def test_calculate_area_sqft_inches(self):
        """Test area conversion from inches to sqft."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        area_sqft = calc.calculate_area_sqft()
        assert area_sqft == 1.0  # 144 sq in = 1 sq ft

    def test_calculate_area_sqft_feet(self):
        """Test area calculation in feet."""
        calc = AcrylicCompositionCalculator(height=4, width=8, unit="feet")
        area_sqft = calc.calculate_area_sqft()
        assert area_sqft == 32.0

    def test_calculate_area_sqft_cm(self):
        """Test area conversion from cm to sqft."""
        calc = AcrylicCompositionCalculator(height=30.48, width=30.48, unit="cm")
        area_sqft = calc.calculate_area_sqft()
        assert abs(area_sqft - 1.0) < 0.01  # ~30.48 cm = 1 foot

    def test_calculate_area_sqft_meters(self):
        """Test area conversion from meters to sqft."""
        calc = AcrylicCompositionCalculator(height=1, width=1, unit="meters")
        area_sqft = calc.calculate_area_sqft()
        assert abs(area_sqft - 10.764) < 0.1  # 1 sq m ~ 10.764 sq ft

    def test_calculate_with_string_formula(self):
        """Test calculation with string formula name."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        result = calc.calculate(formula="standard", num_coats=1, waste_factor=1.0)

        assert result.formula_name == "Standard Mix"
        assert result.surface_area_sqft == 1.0
        # Standard formula: 30 ml/sqft coverage
        assert result.total_solution_ml == 30.0
        # Standard ratios: 30% thinner, 45% glue, 25% color
        assert abs(result.thinner_ml - 9.0) < 0.01
        assert abs(result.glue_ml - 13.5) < 0.01
        assert abs(result.color_ml - 7.5) < 0.01

    def test_calculate_with_custom_formula(self):
        """Test calculation with custom formula object."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        custom = AcrylicFormula(
            name="Custom",
            thinner_ratio=40.0,
            glue_ratio=40.0,
            color_ratio=20.0,
            coverage_ml_per_sqft=50.0
        )
        result = calc.calculate(formula=custom, num_coats=1, waste_factor=1.0)

        assert result.formula_name == "Custom"
        assert result.total_solution_ml == 50.0
        assert abs(result.thinner_ml - 20.0) < 0.01
        assert abs(result.glue_ml - 20.0) < 0.01
        assert abs(result.color_ml - 10.0) < 0.01

    def test_calculate_with_multiple_coats(self):
        """Test calculation with multiple coats."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        result = calc.calculate(formula="standard", num_coats=2, waste_factor=1.0)

        # Should be 2x the single coat amount
        assert result.num_coats == 2
        assert result.total_solution_ml == 60.0  # 30ml * 2 coats

    def test_calculate_with_waste_factor(self):
        """Test calculation with waste factor."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        result = calc.calculate(formula="standard", num_coats=1, waste_factor=1.1)

        assert result.waste_factor == 1.1
        assert result.total_solution_ml == 33.0  # 30ml * 1.1

    def test_calculate_invalid_formula_raises_error(self):
        """Test that invalid formula name raises ValueError."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        with pytest.raises(ValueError, match="Unknown formula"):
            calc.calculate(formula="nonexistent")

    def test_calculate_invalid_num_coats_raises_error(self):
        """Test that invalid num_coats raises ValueError."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        with pytest.raises(ValueError, match="Number of coats must be at least 1"):
            calc.calculate(num_coats=0)

    def test_calculate_invalid_waste_factor_raises_error(self):
        """Test that waste factor < 1 raises ValueError."""
        calc = AcrylicCompositionCalculator(height=12, width=12, unit="inches")
        with pytest.raises(ValueError, match="Waste factor must be >= 1.0"):
            calc.calculate(waste_factor=0.9)

    def test_calculate_from_area(self):
        """Test calculate_from_area method."""
        calc = AcrylicCompositionCalculator(height=1, width=1, unit="feet")
        result = calc.calculate_from_area(
            area_sqft=10.0,
            formula="standard",
            num_coats=1,
            waste_factor=1.0
        )

        assert result.surface_area_sqft == 10.0
        assert result.total_solution_ml == 300.0  # 10 sqft * 30 ml/sqft

    def test_calculate_from_area_invalid_area_raises_error(self):
        """Test that invalid area raises ValueError."""
        calc = AcrylicCompositionCalculator(height=1, width=1, unit="feet")
        with pytest.raises(ValueError, match="Area must be positive"):
            calc.calculate_from_area(area_sqft=0)

    def test_get_summary(self):
        """Test get_summary method returns formatted string."""
        calc = AcrylicCompositionCalculator(height=48, width=96, unit="inches")
        summary = calc.get_summary(formula="standard")
        assert "Standard Mix" in summary
        assert "Thinner" in summary
        assert "Glue" in summary
        assert "Color" in summary

    def test_list_formulas(self):
        """Test list_formulas static method."""
        formulas = AcrylicCompositionCalculator.list_formulas()
        assert "standard" in formulas
        assert "description" in formulas["standard"]
        assert "thinner" in formulas["standard"]
        assert "glue" in formulas["standard"]
        assert "color" in formulas["standard"]

    def test_create_custom_formula(self):
        """Test create_custom_formula static method."""
        formula = AcrylicCompositionCalculator.create_custom_formula(
            name="My Custom",
            thinner_ratio=35.0,
            glue_ratio=40.0,
            color_ratio=25.0,
            coverage_ml_per_sqft=32.0,
            description="My custom formula"
        )

        assert formula.name == "My Custom"
        assert formula.thinner_ratio == 35.0
        assert formula.glue_ratio == 40.0
        assert formula.color_ratio == 25.0
        assert formula.coverage_ml_per_sqft == 32.0

    def test_real_world_signage_calculation(self):
        """Test a realistic signage calculation scenario."""
        # 4' x 8' sign (48" x 96") with 2 coats and 10% waste
        calc = AcrylicCompositionCalculator(
            height=48,
            width=96,
            unit="inches"
        )

        result = calc.calculate(
            formula="standard",
            num_coats=2,
            waste_factor=1.1
        )

        # Area = 48 * 96 / 144 = 32 sq ft
        assert result.surface_area_sqft == 32.0

        # Total solution = 32 sqft * 30 ml/sqft * 2 coats * 1.1 waste
        expected_total = 32.0 * 30.0 * 2 * 1.1
        assert abs(result.total_solution_ml - expected_total) < 0.01

        # Check component ratios are correct (30%, 45%, 25%)
        assert abs(result.thinner_ml / result.total_solution_ml - 0.30) < 0.01
        assert abs(result.glue_ml / result.total_solution_ml - 0.45) < 0.01
        assert abs(result.color_ml / result.total_solution_ml - 0.25) < 0.01
