"""Generated model for ThirdPartyServiceConstructor. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.incoming_webhook import IncomingWebhook

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ThirdPartyServiceConstructor(BaseModel):
    """Generated model for ThirdPartyServiceConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="The service name.")
    type: Literal["aws", "twilio", "github", "gcm", "http"] | None = Field(default=None, description="The type of service.")
    incoming_webhooks: list[IncomingWebhook] | None = None
    version: int | None = None
