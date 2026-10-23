"""Generated model for OrgFederationSettings. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class OrgFederationSettings(BaseModel):
    """Details that define how to connect one MongoDB Cloud organization to one federated authentication service."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    federated_domains: list[str] = Field(alias="federatedDomains", description="List of domains associated with the organization's identity provider.")
    has_role_mappings: bool | None = Field(default=None, alias="hasRoleMappings", description="Flag that indicates whether this organization has role mappings configured.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies this federation.")
    identity_provider_id: str | None = Field(default=None, alias="identityProviderId", description="Legacy 20-hexadecimal digit string that identifies the identity provider connected to this organization.")
    identity_provider_status: Annotated[Literal["ACTIVE", "INACTIVE"], BeforeValidator(upper_case)] | None = Field(default=None, alias="identityProviderStatus", description="String enum that indicates whether the identity provider is active.")
