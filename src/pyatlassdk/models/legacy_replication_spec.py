"""Generated model for LegacyReplicationSpec. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.legacy_regions_config import LegacyRegionsConfig

from pydantic import BaseModel, ConfigDict, Field

class LegacyReplicationSpec(BaseModel):
    """Generated model for LegacyReplicationSpec."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the replication object for a zone in a Global Cluster.\n\n- If you include existing zones in the request, you must specify this parameter.\n\n- If you add a new zone to an existing Global Cluster, you may specify this parameter. The request deletes any existing zones in a Global Cluster that you exclude from the request.")
    num_shards: int | None = Field(default=None, alias="numShards", description="Positive integer that specifies the number of shards to deploy in each specified zone If you set this value to `1` and `clusterType` is `SHARDED`, MongoDB Cloud deploys a single-shard sharded cluster. Don't create a sharded cluster with a single shard for production environments. Single-shard sharded clusters don't provide the same benefits as multi-shard configurations.\n\n If you are upgrading a replica set to a sharded cluster, you cannot increase the number of shards in the same update request.  You should wait until after the cluster has completed upgrading to sharded and you have reconnected all application clients to the MongoDB router before adding additional shards. Otherwise, your data might become inconsistent once MongoDB Cloud begins distributing data across shards.")
    regions_config: LegacyRegionsConfig | None = Field(default=None, alias="regionsConfig")
    zone_name: str | None = Field(default=None, alias="zoneName", description="Human-readable label that identifies the zone in a Global Cluster. Provide this value only if `clusterType` is `GEOSHARDED`.")
