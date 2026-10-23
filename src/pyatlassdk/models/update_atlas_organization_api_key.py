"""Generated model for UpdateAtlasOrganizationApiKey. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class UpdateAtlasOrganizationApiKey(BaseModel):
    """Generated model for UpdateAtlasOrganizationApiKey."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    desc: str | None = Field(default=None, description="Purpose or explanation provided when someone creates this organization API key.")
    roles: list[Annotated[Literal["ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY"], BeforeValidator(upper_case)]] | None = Field(default=None, description="List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this organization.")
