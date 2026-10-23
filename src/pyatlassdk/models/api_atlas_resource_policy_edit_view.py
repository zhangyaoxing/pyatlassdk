"""Generated model for ApiAtlasResourcePolicyEditView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.api_atlas_policy_create_view import ApiAtlasPolicyCreateView

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasResourcePolicyEditView(BaseModel):
    """Generated model for ApiAtlasResourcePolicyEditView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str | None = Field(default=None, description="Description of the atlas resource policy.")
    name: str | None = Field(default=None, description="Human-readable label that describes the atlas resource policy.")
    policies: list[ApiAtlasPolicyCreateView] | None = Field(default=None, description="List of policies that make up the atlas resource policy.")
