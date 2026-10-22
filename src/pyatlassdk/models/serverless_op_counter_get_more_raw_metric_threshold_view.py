"""Generated model for ServerlessOpCounterGetMoreRawMetricThresholdView. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.raw_metric_units import RawMetricUnits

from pydantic import BaseModel, ConfigDict, Field

class ServerlessOpCounterGetMoreRawMetricThresholdView(BaseModel):
    """Generated model for ServerlessOpCounterGetMoreRawMetricThresholdView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    metric_name: str = Field(alias="metricName", description="Human-readable label that identifies the metric against which MongoDB Cloud checks the configured `metricThreshold.threshold`.")
    mode: Literal["AVERAGE"] | None = Field(default=None, description="MongoDB Cloud computes the current metric value as an average.")
    operator: Literal["LESS_THAN", "GREATER_THAN"] | None = Field(default=None, description="Comparison operator to apply when checking the current metric value.")
    threshold: float | None = Field(default=None, description="Value of metric that, when exceeded, triggers an alert.")
    units: RawMetricUnits | None = None
