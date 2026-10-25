"""Generated model for GroupMigrationRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GroupMigrationRequest(BaseModel):
    """Generated model for GroupMigrationRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    destination_org_id: str | None = Field(default=None, alias="destinationOrgId", description="Unique 24-hexadecimal digit string that identifies the organization to move the specified project to.")
    destination_org_private_api_key: str | None = Field(default=None, alias="destinationOrgPrivateApiKey", description="Unique string that identifies the private part of the API Key used to verify access to the destination organization. This parameter is required only when you authenticate with Programmatic API Keys.")
    destination_org_public_api_key: str | None = Field(default=None, alias="destinationOrgPublicApiKey", description="Unique string that identifies the public part of the API Key used to verify access to the destination organization. This parameter is required only when you authenticate with Programmatic API Keys.")
