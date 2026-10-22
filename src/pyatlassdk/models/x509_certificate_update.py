"""Generated model for X509CertificateUpdate. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class X509CertificateUpdate(BaseModel):
    """Generated model for X509CertificateUpdate."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    content: str | None = Field(default=None, description="Certificate content.")
    not_after: datetime | None = Field(default=None, alias="notAfter", description="Latest date that the certificate is valid. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    not_before: datetime | None = Field(default=None, alias="notBefore", description="Earliest date that the certificate is valid. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
