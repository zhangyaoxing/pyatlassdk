"""Generated model for DBUserTLSX509Settings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DBUserTLSX509Settings(BaseModel):
    """Settings to configure TLS Certificates for database users."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cas: str | None = Field(default=None, description="Concatenated list of customer certificate authority (CA) certificates needed to authenticate database users. MongoDB Cloud expects this as a PEM-formatted certificate.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
