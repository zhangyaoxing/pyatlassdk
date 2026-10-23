"""Generated model for AuthFederationRoleMapping. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.connected_org_config_role_assignment import ConnectedOrgConfigRoleAssignment

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuthFederationRoleMapping(BaseModel):
    """Mapping settings that link one IdP and MongoDB Cloud."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    external_group_name: str = Field(alias="externalGroupName", description="Unique human-readable label that identifies the identity provider group to which this role mapping applies.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this role mapping.")
    role_assignments: list[ConnectedOrgConfigRoleAssignment] = Field(alias="roleAssignments", description="Atlas roles and the unique identifiers of the groups and organizations associated with each role. The array must include at least one element with an Organization role and its respective `orgId`. Each element in the array can have a value for `orgId` or `groupId`, but not both.")
