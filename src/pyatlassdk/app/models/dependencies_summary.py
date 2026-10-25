"""Generated model for DependenciesSummary. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.dependency import Dependency

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DependenciesSummary(BaseModel):
    """Generated model for DependenciesSummary."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The dependency collection's unique internal ID.")
    location: str | None = Field(default=None, description="The application's deployment region.")
    user_id: str | None = Field(default=None, description="The unique `_id` value of the MongoDB Cloud user that uploaded the\ndependency collection.")
    last_modified: int | None = Field(default=None, description="The time at which the dependencies were uploaded in [Unix\ntime](https://en.wikipedia.org/wiki/Unix_time) (number of seconds since\nJanuary 1, 1970 at 00:00 UTC).")
    dependencies_list: list[Dependency] | None = Field(default=None, description="An array of documents that each describe a dependency uploaded to the\napplication.")
