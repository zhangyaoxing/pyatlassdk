"""Generated model for OrganizationMaintenanceSettingsUpdateRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrganizationMaintenanceSettingsUpdateRequest(BaseModel):
    """Generated model for OrganizationMaintenanceSettingsUpdateRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    wave_assignment_mode: Annotated[Literal["MANUAL", "ENV_TAG_MAPPING"], BeforeValidator(upper_case)] | None = Field(default=None, alias="waveAssignmentMode", description="Mode configured for this organization that determines how maintenance waves are assigned to projects. Possible values are `MANUAL` and `ENV_TAG_MAPPING`. Defaults to `MANUAL` when unset. Set the organization to `ENV_TAG_MAPPING` mode to have Atlas derive the maintenance wave from each project's environment tag. The tag key must be `environment`. The tag value determines the wave: `development` or `test` maps to Wave 1, `staging` maps to Wave 2, and `production` maps to Wave 3. Only this field can be updated; Atlas derives read-only `effectiveWaveAssignmentMode` on GET responses and uses that value for scheduling when it differs from `waveAssignmentMode`. Omit this field to leave the current value unchanged. Specify null to reset to the default value (`MANUAL`).")
