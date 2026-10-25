"""Generated model for AddOrRemoveOrgRole. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AddOrRemoveOrgRole(BaseModel):
    """Generated model for AddOrRemoveOrgRole."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    org_role: Annotated[Literal["ORG_OWNER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY", "ORG_MEMBER"], BeforeValidator(upper_case)] = Field(alias="orgRole", description="Organization-level role.")
