"""Generated model for ServiceAccountGroup. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ServiceAccountGroup(BaseModel):
    """Generated model for ServiceAccountGroup."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies your project. **NOTE**: Groups and projects are synonymous terms. Your group id is the same as your project id. For existing groups, your group/project id remains the same. The resource and corresponding endpoints use the term groups.")
    roles: list[str] | None = Field(default=None, description="A list of project roles assigned to the Service Account in this project.")
