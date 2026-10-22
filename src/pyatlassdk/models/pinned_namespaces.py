"""Generated model for PinnedNamespaces. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class PinnedNamespaces(BaseModel):
    """Pinned namespaces view for cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the request cluster.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the request project.")
    pinned_namespaces: list[str] = Field(alias="pinnedNamespaces", description="List of all pinned namespaces.")
