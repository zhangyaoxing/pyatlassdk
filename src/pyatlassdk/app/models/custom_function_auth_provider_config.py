"""Generated model for CustomFunctionAuthProviderConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomFunctionAuthProviderConfig(BaseModel):
    """Generated model for CustomFunctionAuthProviderConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auth_function_name: str | None = Field(default=None, alias="authFunctionName", description="The name of the [custom authentication\nfunction](https://www.mongodb.com/docs/atlas/app-services/authentication/custom-function/#the-authentication-function)\nthat handles user logins.")
