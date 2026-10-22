"""Generated model for ReplicationSpec20240805. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.cloud_region_config20240805 import CloudRegionConfig20240805

from pydantic import BaseModel, ConfigDict, Field

class ReplicationSpec20240805(BaseModel):
    """Details that explain how MongoDB Cloud replicates data on the specified MongoDB database."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the replication object for a shard in a Cluster. If you include existing shard replication configurations in the request, you must specify this parameter. If you add a new shard to an existing Cluster, you may specify this parameter. The request deletes any existing shards  in the Cluster that you exclude from the request. This corresponds to Shard ID displayed in the UI.")
    region_configs: list[CloudRegionConfig20240805] | None = Field(default=None, alias="regionConfigs", description="Hardware specifications for nodes set for a given region. Each `regionConfigs` object must be unique by region and cloud provider within the `replicationSpec`. Each `regionConfigs` object describes the region's priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each `regionConfigs` object must have either an `analyticsSpecs` object, `electableSpecs` object, or `readOnlySpecs` object. Tenant clusters only require `electableSpecs`. Dedicated clusters can specify any of these specifications, but must have at least one `electableSpecs` object within a `replicationSpec`.\n\n**Example:**\n\nIf you set `replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize` : `M30`, set `replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize` : `M30` if you have electable nodes and `replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize` : `M30` if you have read-only nodes.")
    zone_id: str | None = Field(default=None, alias="zoneId", description="Unique 24-hexadecimal digit string that identifies the zone in a Global Cluster. This value can be used to configure Global Cluster backup policies.")
    zone_name: str | None = Field(default=None, alias="zoneName", description="Human-readable label that describes the zone this shard belongs to in a Global Cluster. Provide this value only if `clusterType` : `GEOSHARDED` but not `selfManagedSharding` : `true`.")
