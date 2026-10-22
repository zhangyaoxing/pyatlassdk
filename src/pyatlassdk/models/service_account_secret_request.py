"""Generated model for ServiceAccountSecretRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class ServiceAccountSecretRequest(BaseModel):
    """Generated model for ServiceAccountSecretRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    secret_expires_after_hours: int = Field(alias="secretExpiresAfterHours", description="The expiration time of the new Service Account secret, provided in hours. The minimum and maximum allowed expiration times are subject to change and are controlled by the organization's settings.")
