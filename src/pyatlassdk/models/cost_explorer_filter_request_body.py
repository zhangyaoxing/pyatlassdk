"""Generated model for CostExplorerFilterRequestBody. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import date

from pydantic import BaseModel, ConfigDict, Field

class CostExplorerFilterRequestBody(BaseModel):
    """Request body for a cost explorer query."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    clusters: list[str] | None = Field(default=None, description="The list of clusters to be included in the Cost Explorer Query.")
    end_date: date = Field(alias="endDate", description="The exclusive ending date for the Cost Explorer query. The date must be the start of a month.")
    group_by: Literal["organizations", "projects", "clusters", "services"] | None = Field(default=None, alias="groupBy", description="The dimension to group the returned usage results by. At least one filter value needs to be provided for a dimension to be used.")
    include_partial_matches: bool | None = Field(default=None, alias="includePartialMatches", description="Flag to control whether usage that matches the filter criteria, but does not have values for all filter criteria is included in response. Default is false, which excludes the partially matching data.")
    organizations: list[str] | None = Field(default=None, description="The list of organizations to be included in the Cost Explorer Query.")
    projects: list[str] | None = Field(default=None, description="The list of projects to be included in the Cost Explorer Query.")
    services: list[Literal["Atlas", "Clusters", "Storage", "Serverless Instances", "Backup", "Data Transfer", "BI Connector", "Premium Features", "Atlas Data Federation", "Atlas Stream Processing", "App Services", "Charts", "Cloud Manager", "Cloud Manager Standard/Premium", "Legacy Backup", "AI Model APIs", "Automated Embedding", "Native Reranking", "Agent Engine", "Flex Consulting", "Support", "Credits"]] | None = Field(default=None, description="The list of SKU services to be included in the Cost Explorer Query.")
    start_date: date = Field(alias="startDate", description="The inclusive starting date for the Cost Explorer query. The date must be the start of a month.")
