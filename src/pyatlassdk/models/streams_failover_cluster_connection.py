"""Generated model for StreamsFailoverClusterConnection. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.db_role_to_execute import DBRoleToExecute
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class StreamsFailoverClusterConnection(BaseModel):
    """Settings that define a failover connection to an external data store."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique identifier of the connection.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the stream connection.")
    region: str | None = Field(default=None, description="Connection region.")
    state: Literal["PENDING", "READY", "DELETING", "FAILED"] | None = Field(default=None, description="Connection state.")
    type: Literal["Kafka", "Cluster"] | None = Field(default=None, description="Connection type.")
    cluster_group_id: str | None = Field(default=None, alias="clusterGroupId", description="Unique 24-hexadecimal digit string that identifies the project that contains the configured cluster. Required if the ID does not match the project containing the streams workspace. You must first enable the organization setting.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Name of the cluster configured for this connection.")
    db_role_to_execute: DBRoleToExecute | None = Field(default=None, alias="dbRoleToExecute")
