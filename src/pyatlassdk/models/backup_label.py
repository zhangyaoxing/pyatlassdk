"""Generated model for BackupLabel. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class BackupLabel(BaseModel):
    """Collection of key-value pairs that represent custom data to add to the metadata file that MongoDB Cloud uploads to the bucket when the export job finishes."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    key: str | None = Field(default=None, description="Key for the metadata file that MongoDB Cloud uploads to the bucket when the export job finishes.")
    value: str | None = Field(default=None, description="Value for the key to include in file that MongoDB Cloud uploads to the bucket when the export job finishes.")
