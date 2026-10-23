"""Generated model for GeoSharding20240805. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.geo_sharding20240805_custom_zone_mapping import GeoSharding20240805CustomZoneMapping
from pyatlassdk.models.managed_namespaces import ManagedNamespaces

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GeoSharding20240805(BaseModel):
    """Generated model for GeoSharding20240805."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    custom_zone_mapping: GeoSharding20240805CustomZoneMapping | None = Field(default=None, alias="customZoneMapping", description="List that contains comma-separated key value pairs to map zones to geographic regions. These pairs map an ISO 3166-1a2 location code, with an ISO 3166-2 subdivision code when possible, to a unique 24-hexadecimal string that identifies the custom zone.\n\n The 24-hexadecimal string corresponds to a `Replication Specifications` `zoneId` property.\n\nThis parameter returns an empty object if no custom zones exist.\n\nExample: `{\"US-VA\": \"6716c5a804f4ce77e899bf99\", \"DE\": \"6716c5a804f4ce77e899bf9a\"}`.")
    managed_namespaces: list[ManagedNamespaces] | None = Field(default=None, alias="managedNamespaces", description="List that contains a namespace for a Global Cluster. MongoDB Cloud manages this cluster.")
    self_managed_sharding: bool | None = Field(default=None, alias="selfManagedSharding", description="Boolean that controls which management mode the Global Cluster is operating under. If this parameter is true Self-Managed Sharding is enabled and users are in control of the zone sharding within the Global Cluster. If this parameter is false Atlas-Managed Sharding is enabled and Atlas is control of zone sharding within the Global Cluster.")
