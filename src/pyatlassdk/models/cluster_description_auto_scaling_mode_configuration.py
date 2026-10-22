"""Generated model for ClusterDescriptionAutoScalingModeConfiguration. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class ClusterDescriptionAutoScalingModeConfiguration(BaseModel):
    """Contains the internal configuration of AutoScaling on sharded clusters."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_scaling_mode: Literal["INDEPENDENT_SHARD_SCALING", "CLUSTER_WIDE_SCALING"] | None = Field(default=None, alias="autoScalingMode", description="Describes whether cluster nodes scale together across all shards or independently.")
