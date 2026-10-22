"""Generated model for AddOrRemoveUserFromTeam. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class AddOrRemoveUserFromTeam(BaseModel):
    """Generated model for AddOrRemoveUserFromTeam."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user.")
