"""Generated model for AWSAccountDetails. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AWSAccountDetails(BaseModel):
    """Generated model for AWSAccountDetails."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws_account_id: str | None = Field(default=None, alias="awsAccountId", description="The AWS Account ID.")
    cidr_block: str | None = Field(default=None, alias="cidrBlock", description="The VPC CIDR Block.")
    cloud_provider: str | None = Field(default=None, alias="cloudProvider", description="Cloud provider.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    vpc_id: str | None = Field(default=None, alias="vpcId", description="The VPC ID.")
