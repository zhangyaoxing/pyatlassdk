"""Generated model for AdvancedComputeAutoScaling. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.base_cloud_provider_instance_size import BaseCloudProviderInstanceSize

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AdvancedComputeAutoScaling(BaseModel):
    """Options that determine how this cluster handles CPU scaling."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether instance size reactive auto-scaling is enabled.\n\n- Set to `true` to enable instance size reactive auto-scaling. If enabled, you must specify a value for `replicationSpecs[n].regionConfigs[m].autoScaling.compute.maxInstanceSize`.\n- Set to `false` to disable instance size reactive auto-scaling.")
    max_instance_size: BaseCloudProviderInstanceSize | None = Field(default=None, alias="maxInstanceSize")
    min_instance_size: BaseCloudProviderInstanceSize | None = Field(default=None, alias="minInstanceSize")
    scale_down_enabled: bool | None = Field(default=None, alias="scaleDownEnabled", description="Flag that indicates whether the instance size may scale down via reactive auto-scaling. MongoDB Cloud requires this parameter if `replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled` is `true`. If you enable this option, specify a value for `replicationSpecs[n].regionConfigs[m].autoScaling.compute.minInstanceSize`.")
