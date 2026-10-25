"""Generated model for NullTypeSchemaValidationSetting. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class NullTypeSchemaValidationSetting(BaseModel):
    """Generated model for NullTypeSchemaValidationSetting."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = None
