"""Generated model for AdaptiveSettingsResponse. Do not edit manually."""

from __future__ import annotations

from typing import Any
from pyatlassdk.models.adaptive_settings_overrides import AdaptiveSettingsOverrides

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdaptiveSettingsResponse(BaseModel):
    """Adaptive Settings for a cluster, including client-provided overrides and the effective settings derived from those overrides and Atlas-managed defaults."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    adaptive_settings_overrides: AdaptiveSettingsOverrides | None = Field(default=None, alias="adaptiveSettingsOverrides")
    effective_adaptive_settings: dict[str, Any] = Field(alias="effectiveAdaptiveSettings", description="The effective state of Adaptive Settings currently applied to your cluster, based on your overrides and Atlas-managed defaults. Atlas-managed defaults can vary by MongoDB version, so the same setting may default differently across clusters running different versions. If you set an override for a setting that your cluster's current MongoDB version doesn't support, the override doesn't take effect and the effective value reflects the Atlas-managed default instead.")
