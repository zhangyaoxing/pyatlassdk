"""Generated model for AddOrRemoveGroupRole. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class AddOrRemoveGroupRole(BaseModel):
    """Generated model for AddOrRemoveGroupRole."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_role: str = Field(alias="groupRole", description="Project-level role to assign to or remove from the MongoDB Cloud user.")
