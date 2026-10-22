"""Generated model for MdbAvailableVersion. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.base_cloud_provider_instance_size import BaseCloudProviderInstanceSize
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class MdbAvailableVersion(BaseModel):
    """Generated model for MdbAvailableVersion."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Literal["AWS", "AZURE", "GCP", "TENANT"] | None = Field(default=None, alias="cloudProvider", description="Cloud service provider on which MongoDB Cloud provisions the hosts. Set dedicated clusters to `AWS`, `GCP`, `AZURE` or `TENANT`.")
    default_status: Literal["DEFAULT", "NOT_DEFAULT"] | None = Field(default=None, alias="defaultStatus", description="Whether the version is the current default for the Instance Size and Cloud Provider.")
    instance_size: BaseCloudProviderInstanceSize | None = Field(default=None, alias="instanceSize")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    version: str | None = Field(default=None, description="The MongoDB Major Version in question.")
