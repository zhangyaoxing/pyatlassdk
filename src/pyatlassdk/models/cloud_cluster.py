"""Generated model for CloudCluster. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudCluster(BaseModel):
    """Settings that describe the clusters in each project that the API key is authorized to view."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    alert_count: int | None = Field(default=None, alias="alertCount", description="Whole number that indicates the quantity of alerts open on the cluster.")
    auth_enabled: bool | None = Field(default=None, alias="authEnabled", description="Flag that indicates whether authentication is required to access the nodes in this cluster.")
    availability: Literal["available", "dead", "unavailable", "warning"] | None = Field(default=None, description="Term that expresses how many nodes of the cluster can be accessed when MongoDB Cloud receives this request. This parameter returns `available` when all nodes are accessible, `warning` only when some nodes in the cluster can be accessed, `unavailable` when the cluster can't be accessed, or `dead` when the cluster has been deactivated.")
    backup_enabled: bool | None = Field(default=None, alias="backupEnabled", description="Flag that indicates whether the cluster can perform backups. If set to `true`, the cluster can perform backups. You must set this value to `true` for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to `false`, the cluster doesn't use MongoDB Cloud backups.")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="Unique 24-hexadecimal character string that identifies the cluster. Each `clusterId` is used only once across all MongoDB Cloud deployments.")
    data_size_bytes: int | None = Field(default=None, alias="dataSizeBytes", description="Total size of the data stored on each node in the cluster. The resource expresses this value in bytes.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the cluster.")
    node_count: int | None = Field(default=None, alias="nodeCount", description="Whole number that indicates the quantity of nodes that comprise the cluster.")
    ssl_enabled: bool | None = Field(default=None, alias="sslEnabled", description="Flag that indicates whether TLS authentication is required to access the nodes in this cluster.")
    type: Annotated[Literal["REPLICA_SET", "SHARDED_CLUSTER"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable label that indicates the cluster type.")
    versions: list[str] | None = Field(default=None, description="List that contains the versions of MongoDB that each node in the cluster runs.")
