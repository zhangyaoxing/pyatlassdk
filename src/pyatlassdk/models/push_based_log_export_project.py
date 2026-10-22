"""Generated model for PushBasedLogExportProject. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class PushBasedLogExportProject(BaseModel):
    """Generated model for PushBasedLogExportProject."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    bucket_name: str | None = Field(default=None, alias="bucketName", description="The name of the bucket to which the agent will send the logs to.")
    create_date: datetime | None = Field(default=None, alias="createDate", description="Date and time that this feature was enabled on. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    iam_role_id: str | None = Field(default=None, alias="iamRoleId", description="ID of the AWS IAM role that will be used to write to the S3 bucket.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    prefix_path: str | None = Field(default=None, alias="prefixPath", description="S3 directory in which vector will write to in order to store the logs. An empty string denotes the root directory.")
    state: Literal["UNCONFIGURED", "INITIATING", "BUCKET_VERIFIED", "BUCKET_VERIFICATION_FAILED", "ASSUME_ROLE_FAILED", "ACTIVE"] | None = Field(default=None, description="Describes whether or not the feature is enabled and what status it is in.")
