"""Generated model for ClusterOutageSimulation. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.atlas_cluster_outage_simulation_outage_filter import AtlasClusterOutageSimulationOutageFilter

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterOutageSimulation(BaseModel):
    """Generated model for ClusterOutageSimulation."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster that undergoes outage simulation.")
    expiration_date: datetime | None = Field(default=None, alias="expirationDate", description="Date and time when MongoDB Cloud expires the outage simulation. This parameter expresses its value in the ISO 8601 timestamp format in UTC. If not provided, defaults to 3 days from the start date.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project that contains the cluster to undergo outage simulation.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal character string that identifies the outage simulation.")
    outage_filters: list[AtlasClusterOutageSimulationOutageFilter] | None = Field(default=None, alias="outageFilters", description="List of settings that specify the type of cluster outage simulation.")
    start_request_date: datetime | None = Field(default=None, alias="startRequestDate", description="Date and time when MongoDB Cloud started the regional outage simulation. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    state: Annotated[Literal["START_REQUESTED", "STARTING", "SIMULATING", "RECOVERY_REQUESTED", "RECOVERING", "COMPLETE"], BeforeValidator(upper_case)] | None = Field(default=None, description="Phase of the outage simulation.\n\n| State       | Indication |\n|-------------|------------|\n| `START_REQUESTED`    | User has requested cluster outage simulation.|\n| `STARTING`           | MongoDB Cloud is starting cluster outage simulation.|\n| `SIMULATING`         | MongoDB Cloud is simulating cluster outage.|\n| `RECOVERY_REQUESTED` | User has requested recovery from the simulated outage.|\n| `RECOVERING`         | MongoDB Cloud is recovering the cluster from the simulated outage.|\n| `COMPLETE`           | MongoDB Cloud has completed the cluster outage simulation.|")
