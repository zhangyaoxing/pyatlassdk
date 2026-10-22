"""Generated model for ServiceAccountSecret. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class ServiceAccountSecret(BaseModel):
    """Generated model for ServiceAccountSecret."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_at: datetime = Field(alias="createdAt", description="The date that the secret was created on. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    expires_at: datetime = Field(alias="expiresAt", description="The date for the expiration of the secret. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the secret.")
    last_used_at: datetime | None = Field(default=None, alias="lastUsedAt", description="The last time the secret was used. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    masked_secret_value: str | None = Field(default=None, alias="maskedSecretValue", description="The masked Service Account secret.")
    secret: str | None = Field(default=None, description="The secret for the Service Account. It will be returned only the first time after creation.")
