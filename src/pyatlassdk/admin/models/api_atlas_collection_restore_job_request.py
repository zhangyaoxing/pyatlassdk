"""Generated model for ApiAtlasCollectionRestoreJobRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.api_atlas_restore_collection_namespace_view import ApiAtlasRestoreCollectionNamespaceView
from pyatlassdk.admin.models.api_atlas_restore_database_namespace_view import ApiAtlasRestoreDatabaseNamespaceView

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiAtlasCollectionRestoreJobRequest(BaseModel):
    """Request body for creating a collection restore job."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection_suffix: str | None = Field(default=None, alias="collectionSuffix", description="Optional suffix applied to restored collection names.")
    collections: list[ApiAtlasRestoreCollectionNamespaceView] | None = Field(default=None, description="List of collections to restore (up to 100 items).")
    database_suffix: str | None = Field(default=None, alias="databaseSuffix", description="Optional suffix applied to restored database names.")
    databases: list[ApiAtlasRestoreDatabaseNamespaceView] | None = Field(default=None, description="List of databases to restore (up to 100 items).")
    index_strategy: Annotated[Literal["ALL", "NONE", "ALL_EXCEPT_TTL"], BeforeValidator(upper_case)] = Field(alias="indexStrategy", description="Strategy for restoring indexes (all, none, or all except TTL).")
    oplog_inc: int | None = Field(default=None, alias="oplogInc", description="Oplog increment for point-in-time restore.")
    oplog_ts: int | None = Field(default=None, alias="oplogTs", description="Oplog timestamp (seconds part) for point-in-time restore.")
    point_in_time_utc_seconds: int | None = Field(default=None, alias="pointInTimeUtcSeconds", description="Point-in-time restore time in seconds since UNIX epoch.")
    snapshot_id: str | None = Field(default=None, alias="snapshotId", description="ID of the snapshot to restore.")
    target_cluster_name: str = Field(alias="targetClusterName", description="Target cluster name.")
    target_group_id: str = Field(alias="targetGroupId", description="Unique 24-hexadecimal digit string that identifies the target group.")
    write_strategy: Annotated[Literal["CREATE_NEW", "OVERWRITE_EXISTING"], BeforeValidator(upper_case)] = Field(alias="writeStrategy", description="Strategy for writing data on the target (create as new or overwrite existing). With `OVERWRITE_EXISTING`, any writes to the affected databases or collections during the restore will be lost when the existing namespaces are dropped and replaced. To avoid data loss, stop writes to the affected namespaces before starting the restore.")
