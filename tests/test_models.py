"""Tests for data models."""

import pytest
from signage_analyzer.models import Material, MaterialUsage, AnalysisResult


class TestMaterial:
    """Test Material class."""

    def test_valid_full_coverage_material(self):
        """Test creating a valid full coverage material."""
        material = Material(
            name="Aluminum",
            cost_per_sqft=15.0,
            coverage_type="full"
        )
        assert material.name == "Aluminum"
        assert material.cost_per_sqft == 15.0
        assert material.coverage_type == "full"

    def test_valid_partial_coverage_with_area(self):
        """Test creating partial coverage material with area."""
        material = Material(
            name="Vinyl",
            cost_per_sqft=8.0,
            coverage_type="partial",
            coverage_area=100.0
        )
        assert material.coverage_area == 100.0

    def test_valid_partial_coverage_with_percentage(self):
        """Test creating partial coverage material with percentage."""
        material = Material(
            name="Vinyl",
            cost_per_sqft=8.0,
            coverage_type="partial",
            coverage_percentage=50.0
        )
        assert material.coverage_percentage == 50.0

    def test_negative_cost_raises_error(self):
        """Test that negative cost raises ValueError."""
        with pytest.raises(ValueError, match="Cost per square foot must be non-negative"):
            Material(name="Test", cost_per_sqft=-5.0)

    def test_invalid_coverage_type_raises_error(self):
        """Test that invalid coverage type raises ValueError."""
        with pytest.raises(ValueError, match="Coverage type must be 'full' or 'partial'"):
            Material(name="Test", cost_per_sqft=10.0, coverage_type="invalid")

    def test_partial_without_area_or_percentage_raises_error(self):
        """Test that partial coverage without area/percentage raises error."""
        with pytest.raises(ValueError, match="Partial coverage requires"):
            Material(
                name="Test",
                cost_per_sqft=10.0,
                coverage_type="partial"
            )

    def test_negative_coverage_area_raises_error(self):
        """Test that negative coverage area raises ValueError."""
        with pytest.raises(ValueError, match="Coverage area must be non-negative"):
            Material(
                name="Test",
                cost_per_sqft=10.0,
                coverage_type="partial",
                coverage_area=-50
            )

    def test_invalid_coverage_percentage_raises_error(self):
        """Test that invalid coverage percentage raises ValueError."""
        with pytest.raises(ValueError, match="Coverage percentage must be between 0 and 100"):
            Material(
                name="Test",
                cost_per_sqft=10.0,
                coverage_type="partial",
                coverage_percentage=150
            )


class TestMaterialUsage:
    """Test MaterialUsage class."""

    def test_material_usage_to_dict(self):
        """Test MaterialUsage to_dict method."""
        usage = MaterialUsage(
            material_name="Aluminum",
            total_area_sqft=10.5,
            area_with_waste_sqft=11.55,
            cost_per_sqft=15.0,
            total_cost=173.25,
            waste_factor=1.1,
            coverage_type="full"
        )

        result = usage.to_dict()
        assert result["material_name"] == "Aluminum"
        assert result["total_area_sqft"] == 10.5
        assert result["cost_per_sqft"] == 15.0

    def test_material_usage_str(self):
        """Test MaterialUsage string representation."""
        usage = MaterialUsage(
            material_name="Aluminum",
            total_area_sqft=10.5,
            area_with_waste_sqft=11.55,
            cost_per_sqft=15.0,
            total_cost=173.25,
            waste_factor=1.1,
            coverage_type="full"
        )

        result = str(usage)
        assert "Aluminum" in result
        assert "10.50 sq ft" in result
        assert "$15.00" in result
