"""Generated model for AzureNetworkPeeringConnectionSettings. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AzureNetworkPeeringConnectionSettings(BaseModel):
    """Group of Network Peering connection settings."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    azure_directory_id: str = Field(alias="azureDirectoryId", description="Unique string that identifies the Azure AD directory in which the VNet peered with the MongoDB Cloud VNet resides.")
    azure_subscription_id: str = Field(alias="azureSubscriptionId", description="Unique string that identifies the Azure subscription in which the VNet you peered with the MongoDB Cloud VNet resides.")
    container_id: str = Field(alias="containerId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection.")
    error_state: str | None = Field(default=None, alias="errorState", description="Error message returned when a requested Azure network peering resource returns `\"status\" : \"FAILED\"`. The resource returns `null` if the request succeeded.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the network peering connection.")
    provider_name: Literal["AWS", "AZURE", "GCP"] | None = Field(default=None, alias="providerName", description="Cloud service provider that serves the requested network peering connection.")
    resource_group_name: str = Field(alias="resourceGroupName", description="Human-readable label that identifies the resource group in which the VNet to peer with the MongoDB Cloud VNet resides.")
    status: Literal["ADDING_PEER", "AVAILABLE", "FAILED", "DELETION_FAILED", "DELETING"] | None = Field(default=None, description="State of the network peering connection at the time you made the request.")
    vnet_name: str = Field(alias="vnetName", description="Human-readable label that identifies the VNet that you want to peer with the MongoDB Cloud VNet.")
