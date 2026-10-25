"""Generated model for CustomZoneMappings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.zone_mapping import ZoneMapping

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomZoneMappings(BaseModel):
    """Generated model for CustomZoneMappings."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    custom_zone_mappings: list[ZoneMapping] = Field(alias="customZoneMappings", description="List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to the human-readable label for the desired custom zone. MongoDB Cloud maps the ISO 3166-1a2 code to the nearest geographical zone by default. Include this parameter to override the default mappings.\n\nThis parameter returns an empty object if no custom zones exist.")
