"""Generated model for LiveMigrationResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class LiveMigrationResponse(BaseModel):
    """Generated model for LiveMigrationResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal digit string that identifies the migration job.")
    lag_time_seconds: int | None = Field(default=None, alias="lagTimeSeconds", description="Replication lag between the source and destination clusters. Atlas returns this setting only during an active migration, before the cutover phase.")
    migration_hosts: list[str] | None = Field(default=None, alias="migrationHosts", description="List of hosts running MongoDB Agents. These Agents can transfer your MongoDB data between one source and one destination cluster.")
    ready_for_cutover: bool | None = Field(default=None, alias="readyForCutover", description="Flag that indicates the migrated cluster can be cut over to MongoDB Atlas.")
    status: Literal["NEW", "WORKING", "FAILED", "COMPLETE", "EXPIRED"] | None = Field(default=None, description="Progress made in migrating one cluster to MongoDB Atlas.\n\n`NEW`: Someone scheduled a local cluster migration to MongoDB Atlas.\n\n`FAILED`: The cluster migration to MongoDB Atlas failed.\n\n`COMPLETE`: The cluster migration to MongoDB Atlas succeeded.\n\n`EXPIRED`: MongoDB Atlas prepares to begin the cut over of the migrating cluster when source and destination clusters have almost synchronized. If `\"readyForCutover\" : true`, this synchronization starts a timer of 120 hours. You can extend this timer. If the timer expires, MongoDB Atlas returns this status.\n\n`WORKING`: The cluster migration to MongoDB Atlas is performing one of the following tasks:\n\n- Preparing connections to source and destination clusters.\n- Replicating data from source to destination.\n- Verifying MongoDB Atlas connection settings.\n- Stopping replication after the cut over.")
