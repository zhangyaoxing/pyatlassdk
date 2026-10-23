"""Generated model for FederationOidcWorkloadIdentityProvider. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.connected_org_config import ConnectedOrgConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FederationOidcWorkloadIdentityProvider(BaseModel):
    """Generated model for FederationOidcWorkloadIdentityProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    associated_orgs: list[ConnectedOrgConfig] | None = Field(default=None, alias="associatedOrgs", description="List that contains the connected organization configurations associated with the identity provider.")
    audience: str | None = Field(default=None, description="Identifier of the intended recipient of the token.")
    authorization_type: Annotated[Literal["GROUP", "USER"], BeforeValidator(upper_case)] | None = Field(default=None, alias="authorizationType", description="Indicates whether authorization is granted based on group membership or user ID.")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date that the identity provider was created on. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    description: str | None = Field(default=None, description="The description of the identity provider.")
    display_name: str | None = Field(default=None, alias="displayName", description="Human-readable label that identifies the identity provider.")
    groups_claim: str | None = Field(default=None, alias="groupsClaim", description="Identifier of the claim which contains IdP Group IDs in the token.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the identity provider.")
    idp_type: Annotated[Literal["WORKFORCE", "WORKLOAD"], BeforeValidator(upper_case)] | None = Field(default=None, alias="idpType", description="String enum that indicates the type of the identity provider. Default is WORKFORCE.")
    issuer_uri: str | None = Field(default=None, alias="issuerUri", description="Unique string that identifies the issuer of the SAML Assertion or OIDC metadata/discovery document URL.")
    okta_idp_id: str | None = Field(alias="oktaIdpId", description="Legacy 20-hexadecimal digit string that identifies the identity provider.")
    protocol: Annotated[Literal["SAML", "OIDC"], BeforeValidator(upper_case)] | None = Field(default=None, description="String enum that indicates the protocol of the identity provider. Either SAML or OIDC.")
    updated_at: datetime | None = Field(default=None, alias="updatedAt", description="Date that the identity provider was last updated on. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    user_claim: str | None = Field(default=None, alias="userClaim", description="Identifier of the claim which contains the user ID in the token.")
