"""Generated model for LiveMigrationRequest20240530. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.destination import Destination
from pyatlassdk.models.link import Link
from pyatlassdk.models.sharding_request import ShardingRequest
from pyatlassdk.models.source import Source

from pydantic import BaseModel, ConfigDict, Field

class LiveMigrationRequest20240530(BaseModel):
    """Generated model for LiveMigrationRequest20240530."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal digit string that identifies the migration request.")
    destination: Destination
    drop_destination_data: bool | None = Field(default=None, alias="dropDestinationData", description="Flag that indicates whether the migration process drops all collections from the destination cluster before the migration starts.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    migration_hosts: list[str] = Field(alias="migrationHosts", description="List of migration hosts used for this migration.")
    sharding: ShardingRequest | None = None
    source: Source
