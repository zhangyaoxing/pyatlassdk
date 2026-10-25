"""Generated model for AppServiceMetricMatcher. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.app_service_metric_matcher_field import AppServiceMetricMatcherField

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AppServiceMetricMatcher(BaseModel):
    """Rules to apply when comparing an app service metric against this alert configuration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    field_name: AppServiceMetricMatcherField = Field(alias="fieldName")
    operator: Annotated[Literal["EQUALS", "CONTAINS", "STARTS_WITH", "ENDS_WITH", "NOT_EQUALS", "NOT_CONTAINS", "REGEX"], BeforeValidator(upper_case)] = Field(description="Comparison operator to apply when checking the current metric value against **matcher[n].value**. The `REGEX` operator only supports inclusive matches. Use the `NOT_CONTAINS` operator to exclude values.")
    value: str = Field(description="Value to match or exceed using the specified `matchers.operator`.")
