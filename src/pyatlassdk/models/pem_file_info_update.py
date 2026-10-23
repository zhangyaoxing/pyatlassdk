"""Generated model for PemFileInfoUpdate. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.x509_certificate_update import X509CertificateUpdate

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PemFileInfoUpdate(BaseModel):
    """PEM file information for the identity provider's current certificates."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    certificates: list[X509CertificateUpdate] | None = Field(default=None, description="List of certificates in the file.")
    file_name: str | None = Field(default=None, alias="fileName", description="Human-readable label given to the file.")
