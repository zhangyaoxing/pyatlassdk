"""Generated model for GroupServiceAccount. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.service_account_secret import ServiceAccountSecret

from pydantic import BaseModel, ConfigDict, Field

class GroupServiceAccount(BaseModel):
    """Generated model for GroupServiceAccount."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    client_id: str | None = Field(default=None, alias="clientId", description="The Client ID of the Service Account.")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="The date that the Service Account was created on. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    description: str | None = Field(default=None, description="Human readable description for the Service Account.")
    name: str | None = Field(default=None, description="Human-readable name for the Service Account.")
    roles: list[str] | None = Field(default=None, description="A list of Project roles associated with the Service Account.")
    secrets: list[ServiceAccountSecret] | None = Field(default=None, description="A list of secrets associated with the specified Service Account.")
    system_managed: bool = Field(alias="systemManaged", description="Indicates whether the Service Account is system managed.")
