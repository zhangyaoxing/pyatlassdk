"""Generated model for AppleAuthProviderSecretConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AppleAuthProviderSecretConfig(BaseModel):
    """Generated model for AppleAuthProviderSecretConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_secret: str | None = Field(default=None, alias="clientSecret", description="The name of a\n[Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/)\nthat holds your client secret JWT.\n\nTo learn how to create this, see [Create the Client Secret JWT](https://www.mongodb.com/docs/atlas/app-services/authentication/apple/#create-the-client-secret-jwt).")
