"""Generated model for StreamsKafkaSecurity. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsKafkaSecurity(BaseModel):
    """Properties for the secure transport connection to Kafka. For SSL, this can include the trusted certificate to use."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    broker_public_certificate: str | None = Field(default=None, alias="brokerPublicCertificate", description="A trusted, public x509 certificate for connecting to Kafka over SSL.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    protocol: str | None = Field(default=None, description="Describes the transport type. Can be either `SASL_PLAINTEXT`, `SASL_SSL`, or `SSL`.")
