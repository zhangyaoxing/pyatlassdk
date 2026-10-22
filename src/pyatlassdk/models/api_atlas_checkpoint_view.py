"""Generated model for ApiAtlasCheckpointView. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.api_checkpoint_part_view import ApiCheckpointPartView
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class ApiAtlasCheckpointView(BaseModel):
    """Generated model for ApiAtlasCheckpointView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster that contains the checkpoint.")
    completed: datetime | None = Field(default=None, description="Date and time when the checkpoint completed and the balancer restarted. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns the checkpoints.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies checkpoint.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    parts: list[ApiCheckpointPartView] | None = Field(default=None, description="Metadata that describes the complete snapshot.\n\n- For a replica set, this array contains a single document.\n- For a sharded cluster, this array contains one document for each shard plus one document for the config host.")
    restorable: bool | None = Field(default=None, description="Flag that indicates whether MongoDB Cloud can use the checkpoint for a restore.")
    started: datetime | None = Field(default=None, description="Date and time when the balancer stopped and began the checkpoint. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    timestamp: datetime | None = Field(default=None, description="Date and time to which the checkpoint restores. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
