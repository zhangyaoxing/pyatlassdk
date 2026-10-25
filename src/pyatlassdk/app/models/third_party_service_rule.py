"""Generated model for ThirdPartyServiceRule. Do not edit manually."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ThirdPartyServiceRule(BaseModel):
    """[Deprecated] A rule for a third-party service."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str
    actions: Any | None = None
    when: dict[str, Any]
