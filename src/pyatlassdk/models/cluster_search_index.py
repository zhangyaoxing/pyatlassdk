"""Generated model for ClusterSearchIndex. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.cluster_search_index_stored_source import ClusterSearchIndexStoredSource

from pydantic import BaseModel, ConfigDict, Field

class ClusterSearchIndex(BaseModel):
    """Generated model for ClusterSearchIndex."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection_name: str = Field(alias="collectionName", description="Human-readable label that identifies the collection that contains one or more Atlas Search indexes.")
    database: str = Field(description="Human-readable label that identifies the database that contains the collection with one or more Atlas Search indexes.")
    index_id: str | None = Field(default=None, alias="indexID", description="Unique 24-hexadecimal digit string that identifies this Atlas Search index.")
    name: str = Field(description="Human-readable label that identifies this index. Within each namespace, names of all indexes in the namespace must be unique.")
    num_partitions: int | None = Field(default=None, alias="numPartitions", description="Number of index partitions. Allowed values are [1, 2, 4].")
    status: Literal["IN_PROGRESS", "STEADY", "FAILED", "MIGRATING", "STALE", "PAUSED"] | None = Field(default=None, description="Condition of the search index when you made this request.\n\n- `IN_PROGRESS`: Atlas is building or re-building the index after an edit.\n- `STEADY`: You can use this search index.\n- `FAILED`: Atlas could not build the index.\n- `MIGRATING`: Atlas is upgrading the underlying cluster tier and migrating indexes.\n- `PAUSED`: The cluster is paused.")
    stored_source: ClusterSearchIndexStoredSource | None = Field(default=None, alias="storedSource", description="Flag that indicates whether to store all fields (true) on Atlas Search. By default, Atlas doesn't store (false) the fields on Atlas Search.  Alternatively, you can specify an object that only contains the list of fields to store (include) or not store (exclude) on Atlas Search. Note that storing all fields (true) is not allowed for vector search indexes. To learn more, see documentation.")
    type: Literal["search", "vectorSearch"] | None = Field(default=None, description="Type of the index. Default type is search.")
