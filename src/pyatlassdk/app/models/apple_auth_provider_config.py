"""Generated model for AppleAuthProviderConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AppleAuthProviderConfig(BaseModel):
    """Generated model for AppleAuthProviderConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_id: str | None = Field(default=None, alias="clientId", description="Your Apple Services ID.\n\nTo learn how to get this, see [Create a Services ID](https://www.mongodb.com/docs/atlas/app-services/authentication/apple/#create-a-services-id).")
