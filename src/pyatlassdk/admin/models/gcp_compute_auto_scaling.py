"""Generated model for GCPComputeAutoScaling. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GCPComputeAutoScaling(BaseModel):
    """Collection of settings that configures how a cluster might scale its cluster tier and whether the cluster can scale down. Cluster tier auto-scaling is unavailable for clusters using Low CPU or NVME storage classes."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    max_instance_size: Annotated[Literal["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M140", "M200", "M250", "M300", "M400", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "R600", "M30_GEN_2", "M40_GEN_2", "M50_GEN_2", "M60_GEN_2", "M80_GEN_2", "M140_GEN_2", "M200_GEN_2", "M300_GEN_2", "M700_GEN_2", "R40_GEN_2", "R50_GEN_2", "R60_GEN_2", "R80_GEN_2", "R200_GEN_2", "R300_GEN_2", "R400_GEN_2"], BeforeValidator(upper_case)] | None = Field(default=None, alias="maxInstanceSize", description="Maximum instance size to which your cluster can automatically scale.")
    min_instance_size: Annotated[Literal["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M140", "M200", "M250", "M300", "M400", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "R600", "M30_GEN_2", "M40_GEN_2", "M50_GEN_2", "M60_GEN_2", "M80_GEN_2", "M140_GEN_2", "M200_GEN_2", "M300_GEN_2", "M700_GEN_2", "R40_GEN_2", "R50_GEN_2", "R60_GEN_2", "R80_GEN_2", "R200_GEN_2", "R300_GEN_2", "R400_GEN_2"], BeforeValidator(upper_case)] | None = Field(default=None, alias="minInstanceSize", description="Minimum instance size to which your cluster can automatically scale.")
