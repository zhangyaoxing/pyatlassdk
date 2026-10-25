"""Generated model for CreateAtlasProjectApiKey. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CreateAtlasProjectApiKey(BaseModel):
    """Generated model for CreateAtlasProjectApiKey."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    desc: str = Field(description="Purpose or explanation provided when someone created this project API key.")
    roles: list[str] = Field(description="List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this project.")
