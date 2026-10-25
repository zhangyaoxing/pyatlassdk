"""Generated model for GroupServiceAccountUpdateRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GroupServiceAccountUpdateRequest(BaseModel):
    """Generated model for GroupServiceAccountUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str | None = Field(default=None, description="Human readable description for the Service Account.")
    name: str | None = Field(default=None, description="Human-readable name for the Service Account. The name is modifiable and does not have to be unique.")
    roles: list[str] | None = Field(default=None, description="A list of Project roles associated with the Service Account.")
