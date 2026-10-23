"""Generated model for SearchMappings. Do not edit manually."""

from __future__ import annotations

from typing import Any
from pyatlassdk.models.fields import Fields

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchMappings(BaseModel):
    """Index specifications for the collection's fields."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    dynamic: dict[str, Any] | None = Field(default=None, description="Indicates whether the index uses static, default dynamic, or configurable dynamic mappings. Set to `true` to enable dynamic mapping with default type set or define object to specify the name of the configured type sets for dynamic mapping. If you specify configurable dynamic mappings, you must define the referred type sets in the `typeSets` field. Set to `false` to use only static mappings through `mappings.fields`.")
    fields: dict[str, Fields] | None = Field(default=None, description="One or more field specifications for the Atlas Search index. Required if `mappings.dynamic` is omitted or set to `false`.")
