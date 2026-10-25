"""Generated model for Gateway. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.gateway_ip_addresses import GatewayIpAddresses

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Gateway(BaseModel):
    """Represents a service-specific gateway, such as the Atlas Gateway, with its IP addresses."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ips: GatewayIpAddresses | None = None
    name: str | None = Field(default=None, description="Name of the service that this gateway represents.")
