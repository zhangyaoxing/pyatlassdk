"""Generated model for FreeComputeAutoScalingRules. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FreeComputeAutoScalingRules(BaseModel):
    """Collection of settings that configures how a cluster might scale its cluster tier and whether the cluster can scale down."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    max_instance_size: Annotated[Literal["M0", "M2", "M5"], BeforeValidator(upper_case)] | None = Field(default=None, alias="maxInstanceSize", description="Maximum instance size to which your cluster can automatically scale.")
    min_instance_size: Annotated[Literal["M0", "M2", "M5"], BeforeValidator(upper_case)] | None = Field(default=None, alias="minInstanceSize", description="Minimum instance size to which your cluster can automatically scale.")
