"""Generated model for MetricsMeasurement. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.metric_data_point import MetricDataPoint

from pydantic import BaseModel, ConfigDict, Field

class MetricsMeasurement(BaseModel):
    """Generated model for MetricsMeasurement."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    data_points: list[MetricDataPoint] | None = Field(default=None, alias="dataPoints", description="List that contains the value of, and metadata provided for, one data point generated at a particular moment in time. If no data point exists for a particular moment in time, the `value` parameter returns `null`.")
    name: str | None = Field(default=None, description="Human-readable label of the measurement that this data point covers.")
    units: Literal["BYTES", "BYTES_PER_SECOND", "GIGABYTES", "GIGABYTES_PER_HOUR", "MEGABYTES_PER_SECOND", "MICROSECONDS", "MILLISECONDS", "PERCENT", "SCALAR", "SCALAR_PER_SECOND"] | None = Field(default=None, description="Element used to quantify the measurement. The resource returns units of throughput, storage, and time.")
