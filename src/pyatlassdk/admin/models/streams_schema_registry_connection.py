"""Generated model for StreamsSchemaRegistryConnection. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.link import Link
from pyatlassdk.admin.models.schema_registry_authentication import SchemaRegistryAuthentication

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsSchemaRegistryConnection(BaseModel):
    """The configuration for Schema Registry connections."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique identifier of the connection.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the stream connection. For the Sample type, this is the name of the sample source.")
    region: str | None = Field(default=None, description="Connection region.")
    state: Annotated[Literal["PENDING", "READY", "DELETING", "FAILED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Connection state.")
    type: Literal["Kafka", "Cluster", "Sample", "Https", "AzureBlobStorage", "AWSLambda", "AWSKinesisDataStreams", "SchemaRegistry", "GCPPubSub"] | None = Field(default=None, description="Connection type.")
    provider: Annotated[Literal["CONFLUENT"], BeforeValidator(upper_case)] = Field(description="The Schema Registry provider.")
    schema_registry_authentication: SchemaRegistryAuthentication = Field(alias="schemaRegistryAuthentication")
    schema_registry_urls: list[str] = Field(alias="schemaRegistryUrls", description="List of Schema Registry endpoint URLs used by this connection. Each URL must use the http or https scheme and specify a valid host and optional port.")
