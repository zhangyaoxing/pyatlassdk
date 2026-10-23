"""Generated model for ControlPlaneIPAddresses. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.gateway import Gateway
from pyatlassdk.models.inbound_control_plane_cloud_provider_ip_addresses import InboundControlPlaneCloudProviderIPAddresses
from pyatlassdk.models.outbound_control_plane_cloud_provider_ip_addresses import OutboundControlPlaneCloudProviderIPAddresses

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ControlPlaneIPAddresses(BaseModel):
    """List of IP addresses in the Atlas control plane."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    gateways: list[Gateway] | None = Field(default=None, description="List of gateways, each representing a group of service-specific IP addresses that customers can add to their allow lists independently. Includes the Atlas Gateway (data plane) group when present.")
    inbound: InboundControlPlaneCloudProviderIPAddresses | None = None
    outbound: OutboundControlPlaneCloudProviderIPAddresses | None = None
