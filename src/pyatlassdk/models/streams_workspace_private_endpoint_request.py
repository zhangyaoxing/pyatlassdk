"""Generated model for StreamsWorkspacePrivateEndpointRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class StreamsWorkspacePrivateEndpointRequest(BaseModel):
    """Customer VPC endpoint to register for inbound private connectivity to Atlas Stream Processing."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    customer_dns_name: str = Field(alias="customerDnsName", description="DNS name of the customer's VPC endpoint.")
    id: str = Field(description="Unique identifier of the customer's VPC endpoint.")
    region: str = Field(description="Human-readable label identifying the region of the customer's VPC endpoint.")
