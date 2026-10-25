"""Generated model for LogForwarder. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.log_forwarding_action import LogForwardingAction
from pyatlassdk.app.models.log_forwarding_policy import LogForwardingPolicy
from pyatlassdk.app.models.log_status import LogStatus
from pyatlassdk.app.models.log_type import LogType

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogForwarder(BaseModel):
    """Generated model for LogForwarder."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id")
    name: str
    disabled: bool
    log_types: list[LogType]
    log_statuses: list[LogStatus]
    policy: LogForwardingPolicy
    action: LogForwardingAction
