"""Generated model for PrivateEndpointCreate. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PrivateEndpointCreate(BaseModel):
    """Generated model for PrivateEndpointCreate."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider_region: str = Field(description="The cloud provider region that hosts the private endpoint.")
    cloud_provider_endpoint_id: str = Field(description="The private endpoint ID from the cloud provider.")
    comment: str | None = Field(default=None, description="An optional comment that describes the endpoint.")
    endpoint_type: Literal["sync", "general"] = Field(description="The type of endpoint. For more information\non endpoint types and migrating deprecated endpoints to `\"general\"` or `\"sync\"`, \nsee [Use a VPC Private Endpoint](https://www.mongodb.com/docs/atlas/app-services/security/private-endpoints).")
