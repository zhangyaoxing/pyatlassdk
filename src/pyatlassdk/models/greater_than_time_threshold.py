"""Generated model for GreaterThanTimeThreshold. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.time_metric_units import TimeMetricUnits

from pydantic import BaseModel, ConfigDict, Field

class GreaterThanTimeThreshold(BaseModel):
    """A Limit that triggers an alert when greater than a time period."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    operator: Literal["GREATER_THAN"] | None = Field(default=None, description="Comparison operator to apply when checking the current metric value.")
    threshold: int | None = Field(default=None, description="Value of metric that, when exceeded, triggers an alert.")
    units: TimeMetricUnits | None = None
