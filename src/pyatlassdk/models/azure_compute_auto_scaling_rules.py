"""Generated model for AzureComputeAutoScalingRules. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AzureComputeAutoScalingRules(BaseModel):
    """Collection of settings that configures how a cluster might scale its cluster tier and whether the cluster can scale down. Cluster tier auto-scaling is unavailable for clusters using Low CPU or NVME storage classes."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    max_instance_size: Literal["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M90", "M200", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "M60_NVME", "M80_NVME", "M200_NVME", "M300_NVME", "M400_NVME", "M600_NVME"] | None = Field(default=None, alias="maxInstanceSize", description="Maximum instance size to which your cluster can automatically scale.")
    min_instance_size: Literal["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M90", "M200", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "M60_NVME", "M80_NVME", "M200_NVME", "M300_NVME", "M400_NVME", "M600_NVME"] | None = Field(default=None, alias="minInstanceSize", description="Minimum instance size to which your cluster can automatically scale.")
