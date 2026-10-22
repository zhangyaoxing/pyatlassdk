"""Generated model for GroupUpdate. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.resource_tag import ResourceTag

from pydantic import BaseModel, ConfigDict, Field

class GroupUpdate(BaseModel):
    """Request view to update the group."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Human-readable label that identifies the project included in the MongoDB Cloud organization.")
    tags: list[ResourceTag] | None = Field(default=None, description="List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the project.")
    with_default_alerts_settings: bool | None = Field(default=None, alias="withDefaultAlertsSettings", description="Flag that indicates whether the project can automatically create default alerts.")
