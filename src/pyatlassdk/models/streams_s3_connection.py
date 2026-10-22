"""Generated model for StreamsS3Connection. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_aws_connection_config import StreamsAWSConnectionConfig
from pyatlassdk.models.streams_kafka_networking import StreamsKafkaNetworking

from pydantic import BaseModel, ConfigDict, Field

class StreamsS3Connection(BaseModel):
    """The configuration for S3 connections."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique identifier of the connection.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the stream connection. For the Sample type, this is the name of the sample source.")
    region: str | None = Field(default=None, description="Connection region.")
    state: Literal["PENDING", "READY", "DELETING", "FAILED"] | None = Field(default=None, description="Connection state.")
    type: Literal["Kafka", "Cluster", "Sample", "Https", "AzureBlobStorage", "AWSLambda", "AWSKinesisDataStreams", "SchemaRegistry", "GCPPubSub"] | None = Field(default=None, description="Connection type.")
    aws: StreamsAWSConnectionConfig | None = None
    networking: StreamsKafkaNetworking | None = None
