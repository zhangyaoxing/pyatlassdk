"""Generated model for AcknowledgeAlert. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class AcknowledgeAlert(BaseModel):
    """Acknowledging an alert prevents successive notifications. Specify the `acknowledgeUntil` date and optional comment or `unacknowledgeAlert` boolean."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    acknowledged_until: datetime | None = Field(default=None, alias="acknowledgedUntil", description="Date and time until which this alert has been acknowledged. This parameter expresses its value in the ISO 8601 timestamp format in UTC. The resource returns this parameter if a MongoDB User previously acknowledged this alert.")
    acknowledgement_comment: str | None = Field(default=None, alias="acknowledgementComment", description="Comment that a MongoDB Cloud user submitted when acknowledging the alert.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    unacknowledge_alert: bool | None = Field(default=None, alias="unacknowledgeAlert", description="Flag that indicates to unacknowledge a previously acknowledged alert. By default this value is set to false. If set to true, it will override the `acknowledgedUntil` parameter.")
