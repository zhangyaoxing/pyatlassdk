"""Generated model for FacebookAuthProvider. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.facebook_auth_provider_config import FacebookAuthProviderConfig
from pyatlassdk.app.models.facebook_auth_provider_metadata_fields_item_item import FacebookAuthProviderMetadataFieldsItemItem
from pyatlassdk.app.models.facebook_auth_provider_secret_config import FacebookAuthProviderSecretConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FacebookAuthProvider(BaseModel):
    """Generated model for FacebookAuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: Literal["oauth2-facebook"] = Field(description="The name of the authentication provider. For Facebook authentication, this value is always `oauth2-facebook`.")
    type: Literal["oauth2-facebook"] = Field(description="The name of the authentication provider. For Facebook authentication, this value is always `oauth2-facebook`.")
    disabled: bool | None = Field(default=None, description="If `true`, the auth provider is disabled. Users cannot log in through the provider until it is enabled.")
    config: FacebookAuthProviderConfig | None = Field(default=None, description="A configuration object for the Facebook authentication provider.")
    secret_config: FacebookAuthProviderSecretConfig | None = None
    redirect_uris: list[str] | None = None
    metadata_fields: list[list[FacebookAuthProviderMetadataFieldsItemItem]] | None = None
    domain_restrictions: list[str] | None = None
