"""Generated model for CollStatsRankedNamespacesView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CollStatsRankedNamespacesView(BaseModel):
    """Generated model for CollStatsRankedNamespacesView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the request project.")
    identifier_id: str | None = Field(default=None, alias="identifierId", description="Unique 24-hexadecimal digit string that identifies the request process.")
    ranked_namespaces: list[str] = Field(alias="rankedNamespaces", description="Ordered list of the hottest namespaces, highest value first.")
