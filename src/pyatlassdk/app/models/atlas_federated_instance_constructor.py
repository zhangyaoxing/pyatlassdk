"""Generated model for AtlasFederatedInstanceConstructor. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.atlas_federated_instance_constructor_config import AtlasFederatedInstanceConstructorConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasFederatedInstanceConstructor(BaseModel):
    """Generated model for AtlasFederatedInstanceConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: Literal["mongodb-datafederation"]
    type: Literal["datalake"]
    config: AtlasFederatedInstanceConstructorConfig
