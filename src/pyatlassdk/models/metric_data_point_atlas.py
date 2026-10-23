"""Generated model for MetricDataPointAtlas. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MetricDataPointAtlas(BaseModel):
    """Value of, and metadata provided for, one data point generated at a particular moment in time. If no data point exists for a particular moment in time, the `value` parameter returns `null`."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    timestamp: datetime | None = Field(default=None, description="Date and time when this data point occurred. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    value: float | None = Field(default=None, description="Value that comprises this data point.")
