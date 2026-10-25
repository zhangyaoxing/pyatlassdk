"""Generated model for VectorSearchIndexDefinition. Do not edit manually."""

from __future__ import annotations

from typing import Any
from pyatlassdk.admin.models.basic_db_object import BasicDBObject

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class VectorSearchIndexDefinition(BaseModel):
    """The vector search index definition set by the user."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    fields: list[BasicDBObject] = Field(description="Settings that configure the fields, one per object, to index. You must define at least one \"vector\" type field. You can optionally define \"filter\" type fields also.")
    nested_root: str | None = Field(default=None, alias="nestedRoot", description="Top-level path to the array that contains vector fields. When provided, vector fields under this path are treated as nested.")
    num_partitions: int | None = Field(default=None, alias="numPartitions", description="Number of index partitions. Allowed values are [1, 2, 4].")
    stored_source: dict[str, Any] | None = Field(default=None, alias="storedSource", description="Flag that indicates whether to store all fields (true) on Atlas Search. By default, Atlas doesn't store (false) the fields on Atlas Search.  Alternatively, you can specify an object that only contains the list of fields to store (include) or not store (exclude) on Atlas Search. Note that storing all fields (true) is not allowed for vector search indexes. To learn more, see Stored Source Fields.")
