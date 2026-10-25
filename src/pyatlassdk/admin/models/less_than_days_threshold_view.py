"""Generated model for LessThanDaysThresholdView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LessThanDaysThresholdView(BaseModel):
    """Threshold value that triggers an alert."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    operator: Annotated[Literal["LESS_THAN"], BeforeValidator(upper_case)] | None = Field(default=None, description="Comparison operator to apply when checking the current metric value.")
    threshold: int | None = Field(default=None, description="Value of metric that, when exceeded, triggers an alert.")
    units: Annotated[Literal["DAYS"], BeforeValidator(upper_case)] | None = Field(default=None, description="Element used to express the quantity. This can be an element of time, storage capacity, and the like.")
