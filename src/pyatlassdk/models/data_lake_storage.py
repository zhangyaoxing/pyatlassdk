"""Generated model for DataLakeStorage. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.data_lake_database_instance import DataLakeDatabaseInstance
from pyatlassdk.models.data_lake_store_settings import DataLakeStoreSettings

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeStorage(BaseModel):
    """Configuration information for each data store and its mapping to MongoDB Cloud databases."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    databases: list[DataLakeDatabaseInstance] | None = Field(default=None, description="Array that contains the queryable databases and collections for this data lake.")
    stores: list[DataLakeStoreSettings] | None = Field(default=None, description="Array that contains the data stores for the data lake.")
