"""Generated model for VPCPeeringConnection. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class VPCPeeringConnection(BaseModel):
    """Represents a VPC Peering connection on AWS."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Internal VPC Peering Connection ID.")
    accepter_account_id: str | None = Field(default=None, alias="accepterAccountId", description="The account ID responsible for accepting the request.")
    accepter_cidr: str | None = Field(default=None, alias="accepterCidr", description="The CIDR block for the accepter VPC.")
    accepter_vpc_id: str | None = Field(default=None, alias="accepterVpcId", description="The VPC ID accepting the request.")
    cloud_status: str | None = Field(default=None, alias="cloudStatus", description="The status in the cloud provider for this connection.")
    expiration_time: datetime | None = Field(default=None, alias="expirationTime", description="The time when the VPC Peering Connection request expires. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: str | None = Field(default=None, alias="groupId", description="The internal project ID.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    local_status: Literal["NONE", "SCAN_FAILED", "UPDATE_FAILED", "REQUEST_ACCEPT", "ACCEPT_REQUESTED", "REQUEST_REJECT", "REJECT_REQUESTED", "REQUEST_DELETE", "DELETE_REQUESTED", "ACTIVE"] | None = Field(default=None, alias="localStatus", description="The local status of the VPC Peering Connection.")
    name: str | None = Field(default=None, description="Unique VPC Peering Connection name.")
    requester_account_id: str | None = Field(default=None, alias="requesterAccountId", description="The account ID requesting the VPC Peering connection.")
    requester_cidr: str | None = Field(default=None, alias="requesterCidr", description="The CIDR block for the requesting VPC.")
    requester_vpc_id: str | None = Field(default=None, alias="requesterVpcId", description="The VPC ID requesting the VPC Peering connection.")
    status_message: str | None = Field(default=None, alias="statusMessage", description="A status message.")
