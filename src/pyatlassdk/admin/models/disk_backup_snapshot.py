"""Generated model for DiskBackupSnapshot. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupSnapshot(BaseModel):
    """Generated model for DiskBackupSnapshot."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    created_at: datetime | None = Field(default=None, alias="createdAt", description="Date and time when MongoDB Cloud took the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    description: str | None = Field(default=None, description="Human-readable phrase or sentence that explains the purpose of the snapshot. The resource returns this parameter when `\"status\": \"onDemand\"`.")
    expires_at: datetime | None = Field(default=None, alias="expiresAt", description="Date and time when MongoDB Cloud deletes the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    frequency_type: Literal["hourly", "daily", "weekly", "monthly", "yearly"] | None = Field(default=None, alias="frequencyType", description="Human-readable label that identifies how often this snapshot triggers.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the snapshot.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    master_key_uuid: str | None = Field(default=None, alias="masterKeyUUID", description="Unique string that identifies the Amazon Web Services (AWS) Key Management Service (KMS) Customer Master Key (CMK) used to encrypt the snapshot. The resource returns this value when `\"encryptionEnabled\" : true`.")
    mongod_version: str | None = Field(default=None, alias="mongodVersion", description="Version of the MongoDB host that this snapshot backs up.")
    policy_items: list[str] | None = Field(default=None, alias="policyItems", description="List that contains unique identifiers for the policy items.")
    snapshot_type: Literal["onDemand", "scheduled", "fallback"] | None = Field(default=None, alias="snapshotType", description="Human-readable label that identifies when this snapshot triggers.")
    status: Literal["queued", "inProgress", "completed", "failed"] | None = Field(default=None, description="Human-readable label that indicates the stage of the backup process for this snapshot.")
    storage_size_bytes: int | None = Field(default=None, alias="storageSizeBytes", description="Number of bytes taken to store the backup at time of snapshot.")
    type: Literal["replicaSet", "shardedCluster"] | None = Field(default=None, description="Human-readable label that categorizes the cluster as a replica set or sharded cluster.")
