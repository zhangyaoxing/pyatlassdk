"""Generated model for ApiHostViewAtlas. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link_atlas import LinkAtlas

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiHostViewAtlas(BaseModel):
    """Generated model for ApiHostViewAtlas."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud created this MongoDB process. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project. The project contains MongoDB processes that you want to return. The MongoDB process can be either the `mongod` or `mongos`.")
    hostname: str | None = Field(default=None, description="Hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`).")
    id: str | None = Field(default=None, description="Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.")
    last_ping: datetime | None = Field(default=None, alias="lastPing", description="Date and time when MongoDB Cloud received the last ping for this MongoDB process. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    links: list[LinkAtlas] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    port: int | None = Field(default=None, description="Internet Assigned Numbers Authority (IANA) port on which the MongoDB process listens for requests.")
    replica_set_name: str | None = Field(default=None, alias="replicaSetName", description="Human-readable label that identifies the replica set that contains this process. This resource returns this parameter if this process belongs to a replica set.")
    shard_name: str | None = Field(default=None, alias="shardName", description="Human-readable label that identifies the shard that contains this process. This resource returns this value only if this process belongs to a sharded cluster.")
    type_name: Annotated[Literal["REPLICA_PRIMARY", "REPLICA_SECONDARY", "RECOVERING", "SHARD_MONGOS", "SHARD_CONFIG", "SHARD_STANDALONE", "SHARD_PRIMARY", "SHARD_SECONDARY", "NO_DATA"], BeforeValidator(upper_case)] | None = Field(default=None, alias="typeName", description="Type of MongoDB process that MongoDB Cloud tracks. MongoDB Cloud returns new processes as `NO_DATA` until MongoDB Cloud completes deploying the process.")
    user_alias: str | None = Field(default=None, alias="userAlias", description="Human-readable label that identifies the cluster node. MongoDB Cloud sets this hostname usually to the standard hostname for the cluster node. It appears in the connection string for a cluster instead of the value of the hostname parameter.")
    version: str | None = Field(default=None, description="Version of MongoDB that this process runs.")
