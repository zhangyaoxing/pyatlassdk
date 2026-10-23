"""Generated model for StreamsGCPPubSubConnection. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_gcp_connection_config import StreamsGCPConnectionConfig
from pyatlassdk.models.streams_public_private_link_networking import StreamsPublicPrivateLinkNetworking

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsGCPPubSubConnection(BaseModel):
    """The configuration for GCP Pub/Sub connections."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique identifier of the connection.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the stream connection. For the Sample type, this is the name of the sample source.")
    region: str | None = Field(default=None, description="Connection region.")
    state: Annotated[Literal["PENDING", "READY", "DELETING", "FAILED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Connection state.")
    type: Literal["Kafka", "Cluster", "Sample", "Https", "AzureBlobStorage", "AWSLambda", "AWSKinesisDataStreams", "SchemaRegistry", "GCPPubSub"] | None = Field(default=None, description="Connection type.")
    gcp: StreamsGCPConnectionConfig | None = None
    public_private_networking: StreamsPublicPrivateLinkNetworking | None = Field(default=None, alias="publicPrivateNetworking")
