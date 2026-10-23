"""Generated model for LegacyRegionsConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LegacyRegionsConfig(BaseModel):
    """Physical location where MongoDB Cloud provisions cluster nodes."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    pass
