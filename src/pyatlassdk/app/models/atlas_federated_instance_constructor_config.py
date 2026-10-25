"""Generated model for AtlasFederatedInstanceConstructorConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasFederatedInstanceConstructorConfig(BaseModel):
    """Generated model for AtlasFederatedInstanceConstructorConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    data_lake_name: str = Field(alias="dataLakeName", description="The service name used to refer to the Federated database\ninstance within this Atlas app. The name may be at most\n64 characters long and must only contain ASCII letters,\nnumbers, underscores, and hyphens.")
