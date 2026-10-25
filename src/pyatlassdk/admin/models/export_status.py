"""Generated model for ExportStatus. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ExportStatus(BaseModel):
    """State of the Export Job."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    exported_collections: int | None = Field(default=None, alias="exportedCollections", description="Count of collections whose documents were exported to the Export Bucket.")
    total_collections: int | None = Field(default=None, alias="totalCollections", description="Total count of collections whose documents will be exported to the Export Bucket.")
