"""Generated model for ApiKey. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.access_list_item_view import AccessListItemView
from pyatlassdk.models.cloud_access_role_assignment import CloudAccessRoleAssignment

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiKey(BaseModel):
    """Details contained in one API key."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    access_list: list[AccessListItemView] = Field(alias="accessList", description="List of network addresses granted access to this API using this API key.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies this organization API key.")
    public_key: str = Field(alias="publicKey", description="Public API key value set for the specified organization API key.")
    roles: list[CloudAccessRoleAssignment] = Field(description="List that contains roles that the API key needs to have. All roles you provide must be valid for the specified project or organization. Each request must include a minimum of one valid role. The resource returns all project and organization roles assigned to the Cloud user.")
