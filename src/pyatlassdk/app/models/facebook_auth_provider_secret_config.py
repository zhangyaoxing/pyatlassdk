"""Generated model for FacebookAuthProviderSecretConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FacebookAuthProviderSecretConfig(BaseModel):
    """Generated model for FacebookAuthProviderSecretConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_secret: str | None = Field(default=None, alias="clientSecret", description="The name of a\n[Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/)\nthat holds your Facebook App Secret.")
