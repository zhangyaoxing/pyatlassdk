"""Generated model for AppServiceMetricAlertConfigViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.alerts_notification_root_for_group import AlertsNotificationRootForGroup
from pyatlassdk.models.app_service_event_type_view_alertable_with_threshold import AppServiceEventTypeViewAlertableWithThreshold
from pyatlassdk.models.app_service_metric_matcher import AppServiceMetricMatcher
from pyatlassdk.models.app_service_metric_threshold import AppServiceMetricThreshold
from pyatlassdk.models.event_severity import EventSeverity
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AppServiceMetricAlertConfigViewForNdsGroup(BaseModel):
    """App Services metric alert configuration allows to select which app service metrics trigger alerts and how users are notified."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether someone enabled this alert configuration for the specified project.")
    event_type_name: AppServiceEventTypeViewAlertableWithThreshold = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns this alert configuration.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this alert configuration.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    matchers: list[AppServiceMetricMatcher] | None = Field(default=None, description="List of rules that determine whether MongoDB Cloud checks an object for the alert configuration. You can filter using the matchers array if the `eventTypeName` specifies an event for a host, replica set, or sharded cluster.")
    metric_threshold: AppServiceMetricThreshold | None = Field(default=None, alias="metricThreshold")
    notifications: list[AlertsNotificationRootForGroup] = Field(description="List that contains the targets that MongoDB Cloud sends notifications.")
    severity_override: EventSeverity | None = Field(default=None, alias="severityOverride")
    updated: datetime | None = Field(default=None, description="Date and time when someone last updated this alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
