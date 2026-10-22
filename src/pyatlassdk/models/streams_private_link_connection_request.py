"""Generated model for StreamsPrivateLinkConnectionRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class StreamsPrivateLinkConnectionRequest(BaseModel):
    """Request body for updating a Private Link connection."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    dns_domain: str | None = Field(default=None, alias="dnsDomain", description="The domain hostname for the AWS Confluent Serverless Private Link connection. Allowed only when no domain is currently set, or when the connection is in `IDLE` state.")
