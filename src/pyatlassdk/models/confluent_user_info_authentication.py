"""Generated model for ConfluentUserInfoAuthentication. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ConfluentUserInfoAuthentication(BaseModel):
    """Authentication details for type `USER_INFO` with username and password for Confluent Schema Registry."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Annotated[Literal["USER_INFO", "SASL_INHERIT"], BeforeValidator(upper_case)] = Field(description="Authentication type discriminator. Specifies the authentication mechanism for Confluent Schema Registry.")
    password: str = Field(description="Password or Private Key for authentication.")
    username: str = Field(description="Username or Public Key for authentication.")
