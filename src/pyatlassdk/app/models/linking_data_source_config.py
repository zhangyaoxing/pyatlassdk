"""Generated model for LinkingDataSourceConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LinkingDataSourceConfig(BaseModel):
    """Generated model for LinkingDataSourceConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_name: str = Field(alias="clusterName", description="The cluster name of the data source within. The name may be at\nmost 64 characters long and must only contain ASCII letters, numbers,\nunderscores, and hyphens.")
