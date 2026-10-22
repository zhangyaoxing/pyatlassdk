"""Generated model for FederationSamlIdentityProvider. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.connected_org_config import ConnectedOrgConfig
from pyatlassdk.models.pem_file_info import PemFileInfo

from pydantic import BaseModel, ConfigDict, Field

class FederationSamlIdentityProvider(BaseModel):
    """Generated model for FederationSamlIdentityProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    acs_url: str | None = Field(default=None, alias="acsUrl", description="URL that points to where to send the SAML response.")
    associated_domains: list[str] | None = Field(default=None, alias="associatedDomains", description="List that contains the domains associated with the identity provider.")
    associated_orgs: list[ConnectedOrgConfig] | None = Field(default=None, alias="associatedOrgs", description="List that contains the connected organization configurations associated with the identity provider.")
    audience_uri: str | None = Field(default=None, alias="audienceUri", description="Unique string that identifies the intended audience of the SAML assertion.")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date that the identity provider was created on. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    description: str | None = Field(default=None, description="The description of the identity provider.")
    display_name: str | None = Field(default=None, alias="displayName", description="Human-readable label that identifies the identity provider.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the identity provider.")
    idp_type: Literal["WORKFORCE", "WORKLOAD"] | None = Field(default=None, alias="idpType", description="String enum that indicates the type of the identity provider. Default is WORKFORCE.")
    issuer_uri: str | None = Field(default=None, alias="issuerUri", description="Unique string that identifies the issuer of the SAML Assertion or OIDC metadata/discovery document URL.")
    okta_idp_id: str | None = Field(alias="oktaIdpId", description="Legacy 20-hexadecimal digit string that identifies the identity provider.")
    pem_file_info: PemFileInfo | None = Field(default=None, alias="pemFileInfo")
    protocol: Literal["SAML", "OIDC"] | None = Field(default=None, description="String enum that indicates the protocol of the identity provider. Either SAML or OIDC.")
    request_binding: Literal["HTTP-POST", "HTTP-REDIRECT"] | None = Field(default=None, alias="requestBinding", description="SAML Authentication Request Protocol HTTP method binding (POST or REDIRECT) that Federated Authentication uses to send the authentication request.")
    response_signature_algorithm: Literal["SHA-1", "SHA-256"] | None = Field(default=None, alias="responseSignatureAlgorithm", description="Signature algorithm that Federated Authentication uses to encrypt the identity provider signature.")
    slug: str | None = Field(default=None, description="Custom SSO URL for the identity provider.")
    sso_debug_enabled: bool | None = Field(default=None, alias="ssoDebugEnabled", description="Flag that indicates whether the identity provider has SSO debug enabled.")
    sso_url: str | None = Field(default=None, alias="ssoUrl", description="URL that points to the receiver of the SAML authentication request.")
    status: Literal["ACTIVE", "INACTIVE"] | None = Field(default=None, description="String enum that indicates whether the identity provider is active.")
    updated_at: datetime | None = Field(default=None, alias="updatedAt", description="Date that the identity provider was last updated on. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
