"""Generated model for HostMatcher. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.host_matcher_field import HostMatcherField
from pyatlassdk.admin.models.matcher_host_type import MatcherHostType

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class HostMatcher(BaseModel):
    """Rules to apply when comparing an host against this alert configuration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    field_name: HostMatcherField = Field(alias="fieldName")
    operator: Annotated[Literal["EQUALS", "CONTAINS", "STARTS_WITH", "ENDS_WITH", "NOT_EQUALS", "NOT_CONTAINS", "REGEX"], BeforeValidator(upper_case)] = Field(description="Comparison operator to apply when checking the current metric value against **matcher[n].value**. The `REGEX` operator only supports inclusive matches. Use the `NOT_CONTAINS` operator to exclude values.")
    value: MatcherHostType | None = None
