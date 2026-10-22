"""Generated model for X509Certificate. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class X509Certificate(BaseModel):
    """Generated model for X509Certificate."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    not_after: datetime | None = Field(default=None, alias="notAfter", description="Latest date that the certificate is valid. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    not_before: datetime | None = Field(default=None, alias="notBefore", description="Earliest date that the certificate is valid. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
