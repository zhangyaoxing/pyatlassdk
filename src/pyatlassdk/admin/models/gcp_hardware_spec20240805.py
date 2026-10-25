"""Generated model for GCPHardwareSpec20240805. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GCPHardwareSpec20240805(BaseModel):
    """Generated model for GCPHardwareSpec20240805."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    disk_iops: int | None = Field(default=None, alias="diskIOPS", description="Target IOPS (Input/Output Operations Per Second) desired for storage attached to this hardware. Only configurable for Gen 2 instance sizes.\n\n Change this parameter if you:\n\n- set `\"replicationSpecs[n].regionConfigs[m].providerName\" : \"GCP\"`.\n- set `\"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\"` to a Gen 2 instance size (`\"M30_GEN_2\"` or greater).\n\nThe maximum input/output operations per second (IOPS) depend on the selected `.instanceSize` and `.diskSizeGB`.\nThis parameter defaults to the standard IOPS value for the selected `.diskSizeGB`.\nChanging this value impacts cluster cost.")
    disk_size_gb: float | None = Field(default=None, alias="diskSizeGB", description="Storage capacity of instance data volumes expressed in gigabytes. Increase this number to add capacity.\n\n This value must be equal for all shards and node types.\n\n This value is not configurable on M0/M2/M5 clusters.\n\n MongoDB Cloud requires this parameter if you set `replicationSpecs`.\n\n If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. \n\n Storage charge calculations depend on whether you choose the default value or a custom value.\n\n The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier.")
    disk_throughput: int | None = Field(default=None, alias="diskThroughput", description="Throughput (in MiB/s) provisioned for storage attached to this hardware. Only returned for Gen 2 instance sizes.")
    instance_size: Annotated[Literal["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M140", "M200", "M250", "M300", "M400", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "R600", "M30_GEN_2", "M40_GEN_2", "M50_GEN_2", "M60_GEN_2", "M80_GEN_2", "M140_GEN_2", "M200_GEN_2", "M300_GEN_2", "M700_GEN_2", "R40_GEN_2", "R50_GEN_2", "R60_GEN_2", "R80_GEN_2", "R200_GEN_2", "R300_GEN_2", "R400_GEN_2"], BeforeValidator(upper_case)] | None = Field(default=None, alias="instanceSize", description="Hardware specification for the instance sizes in this region in this shard. Each instance size has a default storage and memory capacity. Electable nodes and read-only nodes (known as \"base nodes\") within a single shard must use the same instance size. Analytics nodes can scale independently from base nodes within a shard. Both base nodes and analytics nodes can scale independently from their equivalents in other shards.")
    node_count: int | None = Field(default=None, alias="nodeCount", description="Number of nodes of the given type for MongoDB Cloud to deploy to the region.")
