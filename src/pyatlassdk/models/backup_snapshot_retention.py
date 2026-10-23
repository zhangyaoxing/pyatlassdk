"""Generated model for BackupSnapshotRetention. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class BackupSnapshotRetention(BaseModel):
    """Generated model for BackupSnapshotRetention."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    retention_unit: Annotated[Literal["DAYS", "WEEKS", "MONTHS", "YEARS"], BeforeValidator(upper_case)] = Field(alias="retentionUnit", description="Quantity of time in which MongoDB Cloud measures snapshot retention.")
    retention_value: int = Field(alias="retentionValue", description="Number that indicates the amount of days, weeks, months, or years that MongoDB Cloud retains the snapshot. For less frequent policy items, MongoDB Cloud requires that you specify a value greater than or equal to the value specified for more frequent policy items. If the hourly policy item specifies a retention of two days, specify two days or greater for the retention of the weekly policy item.")
