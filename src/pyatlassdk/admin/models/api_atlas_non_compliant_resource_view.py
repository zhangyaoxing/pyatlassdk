"""Generated model for ApiAtlasNonCompliantResourceView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.api_atlas_resource_policy_metadata_view import ApiAtlasResourcePolicyMetadataView

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasNonCompliantResourceView(BaseModel):
    """Generated model for ApiAtlasNonCompliantResourceView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal character string that identifies the organization the resource belongs to.")
    resource_id: str | None = Field(default=None, alias="resourceId", description="Unique 24-hexadecimal character string that identifies the non-compliant resource.")
    resource_name: str | None = Field(default=None, alias="resourceName", description="Unique human readable string that identifies the non-compliant resource.")
    resource_policies_causing_non_compliance: list[ApiAtlasResourcePolicyMetadataView] | None = Field(default=None, alias="resourcePoliciesCausingNonCompliance", description="List of resource policies causing the resource to be considered non-compliant.")
    resource_type: Annotated[Literal["DEPRECATED_PROJECT", "DEPRECATED_CLUSTER", "PROJECT", "CLUSTER"], BeforeValidator(upper_case)] | None = Field(default=None, alias="resourceType", description="Human-readable label that displays the type of a resource.")
