"""Generated model for AvailableClustersDeployment. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class AvailableClustersDeployment(BaseModel):
    """Deployments that can be migrated to MongoDB Atlas."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    agent_version: str | None = Field(default=None, alias="agentVersion", description="Version of MongoDB Agent that monitors/manages the cluster.")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster.")
    db_size_bytes: int | None = Field(default=None, alias="dbSizeBytes", description="Size of this database on disk at the time of the request expressed in bytes.")
    feature_compatibility_version: str = Field(alias="featureCompatibilityVersion", description="Version of MongoDB features that this cluster supports.")
    managed: bool = Field(description="Flag that indicates whether Automation manages this cluster.")
    mongo_db_version: str = Field(alias="mongoDBVersion", description="Version of MongoDB that this cluster runs.")
    name: str = Field(description="Human-readable label that identifies this cluster.")
    oplog_size_mb: int | None = Field(default=None, alias="oplogSizeMB", description="Size of the Oplog on disk at the time of the request expressed in MB.")
    sharded: bool = Field(description="Flag that indicates whether someone configured this cluster as a sharded cluster.\n\n- If `true`, this cluster serves as a sharded cluster.\n- If `false`, this cluster serves as a replica set.")
    shards_size: int | None = Field(default=None, alias="shardsSize", description="Number of shards that comprise this cluster.")
    tls_enabled: bool = Field(alias="tlsEnabled", description="Flag that indicates whether someone enabled TLS for this cluster.")
