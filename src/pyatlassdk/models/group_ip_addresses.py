"""Generated model for GroupIPAddresses. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.group_service import GroupService

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GroupIPAddresses(BaseModel):
    """List of IP addresses in a project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud project.")
    services: GroupService | None = None
