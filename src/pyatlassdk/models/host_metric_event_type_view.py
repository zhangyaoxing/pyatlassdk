"""Generated model for HostMetricEventTypeView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class HostMetricEventTypeView(CaseInsensitiveEnum):
    """Unique identifier of event type."""
    INSIDE_METRIC_THRESHOLD = "INSIDE_METRIC_THRESHOLD"
    OUTSIDE_METRIC_THRESHOLD = "OUTSIDE_METRIC_THRESHOLD"
