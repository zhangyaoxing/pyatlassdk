"""Generated model for OrgLogIntegrationHeader. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgLogIntegrationHeader(BaseModel):
    """HTTP header with name and value."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="Header name.")
    value: str = Field(description="Header value. Redacted in responses.")
