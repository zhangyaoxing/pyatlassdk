"""Generated model for VPCPeeringActionChallenge. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class VPCPeeringActionChallenge(BaseModel):
    """Container for elements used to challenge the user before taking certain actions on VPC Peering connections."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    requester_account_id: str | None = Field(default=None, alias="requesterAccountId", description="The AWS requester account ID.")
    requester_vpc_id: str | None = Field(default=None, alias="requesterVpcId", description="The AWS requester VPC ID.")
