"""Generated model for BaseAuthProvider. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.provider_type import ProviderType

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class BaseAuthProvider(BaseModel):
    """Generated model for BaseAuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="The name of the authentication provider. This value must be the same as the value of `type`.")
    type: ProviderType
    disabled: bool | None = Field(default=None, description="If `true`, the auth provider is disabled. Users cannot log in through the provider until it is enabled.")
