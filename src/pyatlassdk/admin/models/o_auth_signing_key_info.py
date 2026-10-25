"""Generated model for OAuthSigningKeyInfo. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OAuthSigningKeyInfo(BaseModel):
    """Read-only metadata for the Atlas-managed signing key used by `PRIVATE_KEY_JWT`. Present only for that method. Register the `jwksUri` with your identity provider. Atlas rotates the underlying key without changing this URL."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    algorithm: str | None = Field(default=None, description="Signing algorithm of the Atlas-managed key.")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="When the currently active signing key was created. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    jwks_uri: str | None = Field(default=None, alias="jwksUri", description="Public JWKS URL serving this integration's signing keys. Fixed for the lifetime of the integration.")
    kid: str | None = Field(default=None, description="Key ID stamped on client assertions, the `SHA-1` thumbprint of the key certificate in uppercase hexadecimal. Changes when Atlas rotates the key.")
