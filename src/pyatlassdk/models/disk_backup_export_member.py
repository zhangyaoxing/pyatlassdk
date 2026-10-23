"""Generated model for DiskBackupExportMember. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupExportMember(BaseModel):
    """Generated model for DiskBackupExportMember."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    export_id: str | None = Field(default=None, alias="exportId", description="Unique 24-hexadecimal character string that identifies the the Cloud Backup snapshot export job for each shard in a sharded cluster.")
    replica_set_name: str | None = Field(default=None, alias="replicaSetName", description="Human-readable label that identifies the replica set on the sharded cluster.")
