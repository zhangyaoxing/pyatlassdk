"""Generated model for StreamsAWSConnectionConfig. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsAWSConnectionConfig(BaseModel):
    """AWS configurations for AWS-based connection types."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    role_arn: str | None = Field(default=None, alias="roleArn", description="Amazon Resource Name (ARN) that identifies the Amazon Web Services (AWS) Identity and Access Management (IAM) role that MongoDB Cloud assumes when it accesses resources in your AWS account.")
    test_bucket: str | None = Field(default=None, alias="testBucket", description="The name of an S3 bucket used to check authorization of the passed-in IAM role ARN. This field applies only to S3 connections and is ignored for all other connection types and configurations.")
