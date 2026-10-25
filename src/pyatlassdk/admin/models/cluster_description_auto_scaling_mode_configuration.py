"""Generated model for ClusterDescriptionAutoScalingModeConfiguration. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterDescriptionAutoScalingModeConfiguration(BaseModel):
    """Contains the internal configuration of AutoScaling on sharded clusters."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_scaling_mode: Annotated[Literal["INDEPENDENT_SHARD_SCALING", "CLUSTER_WIDE_SCALING"], BeforeValidator(upper_case)] | None = Field(default=None, alias="autoScalingMode", description="Describes whether cluster nodes scale together across all shards or independently.")
