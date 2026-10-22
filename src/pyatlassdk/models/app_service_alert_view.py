"""Generated model for AppServiceAlertView. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.app_service_event_type_view_alertable import AppServiceEventTypeViewAlertable
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class AppServiceAlertView(BaseModel):
    """App Services alert notifies different activities about a BAAS application."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    acknowledged_until: datetime | None = Field(default=None, alias="acknowledgedUntil", description="Date and time until which this alert has been acknowledged. This parameter expresses its value in the ISO 8601 timestamp format in UTC. The resource returns this parameter if a MongoDB User previously acknowledged this alert.\n\n- To acknowledge this alert forever, set the parameter value to 100 years in the future.\n\n- To unacknowledge a previously acknowledged alert, do not set this parameter value.")
    acknowledgement_comment: str | None = Field(default=None, alias="acknowledgementComment", description="Comment that a MongoDB Cloud user submitted when acknowledging the alert.")
    acknowledging_username: str | None = Field(default=None, alias="acknowledgingUsername", description="MongoDB Cloud username of the person who acknowledged the alert. The response returns this parameter if a MongoDB Cloud user previously acknowledged this alert.")
    alert_config_id: str = Field(alias="alertConfigId", description="Unique 24-hexadecimal digit string that identifies the alert configuration that sets this alert.")
    created: datetime = Field(description="Date and time when MongoDB Cloud created this alert. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    event_type_name: AppServiceEventTypeViewAlertable = Field(alias="eventTypeName")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns this alert.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies this alert.")
    last_notified: datetime | None = Field(default=None, alias="lastNotified", description="Date and time that any notifications were last sent for this alert. This parameter expresses its value in the ISO 8601 timestamp format in UTC. The resource returns this parameter if MongoDB Cloud has sent notifications for this alert.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal character string that identifies the organization that owns the project to which this alert applies.")
    resolved: datetime | None = Field(default=None, description="Date and time that this alert changed to `\"status\" : \"CLOSED\"`. This parameter expresses its value in the ISO 8601 timestamp format in UTC. The resource returns this parameter once `\"status\" : \"CLOSED\"`.")
    severity: Literal["INFO", "WARNING", "ERROR", "CRITICAL"] | None = Field(default=None, description="Severity of the event.")
    status: Literal["CANCELLED", "CLOSED", "OPEN", "TRACKING"] = Field(description="State of this alert at the time you requested its details. TRACKING indicates the alert condition exists but has not persisted for the minimum notification delay. OPEN indicates the alert condition currently exists. CLOSED indicates the alert condition has been resolved.")
    updated: datetime = Field(description="Date and time when someone last updated this alert. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
