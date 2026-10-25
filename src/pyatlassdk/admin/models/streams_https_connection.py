"""Generated model for StreamsHttpsConnection. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsHttpsConnection(BaseModel):
    """Settings that define a connection to an external data store."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique identifier of the connection.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the stream connection. For the Sample type, this is the name of the sample source.")
    region: str | None = Field(default=None, description="Connection region.")
    state: Annotated[Literal["PENDING", "READY", "DELETING", "FAILED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Connection state.")
    type: Literal["Kafka", "Cluster", "Sample", "Https", "AzureBlobStorage", "AWSLambda", "AWSKinesisDataStreams", "SchemaRegistry", "GCPPubSub"] | None = Field(default=None, description="Connection type.")
    headers: dict[str, str] | None = Field(default=None, description="A map of key-value pairs that will be passed as headers for the request.")
    url: str | None = Field(default=None, description="The URL to be used for the request.")
