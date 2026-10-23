"""Generated model for EncryptionAtRestConfigUpdateStalledAlertConfigViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.alert_matcher import AlertMatcher
from pyatlassdk.models.alerts_notification_root_for_group import AlertsNotificationRootForGroup
from pyatlassdk.models.event_severity import EventSeverity
from pyatlassdk.models.greater_than_time_threshold import GreaterThanTimeThreshold
from pyatlassdk.models.group_event_type_view_for_nds_group_alertable_encryption_at_rest_config_update_stalled import GroupEventTypeViewForNdsGroupAlertableEncryptionAtRestConfigUpdateStalled
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EncryptionAtRestConfigUpdateStalledAlertConfigViewForNdsGroup(BaseModel):
    """Configures the duration after which MongoDB Cloud alerts users that an Encryption at Rest configuration update has stalled."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created: datetime | None = Field(default=None, description="Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether someone enabled this alert configuration for the specified project.")
    event_type_name: GroupEventTypeViewForNdsGroupAlertableEncryptionAtRestConfigUpdateStalled = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns this alert configuration.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this alert configuration.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    matchers: list[AlertMatcher] | None = Field(default=None, description="Matching conditions for target resources.")
    notifications: list[AlertsNotificationRootForGroup] = Field(description="List that contains the targets that MongoDB Cloud sends notifications.")
    severity_override: EventSeverity | None = Field(default=None, alias="severityOverride")
    threshold: GreaterThanTimeThreshold | None = None
    updated: datetime | None = Field(default=None, description="Date and time when someone last updated this alert configuration. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
