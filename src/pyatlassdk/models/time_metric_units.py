"""Generated model for TimeMetricUnits. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class TimeMetricUnits(CaseInsensitiveEnum):
    """Element used to express the quantity. This can be an element of time, storage capacity, and the like."""
    NANOSECONDS = "NANOSECONDS"
    MILLISECONDS = "MILLISECONDS"
    MILLION_MINUTES = "MILLION_MINUTES"
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
