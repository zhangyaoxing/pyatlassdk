"""Generated model for ConfluentSaslInheritAuthentication. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class ConfluentSaslInheritAuthentication(BaseModel):
    """Inherits the authentication configuration from Kafka for the Confluent Schema Registry."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Literal["USER_INFO", "SASL_INHERIT"] = Field(description="Authentication type discriminator. Specifies the authentication mechanism for Confluent Schema Registry.")
