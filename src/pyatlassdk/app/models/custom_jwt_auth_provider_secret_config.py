"""Generated model for CustomJwtAuthProviderSecretConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomJwtAuthProviderSecretConfig(BaseModel):
    """Generated model for CustomJwtAuthProviderSecretConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    signing_keys: list[str] | None = Field(default=None, alias="signingKeys")
