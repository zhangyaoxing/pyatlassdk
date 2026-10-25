"""Generated model for GroupService. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.cluster_ip_addresses import ClusterIPAddresses

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GroupService(BaseModel):
    """List of IP addresses in a project categorized by services."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    clusters: list[ClusterIPAddresses] | None = Field(default=None, description="IP addresses of clusters.")
