"""Generated model for CreateAtlasOrganizationApiKey. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class CreateAtlasOrganizationApiKey(BaseModel):
    """Organization Service Account that Atlas creates for this organization. If omitted, Atlas doesn't create an organization Service Account for this organization. If specified, this object requires all body parameters. Note that API Keys cannot be specified in the same request."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    desc: str = Field(description="Purpose or explanation provided when someone created this organization API key.")
    roles: list[Literal["ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_READ_ONLY"]] = Field(description="List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this organization.")
