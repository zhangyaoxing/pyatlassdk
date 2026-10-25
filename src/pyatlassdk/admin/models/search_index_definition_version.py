"""Generated model for SearchIndexDefinitionVersion. Do not edit manually."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchIndexDefinitionVersion(BaseModel):
    """Object which includes the version number of the index definition and the time that the index definition was created."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="The time at which this index definition was created. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    version: int | None = Field(default=None, description="The version number associated with this index definition when it was created.")
