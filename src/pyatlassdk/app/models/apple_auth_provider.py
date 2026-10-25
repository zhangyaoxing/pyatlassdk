"""Generated model for AppleAuthProvider. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.apple_auth_provider_config import AppleAuthProviderConfig
from pyatlassdk.app.models.apple_auth_provider_secret_config import AppleAuthProviderSecretConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AppleAuthProvider(BaseModel):
    """Generated model for AppleAuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: Literal["oauth2-apple"] = Field(description="The name of the authentication provider. For Apple authentication, this value is always `oauth2-apple`.")
    type: Literal["oauth2-apple"] = Field(description="The name of the authentication provider. For Apple authentication, this value is always `oauth2-apple`.")
    disabled: bool | None = Field(default=None, description="If `true`, the auth provider is disabled. Users cannot log in through the provider until it is enabled.")
    config: AppleAuthProviderConfig | None = Field(default=None, description="A configuration object for the Apple authentication provider.")
    secret_config: AppleAuthProviderSecretConfig | None = None
    redirect_uris: list[str] | None = None
