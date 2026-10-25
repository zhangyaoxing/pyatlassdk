"""Generated model for DatabaseUserRole. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseUserRole(BaseModel):
    """Range of resources available to this database user."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    collection_name: str | None = Field(default=None, alias="collectionName", description="Collection on which this role applies.")
    database_name: str = Field(alias="databaseName", description="Database to which the user is granted access privileges.")
    role_name: Literal["atlasAdmin", "backup", "clusterMonitor", "dbAdmin", "dbAdminAnyDatabase", "enableSharding", "read", "readAnyDatabase", "readWrite", "readWriteAnyDatabase", "<a custom role name>"] = Field(alias="roleName", description="Human-readable label that identifies a group of privileges assigned to a database user. This value can either be a built-in role or a custom role.")
