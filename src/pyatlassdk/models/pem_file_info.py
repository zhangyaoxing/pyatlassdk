"""Generated model for PemFileInfo. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.x509_certificate import X509Certificate

from pydantic import BaseModel, ConfigDict, Field

class PemFileInfo(BaseModel):
    """PEM file information for the identity provider's current certificates."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    certificates: list[X509Certificate] | None = Field(default=None, description="List of certificates in the file.")
    file_name: str | None = Field(default=None, alias="fileName", description="Human-readable label given to the file.")
