"""Generated model for ClusterComputeAutoScaling. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class ClusterComputeAutoScaling(BaseModel):
    """Collection of settings that configures how a cluster might scale its cluster tier and whether the cluster can scale down. Cluster tier auto-scaling is unavailable for clusters using Low CPU or NVME storage classes."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether instance size reactive auto-scaling is enabled.\n\n- Set to `true` to enable instance size reactive auto-scaling. If enabled, you must specify a value for `providerSettings.autoScaling.compute.maxInstanceSize`.\n- Set to `false` to disable instance size reactive auto-scaling.")
    scale_down_enabled: bool | None = Field(default=None, alias="scaleDownEnabled", description="Flag that indicates whether the cluster tier can scale down via reactive auto-scaling. This is required if `autoScaling.compute.enabled` is `true`. If you enable this option, specify a value for `providerSettings.autoScaling.compute.minInstanceSize`.")
