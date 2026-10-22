"""Generated model for AzureAccountDetails. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class AzureAccountDetails(BaseModel):
    """Generated model for AzureAccountDetails."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    azure_subscription_id: str | None = Field(default=None, alias="azureSubscriptionId", description="The Azure Subscription ID.")
    cidr_block: str | None = Field(default=None, alias="cidrBlock", description="The VPC CIDR Block.")
    cloud_provider: str | None = Field(default=None, alias="cloudProvider", description="Cloud provider.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    virtual_network_name: str | None = Field(default=None, alias="virtualNetworkName", description="The name of the virtual network.")
