"""Generated model for ApiAtlasCollectionRestoreIndexStatus. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.api_atlas_collection_restore_index_status_failed_indexes_item import ApiAtlasCollectionRestoreIndexStatusFailedIndexesItem

from pydantic import BaseModel, ConfigDict, Field

class ApiAtlasCollectionRestoreIndexStatus(BaseModel):
    """Index build status for a collection within a restore job."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Error message if index build failed.")
    failed_indexes: list[ApiAtlasCollectionRestoreIndexStatusFailedIndexesItem] | None = Field(default=None, alias="failedIndexes", description="List of index specifications that failed to build (up to 64 items).")
    state: Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESSFUL", "FAILED", "NOT_RESTORED"] | None = Field(default=None, description="Index build state indicating the status of index creation during or after a restore operation.")
