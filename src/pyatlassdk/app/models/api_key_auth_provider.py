"""Generated model for ApiKeyAuthProvider. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiKeyAuthProvider(BaseModel):
    """Generated model for ApiKeyAuthProvider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: Literal["api-key"] = Field(description="The name of the authentication provider. For API key authentication, this value is always `api-key`.")
    type: Literal["api-key"] = Field(description="The name of the authentication provider. For API key authentication, this value is always `api-key`.")
    disabled: bool | None = Field(default=None, description="If `true`, the auth provider is disabled. Users cannot log in through the provider until it is enabled.")
