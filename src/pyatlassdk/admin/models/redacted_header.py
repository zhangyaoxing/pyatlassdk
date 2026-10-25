"""Generated model for RedactedHeader. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RedactedHeader(BaseModel):
    """HTTP header with a redacted value."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="Header name.")
    value: str = Field(description="Redacted header value.")
