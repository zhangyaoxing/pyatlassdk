"""Generated model for LogsAuthAuthEvent. Do not edit manually."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsAuthAuthEvent(BaseModel):
    """Generated model for LogsAuthAuthEvent."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: str | None = Field(default=None, description="The requested authentication operation.")
    provider: dict[str, Any] | None = None
