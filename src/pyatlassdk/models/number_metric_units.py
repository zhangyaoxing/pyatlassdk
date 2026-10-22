"""Generated model for NumberMetricUnits. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class NumberMetricUnits(str, Enum):
    """Element used to express the quantity. This can be an element of time, storage capacity, and the like."""
    COUNT = "COUNT"
    THOUSAND = "THOUSAND"
    MILLION = "MILLION"
    BILLION = "BILLION"
