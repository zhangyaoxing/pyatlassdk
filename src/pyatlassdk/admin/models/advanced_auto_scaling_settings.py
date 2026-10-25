"""Generated model for AdvancedAutoScalingSettings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.advanced_auto_scaling_settings_storage_config import AdvancedAutoScalingSettingsStorageConfig
from pyatlassdk.admin.models.advanced_compute_auto_scaling import AdvancedComputeAutoScaling
from pyatlassdk.admin.models.disk_gb_auto_scaling import DiskGBAutoScaling

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdvancedAutoScalingSettings(BaseModel):
    """Options that determine how this cluster handles resource scaling."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    compute: AdvancedComputeAutoScaling | None = None
    disk_gb: DiskGBAutoScaling | None = Field(default=None, alias="diskGB")
    storage_config: AdvancedAutoScalingSettingsStorageConfig | None = Field(default=None, alias="storageConfig", description="Available in Public Preview: Settings that determine the per-shard data-size limit for this cluster. Applies only to Atlas INFINITE clusters. MongoDB Cloud accepts these settings only on `autoScaling` and rejects them on `analyticsAutoScaling`, including when you send them as `null`. In a request that includes `replicationSpecs`, omitting `storageConfig` or sending it as `null` or `{}` clears the limit. Omitting `replicationSpecs` preserves it.")
