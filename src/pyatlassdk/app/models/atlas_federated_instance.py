"""Generated model for AtlasFederatedInstance. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.atlas_federated_instance_config import AtlasFederatedInstanceConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasFederatedInstance(BaseModel):
    """Generated model for AtlasFederatedInstance."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id")
    name: Literal["mongodb-datafederation"]
    type: Literal["datalake"]
    config: AtlasFederatedInstanceConfig
