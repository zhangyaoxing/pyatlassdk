"""Generated model for StreamProcessorMetricAlertConfigViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.alerts_notification_root_for_group import AlertsNotificationRootForGroup
from pyatlassdk.models.event_severity import EventSeverity
from pyatlassdk.models.link import Link
from pyatlassdk.models.stream_processor_event_type_view_alertable_with_threshold import StreamProcessorEventTypeViewAlertableWithThreshold
from pyatlassdk.models.stream_processor_metric_threshold import StreamProcessorMetricThreshold
from pyatlassdk.models.streams_matcher import StreamsMatcher

from pydantic import BaseModel, ConfigDict, Field

class StreamProcessorMetricAlertConfigViewForNdsGroup(BaseModel):
    """Stream Processor threshold alert configuration allows to select thresholds on metrics which trigger alerts and how users are notified."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether someone enabled this alert configuration for the specified project.")
    event_type_name: StreamProcessorEventTypeViewAlertableWithThreshold = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns this alert configuration.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this alert configuration.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    matchers: list[StreamsMatcher] | None = Field(default=None, description="List of rules that determine whether MongoDB Cloud checks an object for the alert configuration.")
    metric_threshold: StreamProcessorMetricThreshold | None = Field(default=None, alias="metricThreshold")
    notifications: list[AlertsNotificationRootForGroup] = Field(description="List that contains the targets that MongoDB Cloud sends notifications.")
    severity_override: EventSeverity | None = Field(default=None, alias="severityOverride")
    threshold: StreamProcessorMetricThreshold | None = None
    updated: datetime | None = Field(default=None, description="Date and time when someone last updated this alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
