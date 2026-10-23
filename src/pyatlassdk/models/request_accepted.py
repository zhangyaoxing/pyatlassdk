"""Generated model for RequestAccepted. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RequestAccepted(BaseModel):
    """Accepted."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    pass
