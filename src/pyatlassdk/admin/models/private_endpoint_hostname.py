"""Generated model for PrivateEndpointHostname. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PrivateEndpointHostname(BaseModel):
    """Set of Private endpoint and hostnames."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    hostname: str | None = Field(default=None, description="Human-readable label that identifies the hostname.")
    private_endpoint: str | None = Field(default=None, alias="privateEndpoint", description="Human-readable label that identifies private endpoint.")
