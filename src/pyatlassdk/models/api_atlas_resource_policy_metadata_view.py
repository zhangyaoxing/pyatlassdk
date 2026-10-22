"""Generated model for ApiAtlasResourcePolicyMetadataView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.api_atlas_policy_metadata_view import ApiAtlasPolicyMetadataView

from pydantic import BaseModel, ConfigDict, Field

class ApiAtlasResourcePolicyMetadataView(BaseModel):
    """Generated model for ApiAtlasResourcePolicyMetadataView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    policies_causing_non_compliance: list[ApiAtlasPolicyMetadataView] | None = Field(default=None, alias="policiesCausingNonCompliance", description="List of policies that are in conflict with the current state of the resource.")
    resource_policy_id: str | None = Field(default=None, alias="resourcePolicyId", description="Unique 24-hexadecimal character string that identifies the atlas resource policy.")
    resource_policy_name: str | None = Field(default=None, alias="resourcePolicyName", description="Human-readable label that describes the atlas resource policy.")
