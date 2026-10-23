"""Generated model for DatabaseRollingIndexRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.collation import Collation
from pyatlassdk.models.database_rolling_index_request_keys_item import DatabaseRollingIndexRequestKeysItem
from pyatlassdk.models.index_options import IndexOptions

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseRollingIndexRequest(BaseModel):
    """Generated model for DatabaseRollingIndexRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collation: Collation | None = None
    collection: str = Field(description="Human-readable label of the collection for which MongoDB Cloud creates an index.")
    db: str = Field(description="Human-readable label of the database that holds the collection on which MongoDB Cloud creates an index.")
    keys: list[DatabaseRollingIndexRequestKeysItem] = Field(description="List that contains one or more objects that describe the parameters that you want to index.")
    options: IndexOptions | None = None
