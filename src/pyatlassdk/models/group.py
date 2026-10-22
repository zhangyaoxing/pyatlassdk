"""Generated model for Group. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.link import Link
from pyatlassdk.models.resource_tag import ResourceTag

from pydantic import BaseModel, ConfigDict, Field

class Group(BaseModel):
    """Generated model for Group."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_count: int = Field(alias="clusterCount", description="Quantity of MongoDB Cloud clusters deployed in this project.")
    created: datetime = Field(description="Date and time when MongoDB Cloud created this project. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud project.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: str = Field(description="Human-readable label that identifies the project included in the MongoDB Cloud organization.")
    org_id: str = Field(alias="orgId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud organization to which the project belongs.")
    region_usage_restrictions: Literal["COMMERCIAL_FEDRAMP_REGIONS_ONLY", "GOV_REGIONS_ONLY"] | None = Field(default=None, alias="regionUsageRestrictions", description="Applies to Atlas for Government only.\n\nIn Commercial Atlas, this field will be rejected in requests and missing in responses.\n\nThis field sets restrictions on available regions in the project.\n\n`COMMERCIAL_FEDRAMP_REGIONS_ONLY`: Only allows deployments in FedRAMP Moderate regions.\n\n`GOV_REGIONS_ONLY`: Only allows deployments in GovCloud regions.")
    tags: list[ResourceTag] | None = Field(default=None, description="List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the project.")
    with_default_alerts_settings: bool | None = Field(default=None, alias="withDefaultAlertsSettings", description="Flag that indicates whether to create the project with default alert settings.")
