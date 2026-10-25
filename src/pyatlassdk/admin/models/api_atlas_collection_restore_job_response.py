"""Generated model for ApiAtlasCollectionRestoreJobResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.api_atlas_collection_restore_job_index_status import ApiAtlasCollectionRestoreJobIndexStatus
from pyatlassdk.admin.models.api_atlas_restore_collection_namespace_view import ApiAtlasRestoreCollectionNamespaceView
from pyatlassdk.admin.models.api_atlas_restore_database_namespace_view import ApiAtlasRestoreDatabaseNamespaceView

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasCollectionRestoreJobResponse(BaseModel):
    """Collection restore job summary including the list of databases and collections in the restore scope (up to 100 items each)."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection_suffix: str | None = Field(default=None, alias="collectionSuffix", description="Suffix applied to restored collection names.")
    collections: list[ApiAtlasRestoreCollectionNamespaceView] | None = Field(default=None, description="List of collections in the restore scope (up to 100 items).")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date and time when the restore job was created (ISO 8601 format in UTC).")
    database_suffix: str | None = Field(default=None, alias="databaseSuffix", description="Suffix applied to restored database names.")
    databases: list[ApiAtlasRestoreDatabaseNamespaceView] | None = Field(default=None, description="List of databases in the restore scope (up to 100 items).")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Error message when the job has failed or been canceled.")
    finished_at: datetime | None = Field(default=None, alias="finishedAt", description="Date and time when the restore job finished (ISO 8601 format in UTC).")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the collection restore job.")
    index_status: ApiAtlasCollectionRestoreJobIndexStatus | None = Field(default=None, alias="indexStatus")
    index_strategy: Annotated[Literal["ALL", "NONE", "ALL_EXCEPT_TTL"], BeforeValidator(upper_case)] | None = Field(default=None, alias="indexStrategy", description="Strategy for restoring indexes (all, none, or all except TTL).")
    oplog_inc: int | None = Field(default=None, alias="oplogInc", description="Oplog increment for point-in-time restore.")
    oplog_ts: int | None = Field(default=None, alias="oplogTs", description="Oplog timestamp (seconds part) for point-in-time restore.")
    point_in_time_utc_seconds: int | None = Field(default=None, alias="pointInTimeUtcSeconds", description="Point-in-time restore time in seconds since UNIX epoch.")
    restored_documents: int | None = Field(default=None, alias="restoredDocuments", description="Number of documents restored so far across all supported collections.")
    snapshot_id: str | None = Field(default=None, alias="snapshotId", description="Unique 24-hexadecimal digit string that identifies the snapshot being restored.")
    state: Annotated[Literal["INITIALIZING", "IN_PROGRESS", "FINALIZING", "SUCCESSFUL", "CANCELED", "FAILED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Current state of the collection restore job. A `SUCCESSFUL` job can include individual `UNSUPPORTED` collection restores. Use the restore job collections endpoint to get per-collection detailed states.")
    target_cluster_name: str | None = Field(default=None, alias="targetClusterName", description="Human-readable label that identifies the target cluster.")
    target_group_id: str | None = Field(default=None, alias="targetGroupId", description="Unique 24-hexadecimal digit string that identifies the target group.")
    total_documents: int | None = Field(default=None, alias="totalDocuments", description="Total number of documents across all supported collections in the restore job. This value may initially reflect an estimate based on collection metadata and can change as accurate document counts become available during the restore.")
    write_strategy: Annotated[Literal["CREATE_NEW", "OVERWRITE_EXISTING"], BeforeValidator(upper_case)] | None = Field(default=None, alias="writeStrategy", description="Strategy for writing data on the target (create as new or overwrite existing). With `OVERWRITE_EXISTING`, any writes to the affected databases or collections during the restore will be lost when the existing namespaces are dropped and replaced. To avoid data loss, stop writes to the affected namespaces before starting the restore.")
