"""Generated model for AdaptiveSettingsOverrides. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class AdaptiveSettingsOverrides(BaseModel):
    """Map of customer-specified overrides for Adaptive Settings, applied on a best-effort basis. Each supported entry that you specify in this object takes precedence over the corresponding Atlas-managed default. For example, if a setting is enabled by default, you can add an override to disable it for your cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    pass
