"""Generated model for BackupRestoreJob. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.api_bson_timestamp_view import ApiBSONTimestampView
from pyatlassdk.admin.models.backup_restore_job_delivery import BackupRestoreJobDelivery
from pyatlassdk.admin.models.link import Link
from pyatlassdk.admin.models.restore_job_file_hash import RestoreJobFileHash

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class BackupRestoreJob(BaseModel):
    """Generated model for BackupRestoreJob."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    batch_id: str | None = Field(default=None, alias="batchId", description="Unique 24-hexadecimal digit string that identifies the batch to which this restore job belongs. This parameter exists only for a sharded cluster restore.")
    checkpoint_id: str | None = Field(default=None, alias="checkpointId", description="Unique 24-hexadecimal digit string that identifies the sharded cluster checkpoint. The checkpoint represents the point in time back to which you want to restore you data. This parameter applies when `\"delivery.methodName\" : \"AUTOMATED_RESTORE\"`. Use this parameter with sharded clusters only.\n\n- If you set `checkpointId`, you can't set `oplogInc`, `oplogTs`, `snapshotId`, or `pointInTimeUTCMillis`.\n- If you provide this parameter, this endpoint restores all data up to this checkpoint to the database you specify in the `delivery` object.")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster with the snapshot you want to return. This parameter returns for restore clusters.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster containing the snapshots you want to retrieve.")
    created: datetime | None = Field(default=None, description="Date and time when someone requested this restore job. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    delivery: BackupRestoreJobDelivery
    deployment_job_id: str | None = Field(default=None, alias="deploymentJobId", description="Unique 24-hexadecimal digit string that identifies the an imported deployment job. This parameter exists when restoring from an imported snapshot/cluster shot.")
    encryption_enabled: bool | None = Field(default=None, alias="encryptionEnabled", description="Flag that indicates whether someone encrypted the data in the restored snapshot.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns the snapshots.")
    hashes: list[RestoreJobFileHash] | None = Field(default=None, description="List that contains documents mapping each restore file to a hashed checksum. This parameter applies after you download the corresponding `delivery.url`. If `\"methodName\" : \"HTTP\"`, this list contains one object that represents the hash of the `.tar.gz` file.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the restore job.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    master_key_uuid: str | None = Field(default=None, alias="masterKeyUUID", description="Universally Unique Identifier (UUID) that identifies the Key Management Interoperability (KMIP) master key used to encrypt the snapshot data. This parameter applies only when `\"encryptionEnabled\" : \"true\"`.")
    oplog_inc: int | None = Field(default=None, alias="oplogInc", description="Thirty-two-bit incrementing ordinal that represents operations within a given second. When paired with `oplogTs`, this represents the point in time to which MongoDB Cloud restores your data. This parameter applies when `\"delivery.methodName\" : \"AUTOMATED_RESTORE\"`.\n\n- If you set `oplogInc`, you must set `oplogTs`, and can't set `checkpointId`, `snapshotId`, or `pointInTimeUTCMillis`.\n- If you provide this parameter, this endpoint restores all data up to and including this Oplog timestamp to the database you specified in the `delivery` object.")
    oplog_ts: str | None = Field(default=None, alias="oplogTs", description="Date and time from which you want to restore this snapshot. This parameter expresses its value in ISO 8601 format in UTC. This represents the first part of an Oplog timestamp. When paired with `oplogInc`, they represent the last database operation to which you want to restore your data. This parameter applies when `\"delivery.methodName\" : \"AUTOMATED_RESTORE\"`. Run a query against `local.oplog.rs` on your replica set to find the desired timestamp.\n\n- If you set `oplogTs`, you must set `oplogInc`, and you can't set `checkpointId`, `snapshotId`, or `pointInTimeUTCMillis`.\n- If you provide this parameter, this endpoint restores all data up to and including this Oplog timestamp to the database you specified in the `delivery` object.")
    point_in_time_utc_millis: int | None = Field(default=None, alias="pointInTimeUTCMillis", description="Timestamp from which you want to restore this snapshot. This parameter expresses its value in the number of milliseconds elapsed since the UNIX epoch. This timestamp must fall within the last 24 hours of the current time. This parameter applies when `\"delivery.methodName\" : \"AUTOMATED_RESTORE\"`.\n\n- If you provide this parameter, this endpoint restores all data up to this point in time to the database you specified in the `delivery` object.\n- If you set `pointInTimeUTCMillis`, you can't set `oplogInc`, `oplogTs`, `snapshotId`, or `checkpointId`.")
    snapshot_id: str | None = Field(default=None, alias="snapshotId", description="Unique 24-hexadecimal digit string that identifies the snapshot to restore. If you set `snapshotId`, you can't set `oplogInc`, `oplogTs`, `pointInTimeUTCMillis`, or `checkpointId`.")
    status_name: Annotated[Literal["IN_PROGRESS", "BROKEN", "KILLED", "FINISHED"], BeforeValidator(upper_case)] | None = Field(default=None, alias="statusName", description="Human-readable label that identifies the status of the downloadable file at the time of the request.")
    timestamp: ApiBSONTimestampView | None = None
