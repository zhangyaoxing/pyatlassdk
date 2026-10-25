"""Generated model for ClusterAutoScalingSettings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.cluster_compute_auto_scaling import ClusterComputeAutoScaling

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterAutoScalingSettings(BaseModel):
    """Range of instance sizes to which your cluster can scale."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    compute: ClusterComputeAutoScaling | None = None
    disk_gb_enabled: bool | None = Field(default=None, alias="diskGBEnabled", description="Flag that indicates whether someone enabled disk auto-scaling for this cluster.")
