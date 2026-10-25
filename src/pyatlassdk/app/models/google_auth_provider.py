"""Generated model for GoogleAuthProvider. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.google_auth_provider_config import GoogleAuthProviderConfig
from pyatlassdk.app.models.google_auth_provider_metadata_fields_item_item import GoogleAuthProviderMetadataFieldsItemItem
from pyatlassdk.app.models.google_auth_provider_secret_config import GoogleAuthProviderSecretConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GoogleAuthProvider(BaseModel):
    """Generated model for GoogleAuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: Literal["oauth2-google"] = Field(description="The name of the authentication provider. For Google authentication, this value is always `oauth2-google`.")
    type: Literal["oauth2-google"] = Field(description="The name of the authentication provider. For Google authentication, this value is always `oauth2-google`.")
    disabled: bool | None = Field(default=None, description="If `true`, the auth provider is disabled. Users cannot log in through the provider until it is enabled.")
    config: GoogleAuthProviderConfig | None = Field(default=None, description="A configuration object for the Google authentication provider.")
    secret_config: GoogleAuthProviderSecretConfig | None = None
    redirect_uris: list[str] | None = None
    metadata_fields: list[list[GoogleAuthProviderMetadataFieldsItemItem]] | None = None
    domain_restrictions: list[str] | None = None
