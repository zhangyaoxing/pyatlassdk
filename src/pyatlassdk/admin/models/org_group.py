"""Generated model for OrgGroup. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.cloud_cluster import CloudCluster

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgGroup(BaseModel):
    """Generated model for OrgGroup."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    clusters: list[CloudCluster] | None = Field(default=None, description="Settings that describe the clusters in each project that the API key is authorized to view.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    group_name: str | None = Field(default=None, alias="groupName", description="Human-readable label that identifies the project.")
    org_id: str | None = Field(default=None, alias="orgId", description="Unique 24-hexadecimal character string that identifies the organization that contains the project.")
    org_name: str | None = Field(default=None, alias="orgName", description="Human-readable label that identifies the organization that contains the project.")
    plan_type: str | None = Field(default=None, alias="planType", description="Human-readable label that indicates the plan type.")
    tags: list[str] | None = Field(default=None, description="List of human-readable labels that categorize the specified project. MongoDB Cloud returns an empty array.")
