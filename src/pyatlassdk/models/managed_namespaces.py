"""Generated model for ManagedNamespaces. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ManagedNamespaces(BaseModel):
    """Generated model for ManagedNamespaces."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection: str = Field(description="Human-readable label of the collection to manage for this Global Cluster.")
    custom_shard_key: str = Field(alias="customShardKey", description="Database parameter used to divide the *collection* into shards. Global clusters require a compound shard key. This compound shard key combines the location parameter and the user-selected custom key.")
    db: str = Field(description="Human-readable label of the database to manage for this Global Cluster.")
    is_custom_shard_key_hashed: bool | None = Field(default=None, alias="isCustomShardKeyHashed", description="Flag that indicates whether someone hashed the custom shard key for the specified collection. If you set this value to `false`, MongoDB Cloud uses ranged sharding.")
    is_shard_key_unique: bool | None = Field(default=None, alias="isShardKeyUnique", description="Flag that indicates whether someone [hashed](https://www.mongodb.com/docs/manual/reference/method/sh.shardCollection/#hashed-shard-keys) the custom shard key. If this parameter returns `false`, this cluster uses [ranged sharding](https://www.mongodb.com/docs/manual/core/ranged-sharding/).")
    num_initial_chunks: int | None = Field(default=None, alias="numInitialChunks", description="Minimum number of chunks to create initially when sharding an empty collection with a [hashed shard key](https://www.mongodb.com/docs/manual/core/hashed-sharding/).")
    presplit_hashed_zones: bool | None = Field(default=None, alias="presplitHashedZones", description="Flag that indicates whether MongoDB Cloud should create and distribute initial chunks for an empty or non-existing collection. MongoDB Cloud distributes data based on the defined zones and zone ranges for the collection.")
