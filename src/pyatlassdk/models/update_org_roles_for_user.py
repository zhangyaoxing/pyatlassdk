"""Generated model for UpdateOrgRolesForUser. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class UpdateOrgRolesForUser(BaseModel):
    """Generated model for UpdateOrgRolesForUser."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_roles: list[Literal["ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY"]] | None = Field(default=None, alias="orgRoles", description="One or more organization level roles to assign to the MongoDB Cloud user.")
