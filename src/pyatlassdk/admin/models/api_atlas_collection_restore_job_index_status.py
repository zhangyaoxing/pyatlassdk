"""Generated model for ApiAtlasCollectionRestoreJobIndexStatus. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasCollectionRestoreJobIndexStatus(BaseModel):
    """Overall index build status for a collection restore job."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    failed_collection_count: int | None = Field(default=None, alias="failedCollectionCount", description="Number of collections that failed to build indexes.")
    state: Annotated[Literal["NOT_STARTED", "IN_PROGRESS", "SUCCESSFUL", "FAILED", "NOT_RESTORED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Index build state indicating the status of index creation during or after a restore operation.")
