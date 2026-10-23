"""Generated model for TenantWithSampleConnections. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class TenantWithSampleConnections(BaseModel):
    """Generated model for TenantWithSampleConnections."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    pass
