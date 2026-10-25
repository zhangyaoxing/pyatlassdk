"""Generated model for NewMessage. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.message_state import MessageState

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class NewMessage(BaseModel):
    """Generated model for NewMessage."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    label: str
    message: str
    topic: str
    state: MessageState
