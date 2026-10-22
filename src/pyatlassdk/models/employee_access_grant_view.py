"""Generated model for EmployeeAccessGrantView. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class EmployeeAccessGrantView(BaseModel):
    """MongoDB employee granted access level and expiration for a cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    expiration_time: datetime = Field(alias="expirationTime", description="Expiration date for the employee access grant. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    grant_type: Literal["CLUSTER_DATABASE_LOGS", "CLUSTER_INFRASTRUCTURE", "CLUSTER_INFRASTRUCTURE_AND_APP_SERVICES_SYNC_DATA"] = Field(alias="grantType", description="Level of access to grant to MongoDB Employees.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
