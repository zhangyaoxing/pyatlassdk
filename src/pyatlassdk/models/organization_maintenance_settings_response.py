"""Generated model for OrganizationMaintenanceSettingsResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrganizationMaintenanceSettingsResponse(BaseModel):
    """Maintenance configuration settings for an organization."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    effective_wave_assignment_mode: Annotated[Literal["MANUAL", "ENV_TAG_MAPPING"], BeforeValidator(upper_case)] | None = Field(default=None, alias="effectiveWaveAssignmentMode", description="Wave assignment mode that Atlas uses when scheduling maintenance for projects in this organization. This read-only field takes precedence over `waveAssignmentMode` for scheduling. It matches `waveAssignmentMode` except when cross-organization maintenance sequencing is enabled and this organization is a linked non-paying organization, in which case it reflects the paying organization's `waveAssignmentMode`. Possible values are `MANUAL` and `ENV_TAG_MAPPING`. Defaults to `MANUAL` when no mode is configured. Omitted from GET responses when maintenance sequencing is disabled for this organization.")
    wave_assignment_mode: Annotated[Literal["MANUAL", "ENV_TAG_MAPPING"], BeforeValidator(upper_case)] | None = Field(default=None, alias="waveAssignmentMode", description="Mode explicitly configured for this organization that determines how maintenance waves are assigned to projects. Possible values are `MANUAL` and `ENV_TAG_MAPPING`. Omitted from the response when no explicit preference has been set; in that case `effectiveWaveAssignmentMode` reflects the value the system uses (`MANUAL` by default). Atlas uses read-only `effectiveWaveAssignmentMode` (not this field) for scheduling. In a cross-organization billing hierarchy, a linked non-paying organization cannot update its `effectiveWaveAssignmentMode` field, which inherits from the paying organization's `waveAssignmentMode`. In this case, a linked non-paying organization's `effectiveWaveAssignmentMode` and `waveAssignmentMode` might differ.")
