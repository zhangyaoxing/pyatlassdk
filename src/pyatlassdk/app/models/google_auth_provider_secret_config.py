"""Generated model for GoogleAuthProviderSecretConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GoogleAuthProviderSecretConfig(BaseModel):
    """Generated model for GoogleAuthProviderSecretConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_secret: str | None = Field(default=None, alias="clientSecret", description="The name of a\n[Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/)\nthat holds the OAuth 2.0 Client Secret for the Client ID\nspecified in `config.clientId`.")
