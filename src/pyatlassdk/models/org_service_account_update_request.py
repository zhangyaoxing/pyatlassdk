"""Generated model for OrgServiceAccountUpdateRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgServiceAccountUpdateRequest(BaseModel):
    """Generated model for OrgServiceAccountUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str | None = Field(default=None, description="Human readable description for the Service Account.")
    name: str | None = Field(default=None, description="Human-readable name for the Service Account. The name is modifiable and does not have to be unique.")
    roles: list[Annotated[Literal["ORG_MEMBER", "ORG_READ_ONLY", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_GROUP_CREATOR", "ORG_OWNER"], BeforeValidator(upper_case)]] | None = Field(default=None, description="A list of organization-level roles for the Service Account.")
