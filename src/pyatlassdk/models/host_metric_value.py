"""Generated model for HostMetricValue. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class HostMetricValue(BaseModel):
    """Value of the metric that triggered the alert. The resource returns this parameter for alerts of events impacting hosts."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    number: float | None = Field(default=None, description="Amount of the `metricName` recorded at the time of the event. This value triggered the alert.")
    units: Literal["bits", "Kbits", "Mbits", "Gbits", "bytes", "KB", "MB", "GB", "TB", "PB", "nsec", "msec", "sec", "min", "hours", "million minutes", "days", "requests", "1000 requests", "tokens", "million tokens", "pixels", "billion pixels", "GB seconds", "GB hours", "GB days", "RPU", "thousand RPU", "million RPU", "WPU", "thousand WPU", "million WPU", "count", "thousand", "million", "billion"] | None = Field(default=None, description="Element used to express the quantity in `currentValue.number`. This can be an element of time, storage capacity, and the like. This metric triggered the alert.")
