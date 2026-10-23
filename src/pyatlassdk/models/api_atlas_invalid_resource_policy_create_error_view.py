"""Generated model for ApiAtlasInvalidResourcePolicyCreateErrorView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.api_atlas_invalid_policy_view import ApiAtlasInvalidPolicyView

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasInvalidResourcePolicyCreateErrorView(BaseModel):
    """Generated model for ApiAtlasInvalidResourcePolicyCreateErrorView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    error_type: Annotated[Literal["POLICY_PARSING_ERROR", "POLICY_HAS_FAILED_VALIDATIONS", "POLICY_HAS_INVALID_PRINCIPAL", "POLICY_HAS_BODY_EXCEEDING_MAX_SIZE", "POLICY_HAS_UNEXPECTED_ENTITIES"], BeforeValidator(upper_case)] | None = Field(default=None, alias="errorType", description="Human-readable label that displays the type of an error.")
    invalid_policies: list[ApiAtlasInvalidPolicyView] | None = Field(default=None, alias="invalidPolicies", description="List of invalid policies containing details of their validation errors.")
