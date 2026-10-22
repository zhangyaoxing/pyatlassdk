"""Generated model for DataLakeAWSCloudProviderConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class DataLakeAWSCloudProviderConfig(BaseModel):
    """Configuration for running Data Federation in AWS."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    external_id: str | None = Field(default=None, alias="externalId", description="Unique identifier associated with the Identity and Access Management (IAM) role that the data lake assumes when accessing the data stores.")
    iam_assumed_role_arn: str | None = Field(default=None, alias="iamAssumedRoleARN", description="Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the data lake assumes when accessing data stores.")
    iam_user_arn: str | None = Field(default=None, alias="iamUserARN", description="Amazon Resource Name (ARN) of the user that the data lake assumes when accessing data stores.")
    role_id: str = Field(alias="roleId", description="Unique identifier of the role that the data lake can use to access the data stores.Required if specifying cloudProviderConfig.")
    test_s3_bucket: str = Field(alias="testS3Bucket", description="Name of the S3 data bucket that the provided role ID is authorized to access. Required if specifying `cloudProviderConfig`.")
