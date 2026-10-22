"""Generated model for GcsLogIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class GcsLogIntegrationRequest(BaseModel):
    """Request schema for creating or updating a Google Cloud Storage log export integration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    log_types: list[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Literal["GCS_LOG_EXPORT"] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    bucket_name: str = Field(alias="bucketName", description="Name of the bucket to store log files.")
    prefix_path: str = Field(alias="prefixPath", description="Path prefix where the log files will be stored. Atlas will add further sub-directories based on the log type.")
    role_id: str = Field(alias="roleId", description="Unique 24-character hexadecimal string that identifies the Atlas Cloud Provider Access role.")
