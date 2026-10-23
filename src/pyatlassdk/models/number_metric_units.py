"""Generated model for NumberMetricUnits. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class NumberMetricUnits(CaseInsensitiveEnum):
    """Element used to express the quantity. This can be an element of time, storage capacity, and the like."""
    COUNT = "COUNT"
    THOUSAND = "THOUSAND"
    MILLION = "MILLION"
    BILLION = "BILLION"
