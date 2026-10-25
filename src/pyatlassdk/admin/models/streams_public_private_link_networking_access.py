"""Generated model for StreamsPublicPrivateLinkNetworkingAccess. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsPublicPrivateLinkNetworkingAccess(BaseModel):
    """Information about networking access."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    connection_id: str | None = Field(default=None, alias="connectionId", description="The ID of the Private Link connection. Required for `PRIVATE_LINK` type. For GCP connections using Private Service Connect (PSC), this is the PSC connection ID.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    type: Annotated[Literal["PUBLIC", "PRIVATE_LINK"], BeforeValidator(upper_case)] | None = Field(default=None, description="Selected networking type. Either `PUBLIC` or `PRIVATE_LINK`. Defaults to `PUBLIC`. For AWS, Azure, and GCP connections, use `PRIVATE_LINK` for AWS PrivateLink, Azure Private Link, or GCP Private Service Connect (PSC) respectively.")
