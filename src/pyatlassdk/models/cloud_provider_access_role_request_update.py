"""Generated model for CloudProviderAccessRoleRequestUpdate. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CloudProviderAccessRoleRequestUpdate(BaseModel):
    """Cloud provider access role."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    provider_name: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="providerName", description="Human-readable label that identifies the cloud provider of the role.")
