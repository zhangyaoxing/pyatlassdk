"""Generated model for StreamsFailoverKafkaConnection. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_failover_kafka_connection_config import StreamsFailoverKafkaConnectionConfig
from pyatlassdk.models.streams_kafka_authentication import StreamsKafkaAuthentication
from pyatlassdk.models.streams_kafka_networking import StreamsKafkaNetworking
from pyatlassdk.models.streams_kafka_security import StreamsKafkaSecurity

from pydantic import BaseModel, ConfigDict, Field

class StreamsFailoverKafkaConnection(BaseModel):
    """Settings that define a failover connection to an external data store."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique identifier of the connection.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the stream connection.")
    region: str | None = Field(default=None, description="Connection region.")
    state: Literal["PENDING", "READY", "DELETING", "FAILED"] | None = Field(default=None, description="Connection state.")
    type: Literal["Kafka", "Cluster"] | None = Field(default=None, description="Connection type.")
    authentication: StreamsKafkaAuthentication | None = None
    bootstrap_servers: str | None = Field(default=None, alias="bootstrapServers", description="Comma separated list of server addresses.")
    config: StreamsFailoverKafkaConnectionConfig | None = Field(default=None, description="Map of Kafka key-value pairs for optional configuration. This object is flat, and keys can have '.' characters.")
    networking: StreamsKafkaNetworking | None = None
    security: StreamsKafkaSecurity | None = None
