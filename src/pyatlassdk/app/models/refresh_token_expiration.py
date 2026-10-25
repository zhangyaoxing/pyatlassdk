"""Generated model for RefreshTokenExpiration. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class RefreshTokenExpiration(BaseModel):
    """Generated model for RefreshTokenExpiration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    expiration_time_seconds: float | None = Field(default=None, description="The time in seconds that a user session refresh token is\nvalid for after it is issued. After this time, the token is\nexpired and the user must re-authenticate.\n\nThe expiration time must be between 30 minutes and 5 years,\ninclusive. The default expiration time is 60 days.")
