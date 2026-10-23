"""Generated model for GroupRole. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GroupRole(BaseModel):
    """Generated model for GroupRole."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project to which this role belongs.")
    group_role: str | None = Field(default=None, alias="groupRole", description="Human-readable label that identifies the collection of privileges that MongoDB Cloud grants a specific API key, MongoDB Cloud user, or MongoDB Cloud team. These roles include project-level roles.")
