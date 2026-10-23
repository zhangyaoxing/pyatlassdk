"""Generated model for DbDataSizeTotalDataMetricThresholdView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.data_metric_units import DataMetricUnits

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DbDataSizeTotalDataMetricThresholdView(BaseModel):
    """Generated model for DbDataSizeTotalDataMetricThresholdView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    metric_name: str = Field(alias="metricName", description="Human-readable label that identifies the metric against which MongoDB Cloud checks the configured `metricThreshold.threshold`.")
    mode: Annotated[Literal["AVERAGE"], BeforeValidator(upper_case)] | None = Field(default=None, description="MongoDB Cloud computes the current metric value as an average.")
    operator: Annotated[Literal["LESS_THAN", "GREATER_THAN"], BeforeValidator(upper_case)] | None = Field(default=None, description="Comparison operator to apply when checking the current metric value.")
    threshold: float | None = Field(default=None, description="Value of metric that, when exceeded, triggers an alert.")
    units: DataMetricUnits | None = None
