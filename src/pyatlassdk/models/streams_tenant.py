"""Generated model for StreamsTenant. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link
from pyatlassdk.models.stream_config import StreamConfig
from pyatlassdk.models.streams_connection import StreamsConnection
from pyatlassdk.models.streams_data_process_region import StreamsDataProcessRegion
from pyatlassdk.models.streams_sample_connections import StreamsSampleConnections

from pydantic import BaseModel, ConfigDict, Field

class StreamsTenant(BaseModel):
    """Generated model for StreamsTenant."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal character string that identifies the project.")
    connections: list[StreamsConnection] | None = Field(default=None, description="List of connections configured in the stream workspace.")
    data_process_region: StreamsDataProcessRegion | None = Field(default=None, alias="dataProcessRegion")
    failover_regions: list[StreamsDataProcessRegion] | None = Field(default=None, alias="failoverRegions", description="List of failover regions configured for the stream workspace.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    hostnames: list[str] | None = Field(default=None, description="List that contains the hostnames assigned to the stream workspace.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Label that identifies the stream workspace.")
    sample_connections: StreamsSampleConnections | None = Field(default=None, alias="sampleConnections")
    stream_config: StreamConfig | None = Field(default=None, alias="streamConfig")
