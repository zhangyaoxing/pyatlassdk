"""Generated model for MesurementsDatabase. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MesurementsDatabase(BaseModel):
    """Generated model for MesurementsDatabase."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    database_name: str | None = Field(default=None, alias="databaseName", description="Human-readable label that identifies the database that the specified MongoDB process serves.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
