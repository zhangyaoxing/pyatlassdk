"""Generated model for DiffHostingFilesDiff. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiffHostingFilesDiff(BaseModel):
    """Generated model for DiffHostingFilesDiff."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    added: list[str] | None = None
    deleted: list[str] | None = None
    modified: list[str] | None = None
