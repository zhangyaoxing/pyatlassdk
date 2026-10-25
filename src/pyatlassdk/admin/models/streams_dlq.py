"""Generated model for StreamsDLQ. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsDLQ(BaseModel):
    """Dead letter queue for the stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    coll: str | None = Field(default=None, description="Name of the collection to use for the DLQ.")
    connection_name: str | None = Field(default=None, alias="connectionName", description="Name of the connection to write DLQ messages to. Must be an Atlas connection.")
    db: str | None = Field(default=None, description="Name of the database to use for the DLQ.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
