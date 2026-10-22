"""Generated model for TeamRole. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class TeamRole(BaseModel):
    """Generated model for TeamRole."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    role_names: list[str] = Field(alias="roleNames", description="One or more project-level roles to assign to the team.")
    team_id: str = Field(alias="teamId", description="Unique 24-hexadecimal character string that identifies the team.")
