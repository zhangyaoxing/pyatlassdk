"""Generated model for FailedLinkingDataSourceResponse. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FailedLinkingDataSourceResponse(BaseModel):
    """Generated model for FailedLinkingDataSourceResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    failed_cluster_names: list[str] | None = Field(default=None, alias="failedClusterNames", description="The names of any data sources that failed to link. This uses the `name` property\nyou assigned to the data source. ")
