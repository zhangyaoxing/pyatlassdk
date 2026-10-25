"""Generated model for PinFCVView. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PinFCVView(BaseModel):
    """Generated model for PinFCVView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    expiration_date: datetime | None = Field(default=None, alias="expirationDate", description="Expiration date of the fixed FCV. If not specified, the expiration date will default to 4 weeks from the date FCV was originally pinned. Note that this field cannot exceed 4 weeks from the pinned date. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
