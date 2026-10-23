"""Generated model for DataLakeDatabaseCollection. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.data_lake_database_data_source_settings import DataLakeDatabaseDataSourceSettings

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeDatabaseCollection(BaseModel):
    """A collection and data sources that map to a ``stores`` data store."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    data_sources: list[DataLakeDatabaseDataSourceSettings] | None = Field(default=None, alias="dataSources", description="Array that contains the data stores that map to a collection for this data lake.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the collection to which MongoDB Cloud maps the data in the data stores.")
