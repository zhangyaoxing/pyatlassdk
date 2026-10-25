"""Generated model for IncomingWebhook. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.incoming_webhook_options import IncomingWebhookOptions

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class IncomingWebhook(BaseModel):
    """Generated model for IncomingWebhook."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str
    function_source: str
    respond_result: bool
    options: IncomingWebhookOptions | None = None
