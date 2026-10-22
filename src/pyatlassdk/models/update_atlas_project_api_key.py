"""Generated model for UpdateAtlasProjectApiKey. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class UpdateAtlasProjectApiKey(BaseModel):
    """Generated model for UpdateAtlasProjectApiKey."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    desc: str | None = Field(default=None, description="Purpose or explanation provided when someone creates this project API key.")
    roles: list[str] | None = Field(default=None, description="List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this project.")
