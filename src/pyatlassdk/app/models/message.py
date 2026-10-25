"""Generated model for Message. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.message_state import MessageState

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Message(BaseModel):
    """Generated model for Message."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    allowed_ips: str | None = None
    app_id: str | None = Field(default=None, alias="appID")
    label: str | None = None
    message: str | None = None
    topic: str | None = None
    created: str | None = None
    sent: str | None = None
    state: MessageState | None = None
