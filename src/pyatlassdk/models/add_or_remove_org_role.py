"""Generated model for AddOrRemoveOrgRole. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AddOrRemoveOrgRole(BaseModel):
    """Generated model for AddOrRemoveOrgRole."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    org_role: Literal["ORG_OWNER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY", "ORG_MEMBER"] = Field(alias="orgRole", description="Organization-level role.")
