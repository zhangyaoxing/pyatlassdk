"""Generated model for DatabaseInheritedRole. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseInheritedRole(BaseModel):
    """Role inherited from another context for this database user."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    db: str = Field(description="Human-readable label that identifies the database on which someone grants the action to one MongoDB user.")
    role: str = Field(description="Human-readable label that identifies the role inherited. Set this value to `admin` for every role except `read` or `readWrite`.")
