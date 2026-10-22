"""Generated model for AlertsThresholdInteger. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.operator import Operator

from pydantic import BaseModel, ConfigDict, Field

class AlertsThresholdInteger(BaseModel):
    """A Limit that triggers an alert when exceeded. The resource returns this parameter when `eventTypeName` has not been set to `OUTSIDE_METRIC_THRESHOLD`."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    operator: Operator | None = None
    threshold: int | None = Field(default=None, description="Value of metric that, when exceeded, triggers an alert.")
    units: Literal["bits", "Kbits", "Mbits", "Gbits", "bytes", "KB", "MB", "GB", "TB", "PB", "nsec", "msec", "sec", "min", "hours", "million minutes", "days", "requests", "1000 requests", "tokens", "million tokens", "pixels", "billion pixels", "GB seconds", "GB hours", "GB days", "RPU", "thousand RPU", "million RPU", "WPU", "thousand WPU", "million WPU", "count", "thousand", "million", "billion"] | None = Field(default=None, description="Element used to express the quantity. This can be an element of time, storage capacity, and the like.")
