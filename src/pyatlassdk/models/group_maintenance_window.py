"""Generated model for GroupMaintenanceWindow. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.protected_hours import ProtectedHours

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GroupMaintenanceWindow(BaseModel):
    """Generated model for GroupMaintenanceWindow."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_defer_once_enabled: bool | None = Field(default=None, alias="autoDeferOnceEnabled", description="Flag that indicates whether MongoDB Cloud should defer all maintenance windows for one week after you enable them. This setting controls the same underlying auto-deferral feature as the `/maintenanceWindow/autoDefer` endpoint. Use either this field (to set a specific value) or that endpoint (to toggle the current value). For most use cases, this field in the PATCH request is preferred because it allows setting an explicit value rather than toggling.")
    day_of_week: int | None = Field(default=None, alias="dayOfWeek", description="One-based integer that represents the day of the week, in the project's configured time zone (see `timeZoneId`), that the maintenance window starts.\n\n- `1`: Sunday.\n- `2`: Monday.\n- `3`: Tuesday.\n- `4`: Wednesday.\n- `5`: Thursday.\n- `6`: Friday.\n- `7`: Saturday.")
    effective_wave_assignment: int | None = Field(default=None, alias="effectiveWaveAssignment", description="Maintenance wave that Atlas uses when scheduling maintenance for this project. This read-only value can differ from `waveAssignment` in two scenarios: (1) when the organization's `effectiveWaveAssignmentMode` is `ENV_TAG_MAPPING`, the effective wave is derived from environment tags regardless of any explicit assignment; (2) when cross-organization maintenance sequencing is active and this project's organization is a linked non-paying organization, the effective wave reflects the paying organization's mode.")
    hour_of_day: int | None = Field(default=None, alias="hourOfDay", description="Zero-based integer that represents the hour of the day, in the project's configured time zone (see `timeZoneId`), that the maintenance window starts according to a 24-hour clock. Use `0` for midnight and `12` for noon. If you haven't changed your project's time zone, this defaults to UTC.")
    number_of_deferrals: int | None = Field(default=None, alias="numberOfDeferrals", description="Number of times the current maintenance event for this project has been deferred.")
    protected_hours: ProtectedHours | None = Field(default=None, alias="protectedHours")
    start_asap: bool | None = Field(default=None, alias="startASAP", description="Flag that indicates whether MongoDB Cloud starts the maintenance window immediately upon receiving this request. To start the maintenance window immediately for your project, MongoDB Cloud must have maintenance scheduled and you must set a maintenance window. This flag resets to `false` after MongoDB Cloud completes maintenance.")
    time_zone_id: str | None = Field(default=None, alias="timeZoneId", description="Identifier for the current time zone of the maintenance window. This can only be updated via the Project Settings UI.")
    wave_assignment: int | None = Field(default=None, alias="waveAssignment", description="Maintenance wave explicitly assigned to this project. Always returned in GET responses when a value has been set, regardless of the organization's `effectiveWaveAssignmentMode`. When the mode is `ENV_TAG_MAPPING`, this stored assignment is preserved but not used for scheduling \u2014 the effective wave is derived from environment tags instead. Not editable when the mode is `ENV_TAG_MAPPING`. Switching back to `MANUAL` restores this value as the effective wave. Must be between 1 and 3, inclusive. Pass `null` to clear an explicit assignment.")
