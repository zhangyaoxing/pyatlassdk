"""Generated model for DataLakeAtlasStoreReadPreference. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.data_lake_atlas_store_read_preference_tag import DataLakeAtlasStoreReadPreferenceTag

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeAtlasStoreReadPreference(BaseModel):
    """MongoDB Cloud cluster read preference, which describes how to route read requests to the cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    max_staleness_seconds: int | None = Field(default=None, alias="maxStalenessSeconds", description="Maximum replication lag, or **staleness**, for reads from secondaries.")
    mode: Literal["primary", "primaryPreferred", "secondary", "secondaryPreferred", "nearest"] | None = Field(default=None, description="Read preference mode that specifies to which replica set member to route the read requests.")
    tag_sets: list[list[DataLakeAtlasStoreReadPreferenceTag]] | None = Field(default=None, alias="tagSets", description="List that contains tag sets or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags.")
