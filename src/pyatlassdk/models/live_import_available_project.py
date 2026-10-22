"""Generated model for LiveImportAvailableProject. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.available_clusters_deployment import AvailableClustersDeployment

from pydantic import BaseModel, ConfigDict, Field

class LiveImportAvailableProject(BaseModel):
    """Generated model for LiveImportAvailableProject."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    deployments: list[AvailableClustersDeployment] = Field(description="List of clusters that can be migrated to MongoDB Cloud.")
    migration_hosts: list[str] = Field(alias="migrationHosts", description="Hostname of MongoDB Agent list that you configured to perform a migration.")
    name: str = Field(description="Human-readable label that identifies this project.")
    project_id: str = Field(alias="projectId", description="Unique 24-hexadecimal digit string that identifies the project to be migrated.")
