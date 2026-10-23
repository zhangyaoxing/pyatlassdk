"""Generated model for DeleteCopiedBackups20240805. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DeleteCopiedBackups20240805(BaseModel):
    """Deleted copy setting whose backup copies need to also be deleted."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] | None = Field(default=None, alias="cloudProvider", description="Human-readable label that identifies the cloud provider for the deleted copy setting whose backup copies you want to delete.")
    region_name: str | None = Field(default=None, alias="regionName", description="Target region for the deleted copy setting whose backup copies you want to delete. Please supply the 'Atlas Region'.")
    zone_id: str | None = Field(default=None, alias="zoneId", description="Unique 24-hexadecimal digit string that identifies the zone in a cluster. For global clusters, there can be multiple zones to choose from. For sharded clusters and replica set clusters, there is only one zone in the cluster. To find the Zone Id, do a GET request to Return One Cluster from One Project and consult the `replicationSpecs` array.")
