"""Generated model for Namespaces. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.namespace_obj import NamespaceObj

from pydantic import BaseModel, ConfigDict, Field

class Namespaces(BaseModel):
    """Generated model for Namespaces."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    namespaces: list[NamespaceObj] | None = Field(default=None, description="List that contains each combination of database, collection, and type on the specified host.")
