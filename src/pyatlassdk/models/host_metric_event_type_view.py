"""Generated model for HostMetricEventTypeView. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class HostMetricEventTypeView(str, Enum):
    """Unique identifier of event type."""
    INSIDE_METRIC_THRESHOLD = "INSIDE_METRIC_THRESHOLD"
    OUTSIDE_METRIC_THRESHOLD = "OUTSIDE_METRIC_THRESHOLD"
