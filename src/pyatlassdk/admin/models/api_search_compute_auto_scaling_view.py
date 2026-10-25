"""Generated model for ApiSearchComputeAutoScalingView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiSearchComputeAutoScalingView(BaseModel):
    """Settings that control Search Node tier scaling based on load."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether Atlas raises the Search Node tier when the nodes are under sustained load. If set to `true`, you must also set `maxInstanceTier`.")
    max_instance_tier: Annotated[Literal["S10", "S20", "S30", "S40", "S50", "S60", "S70", "S80", "S90", "S100", "S110", "S120", "S130", "S135", "S140"], BeforeValidator(upper_case)] | None = Field(default=None, alias="maxInstanceTier", description="Highest Search Node tier that Atlas can scale up to. Required when `enabled` is `true`.")
    min_instance_tier: Annotated[Literal["S10", "S20", "S30", "S40", "S50", "S60", "S70", "S80", "S90", "S100", "S110", "S120", "S130", "S135", "S140"], BeforeValidator(upper_case)] | None = Field(default=None, alias="minInstanceTier", description="Lowest Search Node tier that Atlas can scale down to. Required when `scaleDownEnabled` is `true`. Scaling down is not supported yet, so setting this returns an error.")
    scale_down_enabled: bool | None = Field(default=None, alias="scaleDownEnabled", description="Flag that indicates whether Atlas lowers the Search Node tier when load drops. Takes effect only when `enabled` is `true`. If set to `true`, you must also set `minInstanceTier`. Scaling down is not supported yet, so setting this to `true` returns an error.")
