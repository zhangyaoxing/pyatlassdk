"""Generated model for AtlasClusterOutageSimulationOutageFilter. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasClusterOutageSimulationOutageFilter(BaseModel):
    """Generated model for AtlasClusterOutageSimulationOutageFilter."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "GCP", "AZURE"], BeforeValidator(upper_case)] | None = Field(default=None, alias="cloudProvider", description="The cloud provider of the region that undergoes the outage simulation.")
    region_name: str | None = Field(default=None, alias="regionName", description="The name of the region to undergo an outage simulation.")
    type: Annotated[Literal["REGION"], BeforeValidator(upper_case)] | None = Field(default=None, description="The type of cluster outage to simulate. `REGION` simulates a cluster outage for a region.")
