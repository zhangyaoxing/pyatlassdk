"""Generated model for AzureHardwareSpec20240805. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AzureHardwareSpec20240805(BaseModel):
    """Generated model for AzureHardwareSpec20240805."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    disk_iops: int | None = Field(default=None, alias="diskIOPS", description="Target throughput desired for storage attached to your Azure-provisioned cluster. Change this parameter if you:\n\n- set `replicationSpecs[n].regionConfigs[m].providerName` : `Azure`.\n- set `replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize` : `M40` or greater not including `Mxx_NVME` tiers.\n\nThe maximum input/output operations per second (IOPS) depend on the selected `.instanceSize` and `.diskSizeGB`.\nThis parameter defaults to the cluster tier's standard IOPS value.\nChanging this value impacts cluster cost.")
    disk_size_gb: float | None = Field(default=None, alias="diskSizeGB", description="Storage capacity of instance data volumes expressed in gigabytes. Increase this number to add capacity.\n\n This value must be equal for all shards and node types.\n\n This value is not configurable on M0/M2/M5 clusters.\n\n MongoDB Cloud requires this parameter if you set `replicationSpecs`.\n\n If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. \n\n Storage charge calculations depend on whether you choose the default value or a custom value.\n\n The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.")
    instance_size: Annotated[Literal["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M90", "M200", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "M60_NVME", "M80_NVME", "M200_NVME", "M300_NVME", "M400_NVME", "M600_NVME"], BeforeValidator(upper_case)] | None = Field(default=None, alias="instanceSize", description="Hardware specification for the instance sizes in this region in this shard. Each instance size has a default storage and memory capacity. Electable nodes and read-only nodes (known as \"base nodes\") within a single shard must use the same instance size. Analytics nodes can scale independently from base nodes within a shard. Both base nodes and analytics nodes can scale independently from their equivalents in other shards.")
    node_count: int | None = Field(default=None, alias="nodeCount", description="Number of nodes of the given type for MongoDB Cloud to deploy to the region.")
