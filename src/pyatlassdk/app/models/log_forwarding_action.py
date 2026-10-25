"""Generated model for LogForwardingAction. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogForwardingAction(BaseModel):
    """Generated model for LogForwardingAction."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Literal["collection", "function"] | None = None
    name: str | None = None
    data_source: str | None = None
    database: str | None = None
    collection: str | None = None
