"""Generated model for VictorOpsNotification. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class VictorOpsNotification(BaseModel):
    """VictorOps notification configuration for MongoDB Cloud to send information when an event triggers an alert condition."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    delay_min: int | None = Field(default=None, alias="delayMin", description="Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification.")
    integration_id: str | None = Field(default=None, alias="integrationId", description="The id of the associated integration, the credentials of which to use for requests.")
    interval_min: int | None = Field(default=None, alias="intervalMin", description="Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.\n\nPagerDuty, VictorOps, and OpsGenie notifications don't return this element. Configure and manage the notification interval within each of those services.")
    notifier_id: str | None = Field(default=None, alias="notifierId", description="The `notifierId` is a system-generated unique identifier assigned to each notification method. This is needed when updating third-party notifications without requiring explicit authentication credentials.")
    type_name: Annotated[Literal["VICTOR_OPS"], BeforeValidator(upper_case)] = Field(alias="typeName", description="Human-readable label that displays the alert notification type.")
    victor_ops_api_key: str | None = Field(default=None, alias="victorOpsApiKey", description="API key that MongoDB Cloud needs to send alert notifications to Splunk On-Call. The resource requires this parameter when `\"notifications.[n].typeName\" : \"VICTOR_OPS\"`. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.\n\n**NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:\n\n* View or edit the alert through the Atlas UI.\n\n* Query the alert for the notification through the Atlas Administration API.")
    victor_ops_routing_key: str | None = Field(default=None, alias="victorOpsRoutingKey", description="Routing key that MongoDB Cloud needs to send alert notifications to Splunk On-Call. The resource requires this parameter when `\"notifications.[n].typeName\" : \"VICTOR_OPS\"`. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.")
