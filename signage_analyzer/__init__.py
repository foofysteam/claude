"""
Signage Material Analyzer
A tool for analyzing signage dimensions and calculating material usage per square foot.

Includes:
- SignageAnalyzer: Calculate material usage and costs
- AcrylicCompositionCalculator: Calculate liquid acrylic solution composition
  (thinner, glue, color) similar to eCut plugin for CorelDRAW
"""

from .models import Material, MaterialUsage, AnalysisResult
from .analyzer import SignageAnalyzer
from .acrylic_models import AcrylicFormula, AcrylicComposition, STANDARD_FORMULAS
from .acrylic_calculator import AcrylicCompositionCalculator

__version__ = "1.1.0"
__all__ = [
    # Original signage analyzer
    "SignageAnalyzer",
    "Material",
    "MaterialUsage",
    "AnalysisResult",
    # Acrylic composition calculator
    "AcrylicCompositionCalculator",
    "AcrylicFormula",
    "AcrylicComposition",
    "STANDARD_FORMULAS",
]
