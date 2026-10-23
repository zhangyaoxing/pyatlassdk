"""Generated model for StreamsKafkaNetworkingAccess. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsKafkaNetworkingAccess(BaseModel):
    """Information about networking access."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    connection_id: str | None = Field(default=None, alias="connectionId", description="Reserved. Will be used by `PRIVATE_LINK` connection type. Setting this field with any other networking access type returns a validation error.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Reserved. Will be used by `PRIVATE_LINK` connection type.")
    tgw_route_id: str | None = Field(default=None, alias="tgwRouteId", description="Reserved. Will be used by `TRANSIT_GATEWAY` connection type.")
    type: Annotated[Literal["PUBLIC", "VPC", "PRIVATE_LINK", "TRANSIT_GATEWAY"], BeforeValidator(upper_case)] | None = Field(default=None, description="Selected networking type. Either `PUBLIC`, `VPC`, `PRIVATE_LINK`, or `TRANSIT_GATEWAY`. Defaults to `PUBLIC`. For VPC, ensure that VPC peering exists and connectivity has been established between Atlas VPC and the VPC where Kafka cluster is hosted for the connection to function properly. `TRANSIT_GATEWAY` support is coming soon.")
