# Signage Material Analyzer

A tool for analyzing signage dimensions and calculating material usage per square foot.

## Features

- Calculate total surface area from 2D signage drawings
- Support for multiple material layers (face, substrate, backing, etc.)
- Material usage breakdown per square foot
- Support for rectangular and circular signage shapes
- Waste/overage calculations
- Detailed cost analysis per material

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from signage_analyzer import SignageAnalyzer, Material

# Define signage dimensions (in inches)
analyzer = SignageAnalyzer(height=48, width=96)

# Add materials
analyzer.add_material(Material(
    name="Aluminum Composite",
    cost_per_sqft=12.50,
    coverage_type="full"
))

analyzer.add_material(Material(
    name="Vinyl Graphics",
    cost_per_sqft=8.75,
    coverage_type="full"
))

# Get analysis
results = analyzer.analyze()
print(results)
```

## Usage Examples

See the `examples/` directory for more detailed usage examples.

## API Reference

### SignageAnalyzer

Main class for analyzing signage materials.

**Parameters:**
- `height` (float): Height of signage in inches
- `width` (float): Width of signage in inches (None for circular)
- `shape` (str): Shape type - "rectangle" or "circle" (default: "rectangle")
- `waste_factor` (float): Waste/overage factor (default: 1.1 for 10% waste)

**Methods:**
- `add_material(material)`: Add a material to the analysis
- `analyze()`: Perform the analysis and return results
- `get_summary()`: Get a formatted summary report

### Material

Represents a material used in signage construction.

**Parameters:**
- `name` (str): Material name
- `cost_per_sqft` (float): Cost per square foot
- `coverage_type` (str): "full" or "partial"
- `coverage_area` (float): For partial coverage, area in square inches (optional)
- `coverage_percentage` (float): For partial coverage, percentage of total area (optional)

## License

MIT License
