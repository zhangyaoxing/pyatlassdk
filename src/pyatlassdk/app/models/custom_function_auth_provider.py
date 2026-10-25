"""Generated model for CustomFunctionAuthProvider. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.custom_function_auth_provider_config import CustomFunctionAuthProviderConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomFunctionAuthProvider(BaseModel):
    """Generated model for CustomFunctionAuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: Literal["custom-function"] = Field(description="The name of the authentication provider. For Custom Function authentication, this value is always `custom-function`.")
    type: Literal["custom-function"] = Field(description="The name of the authentication provider. For Custom Function authentication, this value is always `custom-function`.")
    disabled: bool | None = Field(default=None, description="If `true`, the auth provider is disabled. Users cannot log in through the provider until it is enabled.")
    config: CustomFunctionAuthProviderConfig | None = Field(default=None, description="A configuration object for the Custom Function authentication provider.")
