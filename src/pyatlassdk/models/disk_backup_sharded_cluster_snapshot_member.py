"""Generated model for DiskBackupShardedClusterSnapshotMember. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class DiskBackupShardedClusterSnapshotMember(BaseModel):
    """Generated model for DiskBackupShardedClusterSnapshotMember."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS", "AZURE", "GCP"] = Field(alias="cloudProvider", description="Human-readable label that identifies the cloud provider.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the snapshot.")
    replica_set_name: str = Field(alias="replicaSetName", description="Human-readable label that identifies the shard or config host from which MongoDB Cloud took this snapshot.")
