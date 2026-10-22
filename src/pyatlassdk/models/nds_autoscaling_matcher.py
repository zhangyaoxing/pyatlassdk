"""Generated model for NDSAutoscalingMatcher. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.nds_autoscaling_matcher_field import NDSAutoscalingMatcherField

from pydantic import BaseModel, ConfigDict, Field

class NDSAutoscalingMatcher(BaseModel):
    """Rules to apply when comparing a cluster against this alert configuration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    field_name: NDSAutoscalingMatcherField = Field(alias="fieldName")
    operator: Literal["EQUALS", "CONTAINS", "STARTS_WITH", "ENDS_WITH", "NOT_EQUALS", "NOT_CONTAINS", "REGEX"] = Field(description="Comparison operator to apply when checking the current metric value against **matcher[n].value**. The `REGEX` operator only supports inclusive matches. Use the `NOT_CONTAINS` operator to exclude values.")
    value: str = Field(description="Value to match or exceed using the specified `matchers.operator`.")
