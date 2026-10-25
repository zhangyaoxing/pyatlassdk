"""Generated model for ShardingRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.shard_entry import ShardEntry

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ShardingRequest(BaseModel):
    """Document that configures sharding on the destination cluster when migrating from a replica set source to a sharded cluster destination on MongoDB 6.0 or higher. If you don't wish to shard any collections on the destination cluster, leave this empty."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    create_supporting_indexes: bool = Field(alias="createSupportingIndexes", description="Flag that lets the migration create supporting indexes for the shard keys, if none exists, as the destination cluster also needs compatible indexes for the specified shard keys.")
    sharding_entries: list[ShardEntry] = Field(alias="shardingEntries", description="List of shard configurations to shard destination collections. Atlas shards only those collections that you include in the sharding entries array.")
