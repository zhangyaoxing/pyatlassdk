"""Generated model for ApiKeyUserDetails. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.cloud_access_role_assignment import CloudAccessRoleAssignment
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiKeyUserDetails(BaseModel):
    """Details of the Programmatic API Keys."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    desc: str | None = Field(default=None, description="Purpose or explanation provided when someone created this organization API key.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this organization API key assigned to this project.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    private_key: str | None = Field(default=None, alias="privateKey", description="Redacted private key returned for this organization API key. This key displays unredacted when first created.")
    public_key: str | None = Field(default=None, alias="publicKey", description="Public API key value set for the specified organization API key.")
    roles: list[CloudAccessRoleAssignment] | None = Field(default=None, description="List that contains the roles that the API key needs to have. All roles you provide must be valid for the specified project or organization. Each request must include a minimum of one valid role. The resource returns all project and organization roles assigned to the API key.")
