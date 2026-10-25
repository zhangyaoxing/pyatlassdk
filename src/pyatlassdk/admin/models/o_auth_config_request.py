"""Generated model for OAuthConfigRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OAuthConfigRequest(BaseModel):
    """OAuth 2.0 client credentials configuration. Required when `authType` is `OAUTH2`. Secrets are never returned."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_auth_method: Annotated[Literal["CLIENT_SECRET", "PRIVATE_KEY_JWT"], BeforeValidator(upper_case)] = Field(alias="clientAuthMethod", description="How the client authenticates to the token endpoint. `CLIENT_SECRET` sends a shared secret. `PRIVATE_KEY_JWT` signs a client assertion with an Atlas-generated, Atlas-managed key. Register the returned JWKS URL with your identity provider.")
    client_id: str = Field(alias="clientId", description="OAuth 2.0 client identifier registered with the token endpoint.")
    client_secret: str | None = Field(default=None, alias="clientSecret", description="Shared client secret. Required when `clientAuthMethod` is `CLIENT_SECRET`, and rejected for `PRIVATE_KEY_JWT`. Encrypted at rest and never returned.")
    scopes: list[str] | None = Field(default=None, description="Optional OAuth 2.0 scopes requested on the token, sent as a space delimited `scope` parameter. Applies to both client authentication methods.")
    token_endpoint: str = Field(alias="tokenEndpoint", description="OAuth 2.0 token endpoint URL. Must use HTTPS.")
    token_request_params: dict[str, str] | None = Field(default=None, alias="tokenRequestParams", description="Optional provider-specific parameters added to the token request, for example a resource indicator. Applies to both client authentication methods.")
