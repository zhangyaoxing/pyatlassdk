"""Generated model for AtlasClusterConstructor. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.atlas_cluster_service_config import AtlasClusterServiceConfig
from pyatlassdk.app.models.default_rule_constructor import DefaultRuleConstructor
from pyatlassdk.app.models.rule_constructor import RuleConstructor

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasClusterConstructor(BaseModel):
    """Generated model for AtlasClusterConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    version: float | None = None
    config: AtlasClusterServiceConfig
    default_rule: DefaultRuleConstructor | None = None
    rules: list[RuleConstructor]
