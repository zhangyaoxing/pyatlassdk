"""Generated model for RegionSpec. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RegionSpec(BaseModel):
    """Physical location where MongoDB Cloud provisions cluster nodes."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    analytics_nodes: int | None = Field(default=None, alias="analyticsNodes", description="Number of analytics nodes in the region. Analytics nodes handle analytic data such as reporting queries from MongoDB Connector for Business Intelligence on MongoDB Cloud. Analytics nodes are read-only, and can never become the primary. Use `replicationSpecs[n].{region}.analyticsNodes` instead.")
    electable_nodes: Literal[0, 3, 5, 7] | None = Field(default=None, alias="electableNodes", description="Number of electable nodes to deploy in the specified region. Electable nodes can become the primary and can facilitate local reads. Use `replicationSpecs[n].{region}.electableNodes` instead.")
    priority: int | None = Field(default=None, description="Number that indicates the election priority of the region. To identify the Preferred Region of the cluster, set this parameter to `7`. The primary node runs in the **Preferred Region**. To identify a read-only region, set this parameter to `0`.")
    read_only_nodes: int | None = Field(default=None, alias="readOnlyNodes", description="Number of read-only nodes in the region. Read-only nodes can never become the primary member, but can facilitate local reads. Use `replicationSpecs[n].{region}.readOnlyNodes` instead.")
