"""Generated model for StreamsKafkaConnection. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_kafka_authentication import StreamsKafkaAuthentication
from pyatlassdk.models.streams_kafka_networking import StreamsKafkaNetworking
from pyatlassdk.models.streams_kafka_security import StreamsKafkaSecurity

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsKafkaConnection(BaseModel):
    """Settings that define a connection to an external data store."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique identifier of the connection.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the stream connection. For the Sample type, this is the name of the sample source.")
    region: str | None = Field(default=None, description="Connection region.")
    state: Annotated[Literal["PENDING", "READY", "DELETING", "FAILED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Connection state.")
    type: Literal["Kafka", "Cluster", "Sample", "Https", "AzureBlobStorage", "AWSLambda", "AWSKinesisDataStreams", "SchemaRegistry", "GCPPubSub"] | None = Field(default=None, description="Connection type.")
    authentication: StreamsKafkaAuthentication | None = None
    bootstrap_servers: str | None = Field(default=None, alias="bootstrapServers", description="Comma separated list of server addresses.")
    config: dict[str, str] | None = Field(default=None, description="Map of Kafka key-value pairs for optional configuration. This object is flat, and keys can have '.' characters.")
    networking: StreamsKafkaNetworking | None = None
    security: StreamsKafkaSecurity | None = None
