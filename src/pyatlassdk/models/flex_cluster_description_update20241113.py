"""Generated model for FlexClusterDescriptionUpdate20241113. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link
from pyatlassdk.models.resource_tag import ResourceTag

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FlexClusterDescriptionUpdate20241113(BaseModel):
    """Settings that you can specify when you update a flex cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    database_edition: Annotated[Literal["CORE", "INFINITE"], BeforeValidator(upper_case)] | None = Field(default=None, alias="databaseEdition", description="Available in Public Preview: Optional field that indicates whether your tenant cluster will be upgraded to Atlas INFINITE or CORE.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    tags: list[ResourceTag] | None = Field(default=None, description="List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the instance.")
    termination_protection_enabled: bool | None = Field(default=None, alias="terminationProtectionEnabled", description="Flag that indicates whether termination protection is enabled on the cluster. If set to `true`, MongoDB Cloud won't delete the cluster. If set to `false`, MongoDB Cloud will delete the cluster.")
