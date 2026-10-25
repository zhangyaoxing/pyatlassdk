"""Generated model for DBRoleToExecute. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DBRoleToExecute(BaseModel):
    """Name of a built-in or custom DB Role to connect to a MongoDB Cloud Cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    role: str | None = Field(default=None, description="The name of the role to use. Can be a built in role or a custom role.")
    type: Annotated[Literal["BUILT_IN", "CUSTOM"], BeforeValidator(upper_case)] | None = Field(default=None, description="Type of the DB role. Can be either Built In or Custom.")
