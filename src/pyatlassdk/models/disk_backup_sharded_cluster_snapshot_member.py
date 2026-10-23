"""Generated model for DiskBackupShardedClusterSnapshotMember. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupShardedClusterSnapshotMember(BaseModel):
    """Generated model for DiskBackupShardedClusterSnapshotMember."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="cloudProvider", description="Human-readable label that identifies the cloud provider.")
    id: str = Field(description="Unique 24-hexadecimal digit string that identifies the snapshot.")
    replica_set_name: str = Field(alias="replicaSetName", description="Human-readable label that identifies the shard or config host from which MongoDB Cloud took this snapshot.")
