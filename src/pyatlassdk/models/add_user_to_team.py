"""Generated model for AddUserToTeam. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class AddUserToTeam(BaseModel):
    """Generated model for AddUserToTeam."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user.")
