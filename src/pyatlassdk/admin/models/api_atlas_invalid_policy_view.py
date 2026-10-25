"""Generated model for ApiAtlasInvalidPolicyView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.api_atlas_invalid_policy_error_detail_view import ApiAtlasInvalidPolicyErrorDetailView

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasInvalidPolicyView(BaseModel):
    """Generated model for ApiAtlasInvalidPolicyView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    body: str | None = Field(default=None, description="A string that defines the permissions for the policy. The syntax used is the Cedar Policy language.")
    errors: list[ApiAtlasInvalidPolicyErrorDetailView] | None = Field(default=None, description="List of validation errors.")
