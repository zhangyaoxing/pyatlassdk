"""Generated model for StreamsWorkspacePrivateEndpointResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsWorkspacePrivateEndpointResponse(BaseModel):
    """Customer VPC endpoint registered for inbound private connectivity to Atlas Stream Processing."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    customer_dns_name: str | None = Field(default=None, alias="customerDnsName", description="DNS name of the customer's VPC endpoint.")
    endpoint_service_name: str | None = Field(default=None, alias="endpointServiceName", description="Name of the Atlas endpoint service the customer's VPC endpoint connects to. Absent when no endpoint service is configured for the endpoint's region.")
    id: str | None = Field(default=None, description="Unique identifier of the customer's VPC endpoint.")
    provider: str | None = Field(default=None, description="Cloud provider hosting the customer's VPC endpoint.")
    region: str | None = Field(default=None, description="Human-readable label identifying the region of the customer's VPC endpoint.")
    status: Annotated[Literal["PENDING", "OK", "FAILED", "DELETING"], BeforeValidator(upper_case)] | None = Field(default=None, description="Status of the endpoint registration.")
