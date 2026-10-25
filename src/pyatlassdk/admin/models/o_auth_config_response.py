"""Generated model for OAuthConfigResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.o_auth_signing_key_info import OAuthSigningKeyInfo

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OAuthConfigResponse(BaseModel):
    """OAuth 2.0 configuration returned for a metric integration. Secrets are never returned."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_auth_method: Annotated[Literal["CLIENT_SECRET", "PRIVATE_KEY_JWT"], BeforeValidator(upper_case)] = Field(alias="clientAuthMethod", description="How the client authenticates to the token endpoint.")
    client_id: str = Field(alias="clientId", description="OAuth 2.0 client identifier registered with the token endpoint.")
    scopes: list[str] | None = Field(default=None, description="OAuth 2.0 scopes requested on the token.")
    signing_key_info: OAuthSigningKeyInfo | None = Field(default=None, alias="signingKeyInfo")
    token_endpoint: str = Field(alias="tokenEndpoint", description="OAuth 2.0 token endpoint URL.")
    token_request_params: dict[str, str] | None = Field(default=None, alias="tokenRequestParams", description="Provider-specific parameters added to the token request.")
