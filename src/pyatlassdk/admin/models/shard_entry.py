"""Generated model for ShardEntry. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.shard_keys import ShardKeys

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ShardEntry(BaseModel):
    """Sharding configuration for a collection to be sharded on the destination cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection: str = Field(description="Human-readable label that identifies the collection to be sharded on the destination cluster.")
    database: str = Field(description="Human-readable label that identifies the database that contains the collection to be sharded on the destination cluster.")
    shard_collection: ShardKeys = Field(alias="shardCollection")
