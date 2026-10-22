"""Generated model for EmailNotification. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class EmailNotification(BaseModel):
    """Email notification configuration for MongoDB Cloud to send information when an event triggers an alert condition."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    delay_min: int | None = Field(default=None, alias="delayMin", description="Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification.")
    email_address: str | None = Field(default=None, alias="emailAddress", description="Email address to which MongoDB Cloud sends alert notifications. The resource requires this parameter when `\"notifications.[n].typeName\" : \"EMAIL\"`. You don't need to set this value to send emails to individual or groups of MongoDB Cloud users including:\n\n- specific MongoDB Cloud users (`\"notifications.[n].typeName\" : \"USER\"`)\n- MongoDB Cloud users with specific project roles (`\"notifications.[n].typeName\" : \"GROUP\"`)\n- MongoDB Cloud users with specific organization roles (`\"notifications.[n].typeName\" : \"ORG\"`)\n- MongoDB Cloud teams (`\"notifications.[n].typeName\" : \"TEAM\"`)\n\nTo send emails to one MongoDB Cloud user or grouping of users, set the `notifications.[n].emailEnabled` parameter.")
    interval_min: int | None = Field(default=None, alias="intervalMin", description="Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.\n\nPagerDuty, VictorOps, and OpsGenie notifications don't return this element. Configure and manage the notification interval within each of those services.")
    notifier_id: str | None = Field(default=None, alias="notifierId", description="The `notifierId` is a system-generated unique identifier assigned to each notification method. This is needed when updating third-party notifications without requiring explicit authentication credentials.")
    type_name: Literal["EMAIL"] = Field(alias="typeName", description="Human-readable label that displays the alert notification type.")
