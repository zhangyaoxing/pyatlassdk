"""Generated model for FederatedUser. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class FederatedUser(BaseModel):
    """MongoDB Cloud user linked to this federated authentication."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    email_address: str = Field(alias="emailAddress", description="Email address of the MongoDB Cloud user linked to the federated organization.")
    federation_settings_id: str = Field(alias="federationSettingsId", description="Unique 24-hexadecimal digit string that identifies the federation to which this MongoDB Cloud user belongs.")
    first_name: str = Field(alias="firstName", description="First or given name that belongs to the MongoDB Cloud user.")
    last_name: str = Field(alias="lastName", description="Last name, family name, or surname that belongs to the MongoDB Cloud user.")
    user_id: str | None = Field(default=None, alias="userId", description="Unique 24-hexadecimal digit string that identifies this user.")
