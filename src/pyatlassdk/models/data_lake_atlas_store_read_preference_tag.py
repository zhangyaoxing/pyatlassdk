"""Generated model for DataLakeAtlasStoreReadPreferenceTag. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class DataLakeAtlasStoreReadPreferenceTag(BaseModel):
    """Generated model for DataLakeAtlasStoreReadPreferenceTag."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Human-readable label of the tag.")
    value: str | None = Field(default=None, description="Value of the tag.")
