"""Generated model for NetworkPermissionEntry. Do not edit manually."""

from __future__ import annotations

from datetime import datetime
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class NetworkPermissionEntry(BaseModel):
    """Generated model for NetworkPermissionEntry."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws_security_group: str | None = Field(default=None, alias="awsSecurityGroup", description="Unique string of the Amazon Web Services (AWS) security group that you want to add to the project's IP access list. Your IP access list entry can be one `awsSecurityGroup`, one `cidrBlock`, or one `ipAddress`. You must configure Virtual Private Connection (VPC) peering for your project before you can add an AWS security group to an IP access list. You cannot set AWS security groups as temporary access list entries. Don't set this parameter if you set `cidrBlock` or `ipAddress`.")
    cidr_block: str | None = Field(default=None, alias="cidrBlock", description="Range of IP addresses in Classless Inter-Domain Routing (CIDR) notation that you want to add to the project's IP access list. Your IP access list entry can be one `awsSecurityGroup`, one `cidrBlock`, or one `ipAddress`. Don't set this parameter if you set `awsSecurityGroup` or `ipAddress`.")
    comment: str | None = Field(default=None, description="Remark that explains the purpose or scope of this IP access list entry.")
    delete_after_date: datetime | None = Field(default=None, alias="deleteAfterDate", description="Date and time after which MongoDB Cloud deletes the temporary access list entry. This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. The date must be later than the current date but no later than one week after you submit this request. The resource returns this parameter if you specified an expiration date when creating this IP access list entry.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that contains the IP access list to which you want to add one or more entries.")
    ip_address: str | None = Field(default=None, alias="ipAddress", description="IP address that you want to add to the project's IP access list. Your IP access list entry can be one `awsSecurityGroup`, one `cidrBlock`, or one `ipAddress`. Don't set this parameter if you set `awsSecurityGroup` or `cidrBlock`.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
