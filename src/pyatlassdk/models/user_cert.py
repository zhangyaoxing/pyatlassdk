"""Generated model for UserCert. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class UserCert(BaseModel):
    """Generated model for UserCert."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: int | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal character string that identifies this certificate.")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date and time when MongoDB Cloud created this certificate. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    months_until_expiration: int | None = Field(default=None, alias="monthsUntilExpiration", description="Number of months that the certificate remains valid until it expires.")
    not_after: datetime | None = Field(default=None, alias="notAfter", description="Date and time when this certificate expires. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    subject: str | None = Field(default=None, description="Subject Alternative Name associated with this certificate. This parameter expresses its value as a distinguished name as defined in RFC 2253.")
