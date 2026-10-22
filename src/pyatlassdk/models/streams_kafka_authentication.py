"""Generated model for StreamsKafkaAuthentication. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link
from pyatlassdk.models.streams_aws_connection_config import StreamsAWSConnectionConfig

from pydantic import BaseModel, ConfigDict, Field

class StreamsKafkaAuthentication(BaseModel):
    """User credentials required to connect to a Kafka Cluster. Includes the authentication type, as well as the parameters for that authentication mode."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aws: StreamsAWSConnectionConfig | None = None
    client_id: str | None = Field(default=None, alias="clientId", description="OIDC client identifier for authentication to the Kafka cluster.")
    client_secret: str | None = Field(default=None, alias="clientSecret", description="OIDC client secret for authentication to the Kafka cluster.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    mechanism: str | None = Field(default=None, description="Style of authentication. Can be one of PLAIN, SCRAM-256, SCRAM-512, or OAUTHBEARER.")
    method: str | None = Field(default=None, description="SASL OAUTHBEARER authentication method. Currently, only OIDC is supported.")
    password: str | None = Field(default=None, description="Password of the account to connect to the Kafka cluster.")
    sasl_oauthbearer_extensions: str | None = Field(default=None, alias="saslOauthbearerExtensions", description="SASL OAUTHBEARER extensions parameter for additional OAuth2 configuration.")
    scope: str | None = Field(default=None, description="OIDC scope parameter defining the access permissions requested.")
    ssl_certificate: str | None = Field(default=None, alias="sslCertificate", description="SSL certificate for client authentication to Kafka.")
    ssl_key: str | None = Field(default=None, alias="sslKey", description="SSL key for client authentication to Kafka.")
    ssl_key_password: str | None = Field(default=None, alias="sslKeyPassword", description="Password for the SSL key, if it is password protected.")
    token_endpoint_url: str | None = Field(default=None, alias="tokenEndpointUrl", description="OIDC token endpoint URL for obtaining access tokens.")
    username: str | None = Field(default=None, description="Username of the account to connect to the Kafka cluster.")
