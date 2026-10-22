"""Generated model for InboundControlPlaneCloudProviderIPAddresses. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.inbound_control_plane_cloud_provider_ip_addresses_aws import InboundControlPlaneCloudProviderIPAddressesAws
from pyatlassdk.models.inbound_control_plane_cloud_provider_ip_addresses_azure import InboundControlPlaneCloudProviderIPAddressesAzure
from pyatlassdk.models.inbound_control_plane_cloud_provider_ip_addresses_gcp import InboundControlPlaneCloudProviderIPAddressesGcp

from pydantic import BaseModel, ConfigDict, Field

class InboundControlPlaneCloudProviderIPAddresses(BaseModel):
    """List of inbound IP addresses to the Atlas control plane, categorized by cloud provider. If your application allows outbound HTTP requests only to specific IP addresses, you must allow access to the following IP addresses so that your API requests can reach the Atlas control plane."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws: InboundControlPlaneCloudProviderIPAddressesAws | None = Field(default=None, description="Control plane IP addresses in AWS. Each key identifies an Amazon Web Services (AWS) region. Each value identifies control plane IP addresses in the AWS region.")
    azure: InboundControlPlaneCloudProviderIPAddressesAzure | None = Field(default=None, description="Control plane IP addresses in Azure. Each key identifies an Azure region. Each value identifies control plane IP addresses in the Azure region.")
    gcp: InboundControlPlaneCloudProviderIPAddressesGcp | None = Field(default=None, description="Control plane IP addresses in GCP. Each key identifies a Google Cloud (GCP) region. Each value identifies control plane IP addresses in the GCP region.")
