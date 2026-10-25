"""Generated model for ServerlessMetricUnits. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin._enums import CaseInsensitiveEnum

class ServerlessMetricUnits(CaseInsensitiveEnum):
    """Element used to express the quantity. This can be an element of time, storage capacity, and the like."""
    RPU = "RPU"
    THOUSAND_RPU = "THOUSAND_RPU"
    MILLION_RPU = "MILLION_RPU"
    WPU = "WPU"
    THOUSAND_WPU = "THOUSAND_WPU"
    MILLION_WPU = "MILLION_WPU"
