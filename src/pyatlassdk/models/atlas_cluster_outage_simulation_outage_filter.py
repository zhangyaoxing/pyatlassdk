"""Generated model for AtlasClusterOutageSimulationOutageFilter. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AtlasClusterOutageSimulationOutageFilter(BaseModel):
    """Generated model for AtlasClusterOutageSimulationOutageFilter."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS", "GCP", "AZURE"] | None = Field(default=None, alias="cloudProvider", description="The cloud provider of the region that undergoes the outage simulation.")
    region_name: str | None = Field(default=None, alias="regionName", description="The name of the region to undergo an outage simulation.")
    type: Literal["REGION"] | None = Field(default=None, description="The type of cluster outage to simulate. `REGION` simulates a cluster outage for a region.")
