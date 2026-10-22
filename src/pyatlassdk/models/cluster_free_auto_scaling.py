"""Generated model for ClusterFreeAutoScaling. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.free_compute_auto_scaling_rules import FreeComputeAutoScalingRules

from pydantic import BaseModel, ConfigDict, Field

class ClusterFreeAutoScaling(BaseModel):
    """Range of instance sizes to which your cluster can scale."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    compute: FreeComputeAutoScalingRules | None = None
