"""Generated model for NamespacesRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class NamespacesRequest(BaseModel):
    """Generated model for NamespacesRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    namespaces: list[str] | None = Field(default=None, description="List of namespace strings (combination of database and collection) on the specified host or cluster.")
