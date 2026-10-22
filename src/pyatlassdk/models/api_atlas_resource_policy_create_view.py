"""Generated model for ApiAtlasResourcePolicyCreateView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.api_atlas_policy_create_view import ApiAtlasPolicyCreateView

from pydantic import BaseModel, ConfigDict, Field

class ApiAtlasResourcePolicyCreateView(BaseModel):
    """Generated model for ApiAtlasResourcePolicyCreateView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str | None = Field(default=None, description="Description of the atlas resource policy.")
    name: str = Field(description="Human-readable label that describes the atlas resource policy.")
    policies: list[ApiAtlasPolicyCreateView] = Field(description="List of policies that make up the atlas resource policy.")
