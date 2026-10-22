"""Generated model for AwsNetworkPeeringConnectionSettings. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AwsNetworkPeeringConnectionSettings(BaseModel):
    """Group of Network Peering connection settings."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    accepter_region_name: str = Field(alias="accepterRegionName", description="Amazon Web Services (AWS) region where the Virtual Peering Connection (VPC) that you peered with the MongoDB Cloud VPC resides. The resource returns `null` if your VPC and the MongoDB Cloud VPC reside in the same region.")
    aws_account_id: str = Field(alias="awsAccountId", description="Unique twelve-digit string that identifies the Amazon Web Services (AWS) account that owns the VPC that you peered with the MongoDB Cloud VPC.")
    connection_id: str | None = Field(default=None, alias="connectionId", description="Unique string that identifies the peering connection on AWS.")
    container_id: str = Field(alias="containerId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection.")
    error_state_name: Literal["REJECTED", "EXPIRED", "INVALID_ARGUMENT"] | None = Field(default=None, alias="errorStateName", description="Type of error that can be returned when requesting an Amazon Web Services (AWS) peering connection. The resource returns `null` if the request succeeded.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the network peering connection.")
    provider_name: Literal["AWS", "AZURE", "GCP"] | None = Field(default=None, alias="providerName", description="Cloud service provider that serves the requested network peering connection.")
    route_table_cidr_block: str = Field(alias="routeTableCidrBlock", description="Internet Protocol (IP) addresses expressed in Classless Inter-Domain Routing (CIDR) notation of the VPC's subnet that you want to peer with the MongoDB Cloud VPC.")
    status_name: Literal["INITIATING", "PENDING_ACCEPTANCE", "FAILED", "FINALIZING", "AVAILABLE", "TERMINATING"] | None = Field(default=None, alias="statusName", description="State of the network peering connection at the time you made the request.")
    vpc_id: str = Field(alias="vpcId", description="Unique string that identifies the VPC on Amazon Web Services (AWS) that you want to peer with the MongoDB Cloud VPC.")
