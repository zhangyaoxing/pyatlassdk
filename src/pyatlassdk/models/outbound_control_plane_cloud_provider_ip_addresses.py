"""Generated model for OutboundControlPlaneCloudProviderIPAddresses. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.outbound_control_plane_cloud_provider_ip_addresses_aws import OutboundControlPlaneCloudProviderIPAddressesAws
from pyatlassdk.models.outbound_control_plane_cloud_provider_ip_addresses_azure import OutboundControlPlaneCloudProviderIPAddressesAzure
from pyatlassdk.models.outbound_control_plane_cloud_provider_ip_addresses_gcp import OutboundControlPlaneCloudProviderIPAddressesGcp

from pydantic import BaseModel, ConfigDict, Field

class OutboundControlPlaneCloudProviderIPAddresses(BaseModel):
    """List of outbound IP addresses from the Atlas control plane, categorized by cloud provider. If your network allows inbound HTTP requests only from specific IP addresses, you must allow access from the following IP addresses so that Atlas can communicate with your webhooks and KMS."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws: OutboundControlPlaneCloudProviderIPAddressesAws | None = Field(default=None, description="Control plane IP addresses in AWS. Each key identifies an Amazon Web Services (AWS) region. Each value identifies control plane IP addresses in the AWS region.")
    azure: OutboundControlPlaneCloudProviderIPAddressesAzure | None = Field(default=None, description="Control plane IP addresses in Azure. Each key identifies an Azure region. Each value identifies control plane IP addresses in the Azure region.")
    gcp: OutboundControlPlaneCloudProviderIPAddressesGcp | None = Field(default=None, description="Control plane IP addresses in GCP. Each key identifies a Google Cloud (GCP) region. Each value identifies control plane IP addresses in the GCP region.")
