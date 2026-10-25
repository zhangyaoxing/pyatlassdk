"""Generated model for LogsAuthAuthEvent. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsAuthAuthEvent(BaseModel):
    """Generated model for LogsAuthAuthEvent."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: str | None = Field(default=None, description="The requested authentication operation.")
    provider: Literal["anon-user", "local-userpass", "api-key", "oauth2-apple", "oauth2-google", "oauth2-facebook", "custom-token", "custom-function"] | None = None
