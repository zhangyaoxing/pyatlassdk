"""Generated model for ClusterEventViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.cluster_event_type_view_for_nds_group import ClusterEventTypeViewForNdsGroup
from pyatlassdk.models.link import Link
from pyatlassdk.models.raw import Raw

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterEventViewForNdsGroup(BaseModel):
    """Cluster event identifies different activities about cluster of mongod hosts."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created: datetime = Field(description="Date and time when this event occurred. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    event_type_name: ClusterEventTypeViewForNdsGroup = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The `eventId` identifies the specific event.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the event.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    raw: Raw | None = None
    shard_name: str | None = Field(default=None, alias="shardName", description="Human-readable label of the shard associated with the event.")
