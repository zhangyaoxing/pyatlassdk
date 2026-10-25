"""Generated model for DataLakeDatabaseInstance. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.data_lake_api_base import DataLakeApiBase
from pyatlassdk.admin.models.data_lake_database_collection import DataLakeDatabaseCollection

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeDatabaseInstance(BaseModel):
    """Database associated with this data lake. Databases contain collections and views."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collections: list[DataLakeDatabaseCollection] | None = Field(default=None, description="Array of collections and data sources that map to a ``stores`` data store.")
    max_wildcard_collections: int | None = Field(default=None, alias="maxWildcardCollections", description="Maximum number of wildcard collections in the database. This only applies to S3 data sources.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the database to which the data lake maps data.")
    views: list[DataLakeApiBase] | None = Field(default=None, description="Array of aggregation pipelines that apply to the collection. This only applies to S3 data sources.")
