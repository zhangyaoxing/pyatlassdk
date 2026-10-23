"""Generated model for BackupSnapshotPart. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class BackupSnapshotPart(BaseModel):
    """Characteristics that identify this snapshot."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster with the snapshots you want to return.")
    completed_time: datetime | None = Field(default=None, alias="completedTime", description="Date and time when the snapshot completed. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    compression_setting: Annotated[Literal["NONE", "GZIP"], BeforeValidator(upper_case)] | None = Field(default=None, alias="compressionSetting", description="Human-readable label that identifies the method of compression for the snapshot.")
    data_size_bytes: int | None = Field(default=None, alias="dataSizeBytes", description="Total size of the data stored on each node in the cluster. This parameter expresses its value in bytes.")
    encryption_enabled: bool | None = Field(default=None, alias="encryptionEnabled", description="Flag that indicates whether someone encrypted this snapshot.")
    fcv: str | None = Field(default=None, description="Number that indicates the feature compatibility version of MongoDB that the replica set primary ran when MongoDB Cloud created the snapshot.")
    file_size_bytes: int | None = Field(default=None, alias="fileSizeBytes", description="Number that indicates the total size of the data files in bytes.")
    machine_id: str | None = Field(default=None, alias="machineId", description="Hostname and port that indicate the node on which MongoDB Cloud created the snapshot.")
    master_key_uuid: str | None = Field(default=None, alias="masterKeyUUID", description="Unique string that identifies the Key Management Interoperability (KMIP) master key used to encrypt the snapshot data. The resource returns this parameter when `\"parts.encryptionEnabled\" : true`.")
    mongod_version: str | None = Field(default=None, alias="mongodVersion", description="Number that indicates the version of MongoDB that the replica set primary ran when MongoDB Cloud created the snapshot.")
    replica_set_name: str | None = Field(default=None, alias="replicaSetName", description="Human-readable label that identifies the replica set.")
    replica_state: str | None = Field(default=None, alias="replicaState", description="The node's role at the time when snapshot process began.")
    storage_size_bytes: int | None = Field(default=None, alias="storageSizeBytes", description="Number that indicates the total size of space allocated for document storage.")
    type_name: Annotated[Literal["REPLICA_SET", "CONFIG_SERVER", "CONFIG_SERVER_REPLICA_SET", "CONFIG_SHARD_REPLICA_SET"], BeforeValidator(upper_case)] | None = Field(default=None, alias="typeName", description="Human-readable label that identifies the type of server from which MongoDB Cloud took this snapshot.")
