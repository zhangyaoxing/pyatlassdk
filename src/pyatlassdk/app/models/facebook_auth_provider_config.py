"""Generated model for FacebookAuthProviderConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FacebookAuthProviderConfig(BaseModel):
    """Generated model for FacebookAuthProviderConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_id: str | None = Field(default=None, alias="clientId", description="The App ID of your Facebook app.")
