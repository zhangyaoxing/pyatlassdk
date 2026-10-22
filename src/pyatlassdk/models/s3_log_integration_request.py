"""Generated model for S3LogIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class S3LogIntegrationRequest(BaseModel):
    """Request schema for creating or updating an S3 log export integration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    log_types: list[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Literal["S3_LOG_EXPORT"] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    bucket_name: str = Field(alias="bucketName", description="Name of the bucket to store log files.")
    iam_role_id: str = Field(alias="iamRoleId", description="Unique 24-character hexadecimal string that identifies the AWS IAM role that Atlas uses to access the S3 bucket.")
    kms_key: str | None = Field(default=None, alias="kmsKey", description="AWS KMS key ID or ARN for server-side encryption (optional). If not provided, uses bucket default encryption settings.")
    prefix_path: str = Field(alias="prefixPath", description="Path prefix where the log files will be stored. Atlas will add further sub-directories based on the log type.")
    use_legacy_path_structure: bool | None = Field(default=None, alias="useLegacyPathStructure", description="When true, uses the legacy daily-folder path structure compatible with Push-Based Log Export: `{prefix}/{cluster}/{hostname}/{logType}/{YYYY-MM-DD}/{timestamp}-{logType}.log`. When false (default), uses the flat timestamped structure: `{prefix}/{cluster}/{hostname}/{logType}/{timestamp}-{logType}.log`.")
