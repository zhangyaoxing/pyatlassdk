"""Generated model for MongoDBAccessLogs. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class MongoDBAccessLogs(BaseModel):
    """Authentication attempt, one per object, made against the cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auth_result: bool | None = Field(default=None, alias="authResult", description="Flag that indicates whether the response should return successful authentication attempts only.")
    auth_source: str | None = Field(default=None, alias="authSource", description="Database against which someone attempted to authenticate.")
    failure_reason: str | None = Field(default=None, alias="failureReason", description="Reason that the authentication failed. Null if authentication succeeded.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    hostname: str | None = Field(default=None, description="Human-readable label that identifies the hostname of the target node that received the authentication attempt.")
    ip_address: str | None = Field(default=None, alias="ipAddress", description="Internet Protocol address that attempted to authenticate with the database.")
    log_line: str | None = Field(default=None, alias="logLine", description="Text of the host log concerning the authentication attempt.")
    timestamp: str | None = Field(default=None, description="Date and time when someone made this authentication attempt. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC.")
    username: str | None = Field(default=None, description="Username used to authenticate against the database.")
