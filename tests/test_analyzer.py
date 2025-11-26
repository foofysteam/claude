"""Tests for SignageAnalyzer."""

import pytest
import math
from signage_analyzer import SignageAnalyzer, Material


class TestSignageAnalyzerInitialization:
    """Test SignageAnalyzer initialization."""

    def test_valid_rectangle_initialization(self):
        """Test creating analyzer for rectangular signage."""
        analyzer = SignageAnalyzer(height=48, width=96)
        assert analyzer.height == 48
        assert analyzer.width == 96
        assert analyzer.shape == "rectangle"
        assert analyzer.waste_factor == 1.1

    def test_valid_circle_initialization(self):
        """Test creating analyzer for circular signage."""
        analyzer = SignageAnalyzer(height=36, shape="circle")
        assert analyzer.height == 36
        assert analyzer.shape == "circle"

    def test_custom_waste_factor(self):
        """Test custom waste factor."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.15)
        assert analyzer.waste_factor == 1.15

    def test_negative_height_raises_error(self):
        """Test that negative height raises ValueError."""
        with pytest.raises(ValueError, match="Height must be positive"):
            SignageAnalyzer(height=-48, width=96)

    def test_zero_height_raises_error(self):
        """Test that zero height raises ValueError."""
        with pytest.raises(ValueError, match="Height must be positive"):
            SignageAnalyzer(height=0, width=96)

    def test_rectangle_without_width_raises_error(self):
        """Test that rectangle without width raises ValueError."""
        with pytest.raises(ValueError, match="Width must be positive"):
            SignageAnalyzer(height=48, shape="rectangle")

    def test_invalid_shape_raises_error(self):
        """Test that invalid shape raises ValueError."""
        with pytest.raises(ValueError, match="Shape must be"):
            SignageAnalyzer(height=48, width=96, shape="triangle")

    def test_waste_factor_below_one_raises_error(self):
        """Test that waste factor below 1.0 raises ValueError."""
        with pytest.raises(ValueError, match="Waste factor must be"):
            SignageAnalyzer(height=48, width=96, waste_factor=0.9)


class TestAreaCalculation:
    """Test area calculation methods."""

    def test_rectangle_area_calculation(self):
        """Test rectangular area calculation."""
        analyzer = SignageAnalyzer(height=48, width=96)
        area = analyzer.calculate_area()
        assert area == 4608  # 48 * 96

    def test_circle_area_calculation(self):
        """Test circular area calculation."""
        analyzer = SignageAnalyzer(height=36, shape="circle")
        area = analyzer.calculate_area()
        expected_area = math.pi * (18 ** 2)  # radius = 36/2 = 18
        assert abs(area - expected_area) < 0.01


class TestMaterialManagement:
    """Test material addition and management."""

    def test_add_material(self):
        """Test adding a material."""
        analyzer = SignageAnalyzer(height=48, width=96)
        material = Material(name="Aluminum", cost_per_sqft=15.0)
        analyzer.add_material(material)
        assert len(analyzer.materials) == 1

    def test_add_multiple_materials(self):
        """Test adding multiple materials."""
        analyzer = SignageAnalyzer(height=48, width=96)
        analyzer.add_material(Material(name="Aluminum", cost_per_sqft=15.0))
        analyzer.add_material(Material(name="Vinyl", cost_per_sqft=8.0))
        assert len(analyzer.materials) == 2

    def test_add_invalid_material_raises_error(self):
        """Test that adding non-Material raises TypeError."""
        analyzer = SignageAnalyzer(height=48, width=96)
        with pytest.raises(TypeError, match="material must be a Material instance"):
            analyzer.add_material("not a material")


class TestMaterialUsageCalculation:
    """Test material usage calculations."""

    def test_full_coverage_calculation(self):
        """Test calculation for full coverage material."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.1)
        material = Material(name="Aluminum", cost_per_sqft=15.0, coverage_type="full")

        total_area_sqin = 48 * 96  # 4608 sq in
        usage = analyzer.calculate_material_usage(material, total_area_sqin)

        expected_sqft = 4608 / 144  # 32 sq ft
        expected_with_waste = 32 * 1.1  # 35.2 sq ft
        expected_cost = 35.2 * 15.0  # 528.0

        assert abs(usage.total_area_sqft - expected_sqft) < 0.01
        assert abs(usage.area_with_waste_sqft - expected_with_waste) < 0.01
        assert abs(usage.total_cost - expected_cost) < 0.01

    def test_partial_coverage_with_area(self):
        """Test calculation for partial coverage with specific area."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.1)
        material = Material(
            name="Vinyl",
            cost_per_sqft=8.0,
            coverage_type="partial",
            coverage_area=2304  # half of total
        )

        total_area_sqin = 48 * 96
        usage = analyzer.calculate_material_usage(material, total_area_sqin)

        expected_sqft = 2304 / 144  # 16 sq ft
        expected_with_waste = 16 * 1.1  # 17.6 sq ft
        expected_cost = 17.6 * 8.0  # 140.8

        assert abs(usage.total_area_sqft - expected_sqft) < 0.01
        assert abs(usage.area_with_waste_sqft - expected_with_waste) < 0.01
        assert abs(usage.total_cost - expected_cost) < 0.01

    def test_partial_coverage_with_percentage(self):
        """Test calculation for partial coverage with percentage."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.1)
        material = Material(
            name="Vinyl",
            cost_per_sqft=8.0,
            coverage_type="partial",
            coverage_percentage=50.0
        )

        total_area_sqin = 48 * 96
        usage = analyzer.calculate_material_usage(material, total_area_sqin)

        expected_sqft = (4608 * 0.5) / 144  # 16 sq ft
        expected_with_waste = 16 * 1.1  # 17.6 sq ft
        expected_cost = 17.6 * 8.0  # 140.8

        assert abs(usage.total_area_sqft - expected_sqft) < 0.01
        assert abs(usage.area_with_waste_sqft - expected_with_waste) < 0.01
        assert abs(usage.total_cost - expected_cost) < 0.01


