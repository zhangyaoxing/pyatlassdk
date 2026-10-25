"""Generated model for LogForwardingPolicy. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogForwardingPolicy(BaseModel):
    """Generated model for LogForwardingPolicy."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Literal["single", "batch"] | None = None
