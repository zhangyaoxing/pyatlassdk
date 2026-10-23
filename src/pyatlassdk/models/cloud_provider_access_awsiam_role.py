"""Generated model for CloudProviderAccessAWSIAMRole. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.cloud_provider_access_feature_usage import CloudProviderAccessFeatureUsage

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderAccessAWSIAMRole(BaseModel):
    """Details that describe the features linked to the Amazon Web Services (AWS) Identity and Access Management (IAM) role."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    provider_name: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="providerName", description="Human-readable label that identifies the cloud provider of the role.")
    atlas_aws_account_arn: str | None = Field(default=None, alias="atlasAWSAccountArn", description="Amazon Resource Name that identifies the Amazon Web Services (AWS) user account that MongoDB Cloud uses when it assumes the Identity and Access Management (IAM) role.")
    atlas_assumed_role_external_id: str | None = Field(default=None, alias="atlasAssumedRoleExternalId", description="Unique external ID that MongoDB Cloud uses when it assumes the IAM role in your Amazon Web Services (AWS) account.")
    authorized_date: datetime | None = Field(default=None, alias="authorizedDate", description="Date and time when someone authorized this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    created_date: datetime | None = Field(default=None, alias="createdDate", description="Date and time when someone created this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    feature_usages: list[CloudProviderAccessFeatureUsage] | None = Field(default=None, alias="featureUsages", description="List that contains application features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role.")
    iam_assumed_role_arn: str | None = Field(default=None, alias="iamAssumedRoleArn", description="Amazon Resource Name (ARN) that identifies the Amazon Web Services (AWS) Identity and Access Management (IAM) role that MongoDB Cloud assumes when it accesses resources in your AWS account.")
    role_id: str | None = Field(default=None, alias="roleId", description="Unique 24-hexadecimal digit string that identifies the role.")
