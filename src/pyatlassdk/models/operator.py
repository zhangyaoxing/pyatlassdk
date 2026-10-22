"""Generated model for Operator. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class Operator(str, Enum):
    """Comparison operator to apply when checking the current metric value."""
    LT = "<"
    GT = ">"
