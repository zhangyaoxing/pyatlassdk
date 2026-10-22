"""Generated model for AlertMatcher. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AlertMatcher(BaseModel):
    """Rules to apply when comparing an target instance against this alert configuration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    field_name: str = Field(alias="fieldName", description="Name of the parameter in the target object that MongoDB Cloud checks. The parameter must match all rules for MongoDB Cloud to check for alert configurations.")
    operator: Literal["EQUALS", "CONTAINS", "STARTS_WITH", "ENDS_WITH", "NOT_EQUALS", "NOT_CONTAINS", "REGEX"] = Field(description="Comparison operator to apply when checking the current metric value against **matcher[n].value**. The `REGEX` operator only supports inclusive matches. Use the `NOT_CONTAINS` operator to exclude values.")
    value: str = Field(description="Value to match or exceed using the specified `matchers.operator`.")
