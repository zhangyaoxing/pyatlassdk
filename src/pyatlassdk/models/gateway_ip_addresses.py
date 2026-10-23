"""Generated model for GatewayIpAddresses. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.inbound_control_plane_cloud_provider_ip_addresses import InboundControlPlaneCloudProviderIPAddresses
from pyatlassdk.models.outbound_control_plane_cloud_provider_ip_addresses import OutboundControlPlaneCloudProviderIPAddresses

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GatewayIpAddresses(BaseModel):
    """IP addresses for a specific gateway, organized by direction and cloud provider."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    inbound: InboundControlPlaneCloudProviderIPAddresses | None = None
    outbound: OutboundControlPlaneCloudProviderIPAddresses | None = None
