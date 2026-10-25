"""Generated model for CustomSessionTimeouts. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomSessionTimeouts(BaseModel):
    """Defines the session timeout settings for managing user sessions at the organization level. When set to null, the field's value is unset, and the default timeout settings are applied."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    absolute_session_timeout_in_seconds: int | None = Field(default=None, alias="absoluteSessionTimeoutInSeconds", description="Specifies the absolute session timeout duration in seconds. When set to null, the field's value is unset, and the default value of 43,200 seconds (12 hours) is applied. Accepted values range between a minimum of 3,600 seconds (1 hour) and a maximum of 43,200 seconds (12 hours).")
    idle_session_timeout_in_seconds: int | None = Field(default=None, alias="idleSessionTimeoutInSeconds", description="Specifies the idle session timeout duration in seconds. When set to null, the field's value is unset, and the default behavior depends on the context: no timeout for Atlas Commercial, and 600 seconds (10 minutes) for Atlas for Government. Accepted values start at a minimum of 300 seconds (5 minutes). For Atlas Commercial, the maximum value cannot exceed the configured absolute session timeout. For Atlas for Government, the maximum value is capped at 600 seconds (10 minutes).")
