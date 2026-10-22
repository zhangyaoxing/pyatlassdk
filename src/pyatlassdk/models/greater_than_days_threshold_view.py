"""Generated model for GreaterThanDaysThresholdView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class GreaterThanDaysThresholdView(BaseModel):
    """Threshold value that triggers an alert."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    operator: Literal["GREATER_THAN"] | None = Field(default=None, description="Comparison operator to apply when checking the current metric value.")
    threshold: int | None = Field(default=None, description="Value of metric that, when exceeded, triggers an alert.")
    units: Literal["DAYS"] | None = Field(default=None, description="Element used to express the quantity. This can be an element of time, storage capacity, and the like.")
