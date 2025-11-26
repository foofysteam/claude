# Signage Material Analyzer - Usage Guide

## Overview

The Signage Material Analyzer is a Python tool designed to help signage professionals calculate material requirements and costs for signage projects. Given 2D drawings with dimensions and material specifications, it calculates:

- Total surface area
- Material usage per square foot
- Cost breakdowns per material
- Total project costs
- Waste/overage calculations

## Installation

```bash
git clone <repository-url>
cd claude
pip install -r requirements.txt
```

## Basic Concepts

### Dimensions
- All dimensions are specified in **inches**
- Supported shapes: `rectangle` and `circle`
- For rectangles: specify `height` and `width`
- For circles: specify `height` (diameter)

### Materials
Materials can have two coverage types:

1. **Full Coverage**: Material covers the entire signage surface
   ```python
   Material(name="Aluminum", cost_per_sqft=15.0, coverage_type="full")
   ```

2. **Partial Coverage**: Material covers only part of the signage
   ```python
   # By percentage
   Material(name="Vinyl", cost_per_sqft=8.0, coverage_type="partial", coverage_percentage=50.0)

   # By specific area (in square inches)
   Material(name="Logo", cost_per_sqft=18.0, coverage_type="partial", coverage_area=576)
   ```

### Waste Factor
The waste factor accounts for material overage during fabrication:
- `1.0` = No waste (0%)
- `1.1` = 10% waste (default)
- `1.2` = 20% waste
- Use higher waste factors for complex cuts or difficult materials

## Quick Start Example

```python
from signage_analyzer import SignageAnalyzer, Material

# Create analyzer for 4' x 8' sign (48" x 96")
analyzer = SignageAnalyzer(height=48, width=96)

# Add substrate
analyzer.add_material(Material(
    name="Aluminum Composite",
    cost_per_sqft=12.50
))

# Add graphics
analyzer.add_material(Material(
    name="Vinyl Graphics",
    cost_per_sqft=8.75
))

# Analyze and print results
result = analyzer.analyze()
print(result)
```

## Common Use Cases

### 1. Standard Rectangular Sign

```python
analyzer = SignageAnalyzer(
    height=48,      # 4 feet
    width=96,       # 8 feet
    waste_factor=1.1
)

analyzer.add_material(Material(name="ACM Panel", cost_per_sqft=12.00))
analyzer.add_material(Material(name="Vinyl", cost_per_sqft=8.00))
```

### 2. Circular Sign

```python
analyzer = SignageAnalyzer(
    height=36,          # 36" diameter
    shape="circle",
    waste_factor=1.2    # Higher waste for circular cuts
)

analyzer.add_material(Material(name="MDO Plywood", cost_per_sqft=9.50))
```

### 3. Partial Coverage Graphics

```python
analyzer = SignageAnalyzer(height=72, width=120)

# Full coverage substrate
analyzer.add_material(Material(
    name="Dibond",
    cost_per_sqft=14.00,
    coverage_type="full"
))

# Vinyl covers 60% of sign
analyzer.add_material(Material(
    name="Vinyl Graphics",
    cost_per_sqft=12.00,
    coverage_type="partial",
    coverage_percentage=60.0
))
```

### 4. Specific Area Coverage

```python
# 2' x 2' logo on larger sign
analyzer.add_material(Material(
    name="Metallic Vinyl Logo",
    cost_per_sqft=18.00,
    coverage_type="partial",
    coverage_area=576  # 24" x 24" = 576 sq in
))
```

## Getting Results

### Full Analysis Report

```python
result = analyzer.analyze()
print(result)  # Formatted report
```

Output includes:
- Signage dimensions and total area
- Material breakdown with costs
- Total project cost

### Cost Per Square Foot Breakdown

```python
cost_breakdown = analyzer.get_cost_per_sqft()
print(f"Total cost/sqft: ${cost_breakdown['total_cost_per_sqft_of_signage']:.2f}")
```

This shows how much each square foot of finished signage costs, useful for:
- Pricing quotes
- Comparing different material options
- Budget planning

### Dictionary Format

```python
result = analyzer.analyze()
data = result.to_dict()  # Convert to dictionary for JSON/API use
```

## Running Examples

```bash
# Basic usage
python examples/basic_usage.py

# Partial coverage example
python examples/partial_coverage.py

# Circular signage
python examples/circular_signage.py

# Multiple signs project
python examples/multiple_signs.py
```

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=signage_analyzer

# Run specific test file
pytest tests/test_analyzer.py
```

## Tips and Best Practices

1. **Material Ordering**: Add materials in logical order (substrate → graphics → laminate)

2. **Waste Factors**:
   - Simple rectangular cuts: 1.05 - 1.1 (5-10%)
   - Complex shapes/circular: 1.15 - 1.25 (15-25%)
   - Expensive materials: Be conservative with waste

3. **Partial Coverage**: Use percentages for distributed graphics, specific areas for discrete elements like logos

4. **Multiple Signs**: Create separate analyzers for different sign types, then sum totals

5. **Validation**: The tool validates inputs and raises helpful errors for invalid configurations

## API Reference

### SignageAnalyzer(height, width, shape, waste_factor)

**Parameters:**
- `height` (float, required): Height in inches (or diameter for circle)
- `width` (float, optional): Width in inches (required for rectangle)
- `shape` (str, default="rectangle"): "rectangle" or "circle"
- `waste_factor` (float, default=1.1): Waste multiplier (≥ 1.0)

**Methods:**
- `add_material(material)`: Add a Material to analyze
- `calculate_area()`: Get total area in square inches
- `analyze()`: Perform analysis and return AnalysisResult
- `get_summary()`: Get formatted string report
- `get_cost_per_sqft()`: Get per-square-foot cost breakdown

### Material(name, cost_per_sqft, coverage_type, coverage_area, coverage_percentage)

**Parameters:**
- `name` (str, required): Material name
- `cost_per_sqft` (float, required): Cost per square foot (≥ 0)
- `coverage_type` (str, default="full"): "full" or "partial"
- `coverage_area` (float, optional): Area in square inches for partial coverage
- `coverage_percentage` (float, optional): Percentage (0-100) for partial coverage

## Troubleshooting

**Error: "Width must be positive for rectangular signage"**
- Solution: Specify width parameter for rectangle shape

**Error: "No materials added"**
- Solution: Add at least one material before calling analyze()

**Error: "Partial coverage requires either coverage_area or coverage_percentage"**
- Solution: Specify one of these for partial coverage materials

**Error: "Waste factor must be >= 1.0"**
- Solution: Use waste factor ≥ 1.0 (1.1 = 10% waste)

## Support

For issues, feature requests, or questions, please create an issue in the repository.
