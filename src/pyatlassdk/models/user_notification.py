"""Generated model for UserNotification. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class UserNotification(BaseModel):
    """User notification configuration for MongoDB Cloud to send information when an event triggers an alert condition."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    delay_min: int | None = Field(default=None, alias="delayMin", description="Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification.")
    email_enabled: bool | None = Field(default=None, alias="emailEnabled", description="Flag that indicates whether MongoDB Cloud should send email notifications. The resource requires this parameter when one of the following values have been set:\n\n- `\"notifications.[n].typeName\" : \"ORG\"`\n- `\"notifications.[n].typeName\" : \"GROUP\"`\n- `\"notifications.[n].typeName\" : \"USER\"`")
    interval_min: int | None = Field(default=None, alias="intervalMin", description="Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.\n\nPagerDuty, VictorOps, and OpsGenie notifications don't return this element. Configure and manage the notification interval within each of those services.")
    notifier_id: str | None = Field(default=None, alias="notifierId", description="The `notifierId` is a system-generated unique identifier assigned to each notification method. This is needed when updating third-party notifications without requiring explicit authentication credentials.")
    sms_enabled: bool | None = Field(default=None, alias="smsEnabled", description="Flag that indicates whether MongoDB Cloud should send text message notifications. The resource requires this parameter when one of the following values have been set:\n\n- `\"notifications.[n].typeName\" : \"ORG\"`\n- `\"notifications.[n].typeName\" : \"GROUP\"`\n- `\"notifications.[n].typeName\" : \"USER\"`")
    type_name: Literal["USER"] = Field(alias="typeName", description="Human-readable label that displays the alert notification type.")
    username: str | None = Field(default=None, description="MongoDB Cloud username of the person to whom MongoDB Cloud sends notifications. Specify only MongoDB Cloud users who belong to the project that owns the alert configuration. The resource requires this parameter when `\"notifications.[n].typeName\" : \"USER\"`.")
