"""Generated model for StreamsClusterConnection. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.db_role_to_execute import DBRoleToExecute
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsClusterConnection(BaseModel):
    """Settings that define a connection to an external data store."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique identifier of the connection.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the stream connection. For the Sample type, this is the name of the sample source.")
    region: str | None = Field(default=None, description="Connection region.")
    state: Annotated[Literal["PENDING", "READY", "DELETING", "FAILED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Connection state.")
    type: Literal["Kafka", "Cluster", "Sample", "Https", "AzureBlobStorage", "AWSLambda", "AWSKinesisDataStreams", "SchemaRegistry", "GCPPubSub"] | None = Field(default=None, description="Connection type.")
    cluster_group_id: str | None = Field(default=None, alias="clusterGroupId", description="Unique 24-hexadecimal digit string that identifies the project that contains the configured cluster. Required if the ID does not match the project containing the streams workspace. You must first enable the organization setting.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Name of the cluster configured for this connection.")
    db_role_to_execute: DBRoleToExecute | None = Field(default=None, alias="dbRoleToExecute")
