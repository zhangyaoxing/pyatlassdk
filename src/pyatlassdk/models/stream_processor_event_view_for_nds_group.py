"""Generated model for StreamProcessorEventViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.link import Link
from pyatlassdk.models.raw import Raw
from pyatlassdk.models.stream_processor_event_type_view_for_nds_group import StreamProcessorEventTypeViewForNdsGroup

from pydantic import BaseModel, ConfigDict, Field

class StreamProcessorEventViewForNdsGroup(BaseModel):
    """Stream Processor event identifies different activities about a stream processor in Atlas Streams."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created: datetime = Field(description="Date and time when this event occurred. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    event_type_name: StreamProcessorEventTypeViewForNdsGroup = Field(alias="eventTypeName")
    from_tier: str | None = Field(default=None, alias="fromTier", description="Tier the stream processor scaled from.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The `eventId` identifies the specific event.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the event.")
    instance_name: str | None = Field(default=None, alias="instanceName", description="Name of the stream processing workspace associated with the event.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    processor_error_msg: str | None = Field(default=None, alias="processorErrorMsg", description="Error message linked to the stream processor associated with the event.")
    processor_name: str | None = Field(default=None, alias="processorName", description="Name of the stream processor associated with the event.")
    processor_state: str | None = Field(default=None, alias="processorState", description="State of the stream processor associated with the event.")
    raw: Raw | None = None
    reason: str | None = Field(default=None, description="Reason for the autoscale event.")
    region: str | None = Field(default=None, description="Cloud provider region in which the stream processor is running.")
    to_tier: str | None = Field(default=None, alias="toTier", description="Tier the stream processor scaled to.")
