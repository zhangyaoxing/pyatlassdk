"""Generated model for ConnectedOrgConfig. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.auth_federation_role_mapping import AuthFederationRoleMapping
from pyatlassdk.models.federated_user import FederatedUser

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ConnectedOrgConfig(BaseModel):
    """Generated model for ConnectedOrgConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    data_access_identity_provider_ids: list[str] | None = Field(default=None, alias="dataAccessIdentityProviderIds", description="The collection of unique ids representing the identity providers that can be used for data access in this organization.")
    domain_allow_list: list[str] | None = Field(default=None, alias="domainAllowList", description="Approved domains that restrict users who can join the organization based on their email address.")
    domain_restriction_enabled: bool = Field(alias="domainRestrictionEnabled", description="Value that indicates whether domain restriction is enabled for this connected organization.")
    identity_provider_id: str | None = Field(default=None, alias="identityProviderId", description="Legacy 20-hexadecimal digit string that identifies the UI access identity provider that this connected organization configuration is associated with. This id can be found within the Federation Management Console > Identity Providers tab by clicking the info icon in the IdP ID row of a configured identity provider.")
    instant_user_provisioning_disabled: bool | None = Field(default=None, alias="instantUserProvisioningDisabled", description="Flag that indicates whether instant user provisioning is disabled for this connected organization.")
    org_id: str = Field(alias="orgId", description="Unique 24-hexadecimal digit string that identifies the connected organization configuration.")
    post_auth_role_grants: list[Annotated[Literal["ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY"], BeforeValidator(upper_case)]] | None = Field(default=None, alias="postAuthRoleGrants", description="Atlas roles that are granted to a user in this organization after authenticating. Roles are a human-readable label that identifies the collection of privileges that MongoDB Cloud grants a specific MongoDB Cloud user. These roles can only be organization specific roles.")
    role_mappings: list[AuthFederationRoleMapping] | None = Field(default=None, alias="roleMappings", description="Role mappings that are configured in this organization.")
    user_conflicts: list[FederatedUser] | None = Field(default=None, alias="userConflicts", description="List that contains the users who have an email address that doesn't match any domain on the allowed list.")
