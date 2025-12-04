"""
Acrylic Composition Calculator example.
Similar to eCut plugin for CorelDRAW - calculates liquid acrylic solution composition.
"""

from signage_analyzer import (
    AcrylicCompositionCalculator,
    AcrylicFormula,
    STANDARD_FORMULAS
)


def main():
    print("=" * 70)
    print("EXAMPLE 1: Basic Rectangular Signage with Standard Formula")
    print("=" * 70)

    # Create calculator for a 4' x 8' (48" x 96") rectangular sign
    calc = AcrylicCompositionCalculator(
        height=48,
        width=96,
        shape="rectangle",
        unit="inches"
    )

    # Calculate with standard formula
    result = calc.calculate(
        formula="standard",
        num_coats=2,
        waste_factor=1.1  # 10% waste
    )

    print(result)

    print("\n" + "=" * 70)
    print("EXAMPLE 2: Circular Sign with High Gloss Formula")
    print("=" * 70)

    # Create calculator for a 36" diameter circular sign
    calc_circle = AcrylicCompositionCalculator(
        height=36,
        shape="circle",
        unit="inches"
    )

    # Calculate with high gloss formula
    result_gloss = calc_circle.calculate(
        formula="high_gloss",
        num_coats=3,
        waste_factor=1.15  # 15% waste for circular shapes
    )

    print(result_gloss)

    print("\n" + "=" * 70)
    print("EXAMPLE 3: Using Metric Measurements (cm)")
    print("=" * 70)

    # Create calculator for a 100cm x 200cm sign
    calc_metric = AcrylicCompositionCalculator(
        height=100,
        width=200,
        shape="rectangle",
        unit="cm"
    )

    result_metric = calc_metric.calculate(
        formula="outdoor",
        num_coats=2,
        waste_factor=1.1
    )

    print(result_metric)

    print("\n" + "=" * 70)
    print("EXAMPLE 4: Custom Formula")
    print("=" * 70)

    # Create a custom formula for specialty acrylic
    custom_formula = AcrylicCompositionCalculator.create_custom_formula(
        name="Custom Metallic",
        thinner_ratio=28.0,
        glue_ratio=42.0,
        color_ratio=30.0,  # Higher color ratio for metallic effect
        coverage_ml_per_sqft=38.0,  # Heavier coverage
        description="Custom formula for metallic signage"
    )

    calc_custom = AcrylicCompositionCalculator(
        height=24,
        width=48,
        unit="inches"
    )

    result_custom = calc_custom.calculate(
        formula=custom_formula,
        num_coats=2,
        waste_factor=1.1
    )

    print(result_custom)

    print("\n" + "=" * 70)
    print("EXAMPLE 5: Calculate from Known Area")
    print("=" * 70)

    # Calculate directly from a known area (e.g., 50 sq ft)
    calc_area = AcrylicCompositionCalculator(height=1, width=1, unit="feet")  # Dummy init
    result_area = calc_area.calculate_from_area(
        area_sqft=50.0,
        formula="standard",
        num_coats=2,
        waste_factor=1.1
    )

    print(result_area)

    print("\n" + "=" * 70)
    print("AVAILABLE FORMULAS")
    print("=" * 70)

    formulas = AcrylicCompositionCalculator.list_formulas()
    for name, details in formulas.items():
        print(f"\n{name}:")
        print(f"  Description: {details['description']}")
        print(f"  Thinner: {details['thinner']}")
        print(f"  Glue: {details['glue']}")
        print(f"  Color: {details['color']}")
        print(f"  Coverage: {details['coverage']}")


if __name__ == "__main__":
    main()
