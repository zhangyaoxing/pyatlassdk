"""Generated model for WebhookNotification. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class WebhookNotification(BaseModel):
    """Webhook notification configuration for MongoDB Cloud to send information when an event triggers an alert condition."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    delay_min: int | None = Field(default=None, alias="delayMin", description="Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification.")
    integration_id: str | None = Field(default=None, alias="integrationId", description="The id of the associated integration, the credentials of which to use for requests.")
    interval_min: int | None = Field(default=None, alias="intervalMin", description="Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.\n\nPagerDuty, VictorOps, and OpsGenie notifications don't return this element. Configure and manage the notification interval within each of those services.")
    notifier_id: str | None = Field(default=None, alias="notifierId", description="The `notifierId` is a system-generated unique identifier assigned to each notification method. This is needed when updating third-party notifications without requiring explicit authentication credentials.")
    type_name: Annotated[Literal["WEBHOOK"], BeforeValidator(upper_case)] = Field(alias="typeName", description="Human-readable label that displays the alert notification type.")
    webhook_body_template: str | None = Field(default=None, alias="webhookBodyTemplate", description="Template, using ${field} interpolation, that renders the HTTP body MongoDB Cloud sends with each webhook notification. Must render valid JSON. When unset, MongoDB Cloud sends its default JSON payload.")
    webhook_headers_template: str | None = Field(default=None, alias="webhookHeadersTemplate", description="Template, using ${field} interpolation, that renders the HTTP headers MongoDB Cloud sends with each webhook notification. Must render a JSON object mapping header name to header value. The webhook secret and the signature header are NOT exposed to templates.")
    webhook_secret: str | None = Field(default=None, alias="webhookSecret", description="Authentication secret for a webhook-based alert.\n\nAtlas returns this value if you set `notifications.[n].typeName` :`WEBHOOK` and either:\n* You set `notification.[n].webhookSecret` to a non-empty string\n* You set a default webhook secret either on the Integrations page, or with the Integrations API\n\n**NOTE**: When you view or edit the alert for a webhook notification, the secret appears completely redacted.")
    webhook_url: str | None = Field(default=None, alias="webhookUrl", description="Target URL for a webhook-based alert.\n\nAtlas returns this value if you set `\"notifications.[n].typeName\" :\"WEBHOOK\"` and either:\n* You set `notification.[n].webhookURL` to a non-empty string\n* You set a default webhook URL either on the Integrations page, or with the Integrations API\n\n**NOTE**: When you view or edit the alert for a Webhook URL notification, the URL appears partially redacted.")
