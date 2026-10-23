"""Generated model for DiskBackupSnapshotAWSExportBucketResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupSnapshotAWSExportBucketResponse(BaseModel):
    """Generated model for DiskBackupSnapshotAWSExportBucketResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(alias="_id", description="Unique 24-hexadecimal character string that identifies the Export Bucket.")
    bucket_name: str = Field(alias="bucketName", description="The name of the AWS S3 Bucket, Azure Storage Container, or Google Cloud Storage Bucket that Snapshots are exported to.")
    cloud_provider: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="cloudProvider", description="Human-readable label that identifies the cloud provider.")
    iam_role_id: str = Field(alias="iamRoleId", description="Unique 24-hexadecimal character string that identifies the Unified AWS Access role ID that MongoDB Cloud uses to access the AWS S3 bucket.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    region: str | None = Field(default=None, description="AWS region for the export bucket. This is set by Atlas and is never user-supplied.")
    require_private_networking: bool | None = Field(default=None, alias="requirePrivateNetworking", description="Indicates whether to use private link. User supplied.")
