"""Generated model for ServerlessTenantEndpointUpdate. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class ServerlessTenantEndpointUpdate(BaseModel):
    """Update view for a serverless tenant endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    comment: str | None = Field(default=None, description="Human-readable comment associated with the private endpoint.")
    provider_name: Literal["AWS", "AZURE"] = Field(alias="providerName", description="Human-readable label that identifies the cloud provider of the tenant endpoint.")
