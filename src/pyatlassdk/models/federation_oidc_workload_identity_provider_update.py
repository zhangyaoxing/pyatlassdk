"""Generated model for FederationOidcWorkloadIdentityProviderUpdate. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class FederationOidcWorkloadIdentityProviderUpdate(BaseModel):
    """Generated model for FederationOidcWorkloadIdentityProviderUpdate."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    audience: str | None = Field(default=None, description="Identifier of the intended recipient of the token.")
    authorization_type: Literal["GROUP", "USER"] | None = Field(default=None, alias="authorizationType", description="Indicates whether authorization is granted based on group membership or user ID.")
    description: str | None = Field(default=None, description="The description of the identity provider.")
    display_name: str | None = Field(default=None, alias="displayName", description="Human-readable label that identifies the identity provider.")
    groups_claim: str | None = Field(default=None, alias="groupsClaim", description="Identifier of the claim which contains IdP Group IDs in the token.")
    idp_type: Literal["WORKFORCE", "WORKLOAD"] | None = Field(default=None, alias="idpType", description="String enum that indicates the type of the identity provider. Default is WORKFORCE.")
    issuer_uri: str | None = Field(default=None, alias="issuerUri", description="Unique string that identifies the issuer of the SAML Assertion or OIDC metadata/discovery document URL.")
    protocol: Literal["SAML", "OIDC"] | None = Field(default=None, description="String enum that indicates the protocol of the identity provider. Either SAML or OIDC.")
    user_claim: str | None = Field(default=None, alias="userClaim", description="Identifier of the claim which contains the user ID in the token.")
