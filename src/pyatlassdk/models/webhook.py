"""Generated model for Webhook. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Webhook(BaseModel):
    """Details to integrate one webhook with one MongoDB Cloud project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    body_template: str | None = Field(default=None, alias="bodyTemplate", description="HTTP body template for a webhook-based alert. The rendered output MUST be valid JSON \u2014 MongoDB Cloud sends the rendered body with `Content-Type: application/json`. If the template fails to render, exceeds the 16 KB limit, or renders non-JSON output, MongoDB Cloud sends the webhook with its default JSON payload instead.")
    headers_template: str | None = Field(default=None, alias="headersTemplate", description="HTTP headers template for a webhook-based alert. The rendered output MUST be a JSON object mapping header name to header value (e.g. `{\"X-Custom-Header\": \"static-value\", \"X-Alert-Id\": \"${id}\"}`). Placeholders may reference any alert-view field plus `${eventType}`; the webhook secret and the signature header are NOT exposed to templates. If the template fails to render, exceeds the 4 KB limit, or renders output that is not a valid JSON name\u2192value object, MongoDB Cloud sends the webhook with its default set of headers instead.")
    id: str | None = Field(default=None, description="Integration id.")
    secret: str | None = Field(default=None, description="An optional field returned if your webhook is configured with a secret.\n\n**NOTE**: When you view or edit the alert for a webhook notification, the secret appears completely redacted.")
    type: Annotated[Literal["WEBHOOK"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
    url: str = Field(description="Endpoint web address to which MongoDB Cloud sends notifications.\n\n**NOTE**: When you view or edit the alert for a webhook notification, the URL appears partially redacted.")
