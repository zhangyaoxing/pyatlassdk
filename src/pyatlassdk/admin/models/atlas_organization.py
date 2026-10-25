"""Generated model for AtlasOrganization. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasOrganization(BaseModel):
    """Details that describe the organization."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the organization.")
    is_deleted: bool | None = Field(default=None, alias="isDeleted", description="Flag that indicates whether this organization has been deleted.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str = Field(description="Human-readable label that identifies the organization.")
    skip_default_alerts_settings: bool | None = Field(default=None, alias="skipDefaultAlertsSettings", description="Disables automatic alert creation. When set to true, no organization level alerts will be created automatically.")
