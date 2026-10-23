"""Generated model for SearchMappings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.search_mappings_dynamic import SearchMappingsDynamic
from pyatlassdk.models.search_mappings_fields import SearchMappingsFields

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SearchMappings(BaseModel):
    """Index specifications for the collection's fields."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    dynamic: SearchMappingsDynamic | None = Field(default=None, description="Indicates whether the index uses static, default dynamic, or configurable dynamic mappings. Set to `true` to enable dynamic mapping with default type set or define object to specify the name of the configured type sets for dynamic mapping. If you specify configurable dynamic mappings, you must define the referred type sets in the `typeSets` field. Set to `false` to use only static mappings through `mappings.fields`.")
    fields: SearchMappingsFields | None = Field(default=None, description="One or more field specifications for the Atlas Search index. Required if `mappings.dynamic` is omitted or set to `false`.")
