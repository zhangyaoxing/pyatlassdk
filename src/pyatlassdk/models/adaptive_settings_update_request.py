"""Generated model for AdaptiveSettingsUpdateRequest. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.adaptive_settings_overrides import AdaptiveSettingsOverrides

from pydantic import BaseModel, ConfigDict, Field

class AdaptiveSettingsUpdateRequest(BaseModel):
    """Adaptive Settings for a cluster, including client-provided overrides and the effective settings derived from those overrides and Atlas-managed defaults."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    adaptive_settings_overrides: AdaptiveSettingsOverrides | None = Field(default=None, alias="adaptiveSettingsOverrides")
