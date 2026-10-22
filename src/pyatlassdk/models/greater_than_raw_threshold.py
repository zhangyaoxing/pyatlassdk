"""Generated model for GreaterThanRawThreshold. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.raw_metric_units import RawMetricUnits

from pydantic import BaseModel, ConfigDict, Field

class GreaterThanRawThreshold(BaseModel):
    """A Limit that triggers an alert when greater than a number."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    operator: Literal["GREATER_THAN"] | None = Field(default=None, description="Comparison operator to apply when checking the current metric value.")
    threshold: int | None = Field(default=None, description="Value of metric that, when exceeded, triggers an alert.")
    units: RawMetricUnits | None = None
