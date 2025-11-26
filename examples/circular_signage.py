"""
Example showing circular signage analysis.
"""

from signage_analyzer import SignageAnalyzer, Material


def main():
    print("=" * 70)
    print("EXAMPLE: Circular Signage")
    print("=" * 70)

    # Create analyzer for a 36" diameter circular sign
    analyzer = SignageAnalyzer(
        height=36,  # diameter
        shape="circle",
        waste_factor=1.2  # 20% waste for circular cuts
    )

    # Add materials
    analyzer.add_material(Material(
        name="MDO Plywood (3/4\")",
        cost_per_sqft=9.50,
        coverage_type="full"
    ))

    analyzer.add_material(Material(
        name="Exterior Paint",
        cost_per_sqft=4.25,
        coverage_type="full"
    ))

    analyzer.add_material(Material(
        name="Vinyl Lettering",
        cost_per_sqft=7.50,
        coverage_type="partial",
        coverage_percentage=30.0
    ))

    # Get analysis
    result = analyzer.analyze()
    print(result)

    # Show cost breakdown
    print("\n" + "=" * 70)
    print("COST PER SQUARE FOOT BREAKDOWN")
    print("=" * 70)
    cost_breakdown = analyzer.get_cost_per_sqft()
    print(f"\nTotal Signage Area: {cost_breakdown['total_signage_area_sqft']:.2f} sq ft")
    print(f"Total Project Cost: ${result.total_cost:.2f}")
    print(f"Cost per sq ft of signage: ${cost_breakdown['total_cost_per_sqft_of_signage']:.2f}")


if __name__ == "__main__":
    main()
