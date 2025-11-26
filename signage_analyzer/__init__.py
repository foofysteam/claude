"""
Signage Material Analyzer
A tool for analyzing signage dimensions and calculating material usage per square foot.
"""

from .models import Material, MaterialUsage
from .analyzer import SignageAnalyzer

__version__ = "1.0.0"
__all__ = ["SignageAnalyzer", "Material", "MaterialUsage"]
