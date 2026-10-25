"""Generated model for ConfluentSaslInheritAuthentication. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ConfluentSaslInheritAuthentication(BaseModel):
    """Inherits the authentication configuration from Kafka for the Confluent Schema Registry."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Annotated[Literal["USER_INFO", "SASL_INHERIT"], BeforeValidator(upper_case)] = Field(description="Authentication type discriminator. Specifies the authentication mechanism for Confluent Schema Registry.")
