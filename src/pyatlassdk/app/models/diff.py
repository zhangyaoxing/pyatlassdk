"""Generated model for Diff. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.diff_hosting_files_diff import DiffHostingFilesDiff

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Diff(BaseModel):
    """Generated model for Diff."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    diffs: list[str] | None = Field(default=None, description="A list where each item is the line-by-line diff for a specific\nconfiguration file.")
    hosting_files_diff: DiffHostingFilesDiff | None = Field(default=None, description="The filenames of hosted files that have been added, removed, or\nmodified.")
