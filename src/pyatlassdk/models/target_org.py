"""Generated model for TargetOrg. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class TargetOrg(BaseModel):
    """Generated model for TargetOrg."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    link_token: str = Field(alias="linkToken", description="Link token that contains all the information required to complete the link.")
