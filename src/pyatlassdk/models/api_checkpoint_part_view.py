"""Generated model for ApiCheckpointPartView. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.api_bson_timestamp_view import ApiBSONTimestampView

from pydantic import BaseModel, ConfigDict, Field

class ApiCheckpointPartView(BaseModel):
    """Metadata contained in one document that describes the complete snapshot taken for this node."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    replica_set_name: str | None = Field(default=None, alias="replicaSetName", description="Human-readable label that identifies the replica set to which this checkpoint applies.")
    shard_name: str | None = Field(default=None, alias="shardName", description="Human-readable label that identifies the shard to which this checkpoint applies.")
    token_discovered: bool | None = Field(default=None, alias="tokenDiscovered", description="Flag that indicates whether the token exists.")
    token_timestamp: ApiBSONTimestampView | None = Field(default=None, alias="tokenTimestamp")
    type_name: Literal["REPLICA_SET", "CONFIG_SERVER", "CONFIG_SERVER_REPLICA_SET"] | None = Field(default=None, alias="typeName", description="Human-readable label that identifies the type of host that the part represents.")
