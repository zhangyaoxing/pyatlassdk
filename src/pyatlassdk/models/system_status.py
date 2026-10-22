"""Generated model for SystemStatus. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.api_key import ApiKey
from pyatlassdk.models.authenticated_user import AuthenticatedUser
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class SystemStatus(BaseModel):
    """Generated model for SystemStatus."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    api_key: ApiKey | None = Field(default=None, alias="apiKey")
    app_name: Literal["MongoDB Atlas"] = Field(alias="appName", description="Human-readable label that identifies the service from which you requested this response.")
    build: str = Field(description="Unique 40-hexadecimal digit hash that identifies the latest git commit merged for this application.")
    ip_address: str = Field(alias="ipAddress", description="IPv4 or IPv6 address from which you requested this response. Use this value to confirm which address IP access lists evaluate for your requests.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    throttling: bool = Field(description="Flag that indicates whether someone enabled throttling on this service.")
    user: AuthenticatedUser | None = None
