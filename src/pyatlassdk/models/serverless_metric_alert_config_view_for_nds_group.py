"""Generated model for ServerlessMetricAlertConfigViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.alert_matcher import AlertMatcher
from pyatlassdk.models.alerts_notification_root_for_group import AlertsNotificationRootForGroup
from pyatlassdk.models.event_severity import EventSeverity
from pyatlassdk.models.link import Link
from pyatlassdk.models.serverless_event_type_view_alertable import ServerlessEventTypeViewAlertable
from pyatlassdk.models.serverless_metric_threshold import ServerlessMetricThreshold

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ServerlessMetricAlertConfigViewForNdsGroup(BaseModel):
    """Serverless metric alert configuration allows to select which serverless database metrics trigger alerts and how users are notified."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether someone enabled this alert configuration for the specified project.")
    event_type_name: ServerlessEventTypeViewAlertable = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns this alert configuration.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this alert configuration.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    matchers: list[AlertMatcher] | None = Field(default=None, description="Matching conditions for target resources.")
    metric_threshold: ServerlessMetricThreshold | None = Field(default=None, alias="metricThreshold")
    notifications: list[AlertsNotificationRootForGroup] = Field(description="List that contains the targets that MongoDB Cloud sends notifications.")
    severity_override: EventSeverity | None = Field(default=None, alias="severityOverride")
    updated: datetime | None = Field(default=None, description="Date and time when someone last updated this alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
