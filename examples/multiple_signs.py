"""
Example showing analysis of multiple signs in a project.
"""

from signage_analyzer import SignageAnalyzer, Material


def analyze_sign(name, height, width, materials):
    """Helper function to analyze a single sign."""
    print(f"\n{'=' * 70}")
    print(f"ANALYZING: {name}")
    print('=' * 70)

    analyzer = SignageAnalyzer(height=height, width=width, waste_factor=1.1)

    for mat_data in materials:
        analyzer.add_material(Material(**mat_data))

    result = analyzer.analyze()
    print(result)

    return result.total_cost


def main():
    print("=" * 70)
    print("MULTIPLE SIGNS PROJECT ANALYSIS")
    print("=" * 70)

    total_project_cost = 0.0

    # Main entrance sign
    cost1 = analyze_sign(
        name="Main Entrance Sign (8' x 4')",
        height=48,
        width=96,
        materials=[
            {"name": "Aluminum Composite", "cost_per_sqft": 12.50},
            {"name": "Vinyl Graphics", "cost_per_sqft": 8.75},
            {"name": "LED Lighting", "cost_per_sqft": 15.00, "coverage_type": "partial", "coverage_percentage": 40}
        ]
    )
    total_project_cost += cost1

    # Directional signs (smaller)
    cost2 = analyze_sign(
        name="Directional Sign (2' x 3')",
        height=24,
        width=36,
        materials=[
            {"name": "PVC Panel", "cost_per_sqft": 8.00},
            {"name": "Vinyl Text", "cost_per_sqft": 6.50, "coverage_type": "partial", "coverage_percentage": 50}
        ]
    )
    # Multiply by 4 for 4 directional signs
    total_project_cost += cost2 * 4

    # Summary
    print("\n" + "=" * 70)
    print("PROJECT SUMMARY")
    print("=" * 70)
    print(f"\n1 Main Entrance Sign: ${cost1:.2f}")
    print(f"4 Directional Signs: ${cost2:.2f} x 4 = ${cost2 * 4:.2f}")
    print(f"\nTOTAL PROJECT COST: ${total_project_cost:.2f}")
    print("=" * 70)


if __name__ == "__main__":
    main()
