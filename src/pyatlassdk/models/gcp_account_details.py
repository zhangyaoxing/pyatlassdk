"""Generated model for GCPAccountDetails. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GCPAccountDetails(BaseModel):
    """Generated model for GCPAccountDetails."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cidr_block: str | None = Field(default=None, alias="cidrBlock", description="The VPC CIDR Block.")
    cloud_provider: str | None = Field(default=None, alias="cloudProvider", description="Cloud provider.")
    gcp_project_id: str | None = Field(default=None, alias="gcpProjectId", description="The GCP Project ID.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    vpc_network_name: str | None = Field(default=None, alias="vpcNetworkName", description="The name of the VPC network.")
