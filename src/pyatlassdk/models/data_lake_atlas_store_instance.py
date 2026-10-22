"""Generated model for DataLakeAtlasStoreInstance. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.data_lake_atlas_store_read_concern import DataLakeAtlasStoreReadConcern
from pyatlassdk.models.data_lake_atlas_store_read_preference import DataLakeAtlasStoreReadPreference

from pydantic import BaseModel, ConfigDict, Field

class DataLakeAtlasStoreInstance(BaseModel):
    """Group of settings that define where the data is stored."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Human-readable label that identifies the data store. The **databases.[n].collections.[n].dataSources.[n].storeName** field references this values as part of the mapping configuration. To use MongoDB Cloud as a data store, the data lake requires a serverless instance or an `M10` or higher cluster.")
    provider: str
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label of the MongoDB Cloud cluster on which the store is based.")
    project_id: str | None = Field(default=None, alias="projectId", description="Unique 24-hexadecimal digit string that identifies the project.")
    read_concern: DataLakeAtlasStoreReadConcern | None = Field(default=None, alias="readConcern")
    read_preference: DataLakeAtlasStoreReadPreference | None = Field(default=None, alias="readPreference")
