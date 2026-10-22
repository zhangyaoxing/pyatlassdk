"""Generated model for FederationSamlIdentityProviderUpdate. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.pem_file_info_update import PemFileInfoUpdate

from pydantic import BaseModel, ConfigDict, Field

class FederationSamlIdentityProviderUpdate(BaseModel):
    """Generated model for FederationSamlIdentityProviderUpdate."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    associated_domains: list[str] | None = Field(default=None, alias="associatedDomains", description="List that contains the domains associated with the identity provider.")
    description: str | None = Field(default=None, description="The description of the identity provider.")
    display_name: str | None = Field(default=None, alias="displayName", description="Human-readable label that identifies the identity provider.")
    idp_type: Literal["WORKFORCE", "WORKLOAD"] | None = Field(default=None, alias="idpType", description="String enum that indicates the type of the identity provider. Default is WORKFORCE.")
    issuer_uri: str | None = Field(default=None, alias="issuerUri", description="Unique string that identifies the issuer of the SAML Assertion or OIDC metadata/discovery document URL.")
    pem_file_info: PemFileInfoUpdate | None = Field(default=None, alias="pemFileInfo")
    protocol: Literal["SAML", "OIDC"] | None = Field(default=None, description="String enum that indicates the protocol of the identity provider. Either SAML or OIDC.")
    request_binding: Literal["HTTP-POST", "HTTP-REDIRECT"] | None = Field(default=None, alias="requestBinding", description="SAML Authentication Request Protocol HTTP method binding (POST or REDIRECT) that Federated Authentication uses to send the authentication request.")
    response_signature_algorithm: Literal["SHA-1", "SHA-256"] | None = Field(default=None, alias="responseSignatureAlgorithm", description="Signature algorithm that Federated Authentication uses to encrypt the identity provider signature.")
    slug: str | None = Field(default=None, description="Custom SSO URL for the identity provider.")
    sso_debug_enabled: bool = Field(alias="ssoDebugEnabled", description="Flag that indicates whether the identity provider has SSO debug enabled.")
    sso_url: str | None = Field(default=None, alias="ssoUrl", description="URL that points to the receiver of the SAML authentication request.")
    status: Literal["ACTIVE", "INACTIVE"] | None = Field(default=None, description="String enum that indicates whether the identity provider is active.")
