"""
Example showing partial coverage materials.
"""

from signage_analyzer import SignageAnalyzer, Material


def main():
    print("=" * 70)
    print("EXAMPLE: Signage with Partial Coverage Materials")
    print("=" * 70)

    # Create analyzer for a 6' x 10' (72" x 120") rectangular sign
    analyzer = SignageAnalyzer(
        height=72,
        width=120,
        waste_factor=1.15  # 15% waste
    )

    # Full coverage substrate
    analyzer.add_material(Material(
        name="Dibond Substrate",
        cost_per_sqft=14.00,
        coverage_type="full"
    ))

    # Partial coverage - 60% of the sign has vinyl graphics
    analyzer.add_material(Material(
        name="Premium Vinyl Graphics",
        cost_per_sqft=12.00,
        coverage_type="partial",
        coverage_percentage=60.0
    ))

    # Partial coverage - specific area for logo
    analyzer.add_material(Material(
        name="Metallic Vinyl Logo",
        cost_per_sqft=18.00,
        coverage_type="partial",
        coverage_area=288  # 2' x 2' logo = 24" x 24" = 576 sq in / 2 = 288 sq in
    ))

    # Laminate over graphics only (60% coverage)
    analyzer.add_material(Material(
        name="UV Laminate",
        cost_per_sqft=6.50,
        coverage_type="partial",
        coverage_percentage=60.0
    ))

    # Get analysis
    result = analyzer.analyze()
    print(result)


if __name__ == "__main__":
    main()
