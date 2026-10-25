"""Generated model for GoogleAuthProviderConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GoogleAuthProviderConfig(BaseModel):
    """Generated model for GoogleAuthProviderConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_id: str | None = Field(default=None, alias="clientId", description="An OAuth 2.0 Client ID for your GCP project.\n\nTo learn how to create one, see [Set Up a Project in\nthe Google API\nConsole](https://www.mongodb.com/docs/atlas/app-services/authentication/google/#std-label-auth-gcp-project-setup).")
    open_id: bool | None = Field(default=None, alias="openId", description="An OAuth 2.0")