class TestAnalysis:
    """Test complete analysis."""

    def test_analyze_without_materials_raises_error(self):
        """Test that analyzing without materials raises error."""
        analyzer = SignageAnalyzer(height=48, width=96)
        with pytest.raises(ValueError, match="No materials added"):
            analyzer.analyze()

    def test_basic_analysis(self):
        """Test basic analysis with one material."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.1)
        analyzer.add_material(Material(name="Aluminum", cost_per_sqft=15.0))

        result = analyzer.analyze()

        assert result.signage_height == 48
        assert result.signage_width == 96
        assert result.shape == "rectangle"
        assert result.total_area_sqin == 4608
        assert abs(result.total_area_sqft - 32.0) < 0.01
        assert len(result.material_usages) == 1

    def test_analysis_with_multiple_materials(self):
        """Test analysis with multiple materials."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.1)
        analyzer.add_material(Material(name="Aluminum", cost_per_sqft=15.0))
        analyzer.add_material(Material(name="Vinyl", cost_per_sqft=8.0))

        result = analyzer.analyze()

        assert len(result.material_usages) == 2
        # Total cost = (32 * 1.1 * 15) + (32 * 1.1 * 8) = 528 + 281.6 = 809.6
        expected_total = (32 * 1.1 * 15) + (32 * 1.1 * 8)
        assert abs(result.total_cost - expected_total) < 0.01

    def test_get_summary(self):
        """Test getting formatted summary."""
        analyzer = SignageAnalyzer(height=48, width=96)
        analyzer.add_material(Material(name="Aluminum", cost_per_sqft=15.0))

        summary = analyzer.get_summary()
        assert "SIGNAGE MATERIAL ANALYSIS REPORT" in summary
        assert "Aluminum" in summary
        assert "32.00 sq ft" in summary

    def test_get_cost_per_sqft(self):
        """Test getting cost per square foot breakdown."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.1)
        analyzer.add_material(Material(name="Aluminum", cost_per_sqft=15.0))

        cost_breakdown = analyzer.get_cost_per_sqft()

        assert abs(cost_breakdown["total_signage_area_sqft"] - 32.0) < 0.01
        assert len(cost_breakdown["materials"]) == 1

        # Cost per sqft of signage = (32 * 1.1 * 15) / 32 = 16.5
        expected_cost_per_sqft = 16.5
        assert abs(cost_breakdown["total_cost_per_sqft_of_signage"] - expected_cost_per_sqft) < 0.01


class TestEdgeCases:
    """Test edge cases and special scenarios."""

    def test_very_small_signage(self):
        """Test with very small signage dimensions."""
        analyzer = SignageAnalyzer(height=1, width=1)
        analyzer.add_material(Material(name="Test", cost_per_sqft=10.0))

        result = analyzer.analyze()
        assert result.total_area_sqin == 1
        assert abs(result.total_area_sqft - (1/144)) < 0.001

    def test_no_waste_factor(self):
        """Test with waste factor of 1.0 (no waste)."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.0)
        analyzer.add_material(Material(name="Aluminum", cost_per_sqft=15.0))

        result = analyzer.analyze()
        # No waste, so area with waste = total area
        assert abs(result.material_usages[0].area_with_waste_sqft - 32.0) < 0.01

    def test_high_waste_factor(self):
        """Test with high waste factor."""
        analyzer = SignageAnalyzer(height=48, width=96, waste_factor=1.5)
        analyzer.add_material(Material(name="Aluminum", cost_per_sqft=15.0))

        result = analyzer.analyze()
        # 50% waste
        expected_area_with_waste = 32.0 * 1.5
        assert abs(result.material_usages[0].area_with_waste_sqft - expected_area_with_waste) < 0.01
