"""Generated model for CreatePushBasedLogExportProjectRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CreatePushBasedLogExportProjectRequest(BaseModel):
    """Generated model for CreatePushBasedLogExportProjectRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    bucket_name: str = Field(alias="bucketName", description="The name of the bucket to which the agent will send the logs to.")
    iam_role_id: str = Field(alias="iamRoleId", description="ID of the AWS IAM role that will be used to write to the S3 bucket.")
    prefix_path: str = Field(alias="prefixPath", description="S3 directory in which vector will write to in order to store the logs. An empty string denotes the root directory.")
