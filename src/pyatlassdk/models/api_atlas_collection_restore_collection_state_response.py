"""Generated model for ApiAtlasCollectionRestoreCollectionStateResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.api_atlas_collection_restore_index_status import ApiAtlasCollectionRestoreIndexStatus

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasCollectionRestoreCollectionStateResponse(BaseModel):
    """Collection-level state within a collection restore job."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    effective_target_namespace: str | None = Field(default=None, alias="effectiveTargetNamespace", description="Actual target namespace after restore (e.g. after conflict rename).")
    index_status: ApiAtlasCollectionRestoreIndexStatus | None = Field(default=None, alias="indexStatus")
    restored_documents: int | None = Field(default=None, alias="restoredDocuments", description="Number of documents restored so far.")
    source_namespace: str | None = Field(default=None, alias="sourceNamespace", description="Source namespace that was requested to restore.")
    state: Annotated[Literal["NOT_STARTED", "IN_PROGRESS", "FINALIZING", "NOT_FOUND", "UNSUPPORTED", "SUCCESSFUL", "ROLLBACK", "NOT_RESTORED", "FAILED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Current state of this collection within the restore job.")
    target_namespace: str | None = Field(default=None, alias="targetNamespace", description="Requested target namespace for the restored collection.")
    total_documents: int | None = Field(default=None, alias="totalDocuments", description="Total document count for this collection.")
