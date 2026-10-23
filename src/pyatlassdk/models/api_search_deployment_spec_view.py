"""Generated model for ApiSearchDeploymentSpecView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiSearchDeploymentSpecView(BaseModel):
    """Hardware specification for the Search Nodes that back a search deployment."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    instance_size: Annotated[Literal["S10_HIGHCPU", "S20_HIGHCPU_NVME", "S30_HIGHCPU_NVME", "S40_HIGHCPU_NVME", "S50_HIGHCPU_NVME", "S60_HIGHCPU_NVME", "S70_HIGHCPU_NVME", "S80_HIGHCPU_NVME", "S30_LOWCPU_NVME", "S40_LOWCPU_NVME", "S50_LOWCPU_NVME", "S60_LOWCPU_NVME", "S70_LOWCPU_NVME", "S80_LOWCPU_NVME", "S90_LOWCPU_NVME", "S100_LOWCPU_NVME", "S110_LOWCPU_NVME", "S120_LOWCPU_NVME", "S130_LOWCPU_NVME", "S135_LOWCPU_NVME", "S140_LOWCPU_NVME", "S40_STORAGE_NVME", "S50_STORAGE_NVME", "S60_STORAGE_NVME", "S80_STORAGE_NVME", "S90_STORAGE_NVME"], BeforeValidator(upper_case)] = Field(alias="instanceSize", description="Hardware specification for the Search Node instance sizes.")
    node_count: int = Field(alias="nodeCount", description="Number of Search Nodes in the cluster.")
