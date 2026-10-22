"""Generated model for ConfluentUserInfoAuthentication. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class ConfluentUserInfoAuthentication(BaseModel):
    """Authentication details for type `USER_INFO` with username and password for Confluent Schema Registry."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Literal["USER_INFO", "SASL_INHERIT"] = Field(description="Authentication type discriminator. Specifies the authentication mechanism for Confluent Schema Registry.")
    password: str = Field(description="Password or Private Key for authentication.")
    username: str = Field(description="Username or Public Key for authentication.")
