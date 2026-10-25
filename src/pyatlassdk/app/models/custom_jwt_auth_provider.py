"""Generated model for CustomJwtAuthProvider. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.custom_jwt_auth_provider_config import CustomJwtAuthProviderConfig
from pyatlassdk.app.models.custom_jwt_auth_provider_metadata_fields_item import CustomJwtAuthProviderMetadataFieldsItem
from pyatlassdk.app.models.custom_jwt_auth_provider_secret_config import CustomJwtAuthProviderSecretConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomJwtAuthProvider(BaseModel):
    """Generated model for CustomJwtAuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: Literal["custom-token"] = Field(description="The name of the authentication provider. For Custom JWT authentication, this value is always `custom-token`.")
    type: Literal["custom-token"] = Field(description="The name of the authentication provider. For Custom JWT authentication, this value is always `custom-token`.")
    disabled: bool | None = Field(default=None, description="If `true`, the auth provider is disabled. Users cannot log in through the provider until it is enabled.")
    config: CustomJwtAuthProviderConfig | None = Field(default=None, description="A configuration object for the Custom JWT authentication provider.")
    secret_config: CustomJwtAuthProviderSecretConfig | None = None
    metadata_fields: list[CustomJwtAuthProviderMetadataFieldsItem] | None = Field(default=None, description="Metadata fields are additional data that describe each\nuser. The value of each metadata field comes from some\nfield included in the JWT from the external\nauthentication system.\n\nA user's metadata fields refresh whenever they log in.")
