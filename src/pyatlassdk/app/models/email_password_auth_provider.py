"""Generated model for EmailPasswordAuthProvider. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.email_password_auth_provider_config_variant1 import EmailPasswordAuthProviderConfigVariant1
from pyatlassdk.app.models.email_password_auth_provider_config_variant2 import EmailPasswordAuthProviderConfigVariant2
from pyatlassdk.app.models.email_password_auth_provider_config_variant3 import EmailPasswordAuthProviderConfigVariant3
from pyatlassdk.app.models.email_password_auth_provider_config_variant4 import EmailPasswordAuthProviderConfigVariant4
from pyatlassdk.app.models.email_password_auth_provider_config_variant5 import EmailPasswordAuthProviderConfigVariant5
from pyatlassdk.app.models.email_password_auth_provider_config_variant6 import EmailPasswordAuthProviderConfigVariant6

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EmailPasswordAuthProvider(BaseModel):
    """Generated model for EmailPasswordAuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: Literal["local-userpass"] = Field(description="The name of the authentication provider. For Email/Password authentication, this value is always `local-userpass`.")
    type: Literal["local-userpass"] = Field(description="The name of the authentication provider. For Email/Password authentication, this value is always `local-userpass`.")
    disabled: bool | None = Field(default=None, description="If `true`, the auth provider is disabled. Users cannot log in through the provider until it is enabled.")
    config: EmailPasswordAuthProviderConfigVariant1 | EmailPasswordAuthProviderConfigVariant2 | EmailPasswordAuthProviderConfigVariant3 | EmailPasswordAuthProviderConfigVariant4 | EmailPasswordAuthProviderConfigVariant5 | EmailPasswordAuthProviderConfigVariant6 | None = None
