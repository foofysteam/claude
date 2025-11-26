"""
Basic usage example for Signage Material Analyzer.
"""

from signage_analyzer import SignageAnalyzer, Material


def main():
    print("=" * 70)
    print("EXAMPLE 1: Basic Rectangular Signage")
    print("=" * 70)

    # Create analyzer for a 4' x 8' (48" x 96") rectangular sign
    analyzer = SignageAnalyzer(
        height=48,
        width=96,
        waste_factor=1.1  # 10% waste
    )

    # Add materials
    analyzer.add_material(Material(
        name="Aluminum Composite Panel (3mm)",
        cost_per_sqft=12.50,
        coverage_type="full"
    ))

    analyzer.add_material(Material(
        name="Vinyl Graphics",
        cost_per_sqft=8.75,
        coverage_type="full"
    ))

    # Get analysis
    result = analyzer.analyze()
    print(result)

    # Get cost per square foot breakdown
    print("\n" + "=" * 70)
    print("COST PER SQUARE FOOT BREAKDOWN")
    print("=" * 70)
    cost_breakdown = analyzer.get_cost_per_sqft()
    print(f"\nTotal Signage Area: {cost_breakdown['total_signage_area_sqft']:.2f} sq ft")
    print(f"\nMaterials:")
    for material in cost_breakdown['materials']:
        print(f"  {material['name']}:")
        print(f"    Material Cost: ${material['material_cost_per_sqft']:.2f}/sq ft")
        print(f"    Cost per sq ft of signage: ${material['cost_per_sqft_of_signage']:.2f}")
    print(f"\nTotal Cost per sq ft of signage: ${cost_breakdown['total_cost_per_sqft_of_signage']:.2f}")


if __name__ == "__main__":
    main()
