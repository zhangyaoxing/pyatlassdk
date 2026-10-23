"""Generated model for ClusterStatus. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ClusterStatus(BaseModel):
    """Generated model for ClusterStatus."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    change_status: Annotated[Literal["PENDING", "APPLIED"], BeforeValidator(upper_case)] | None = Field(default=None, alias="changeStatus", description="State of cluster at the time of this request. Atlas returns **Applied** if it completed adding a user to, or removing a user from, your cluster. Atlas returns **Pending** if it's still making the requested user changes. When status is **Pending**, new users can't log in.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
