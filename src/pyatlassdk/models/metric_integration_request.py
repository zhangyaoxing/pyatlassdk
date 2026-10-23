"""Generated model for MetricIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.header import Header
from pyatlassdk.models.o_auth_config_request import OAuthConfigRequest

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MetricIntegrationRequest(BaseModel):
    """Request schema for creating a metric integration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aggregation_temporality: Annotated[Literal["DELTA", "CUMULATIVE"], BeforeValidator(upper_case)] = Field(alias="aggregationTemporality", description="The temporality to send to the metric integration.")
    auth_type: Annotated[Literal["HEADER", "OAUTH2"], BeforeValidator(upper_case)] = Field(alias="authType", description="Authentication method the integration uses when exporting metrics to the endpoint. `HEADER` authenticates with the static HTTP headers provided in the `headers` field, which must be set when this value is used. `OAUTH2` acquires a bearer token from an OAuth 2.0 token endpoint using the `oauth` field.")
    endpoint: str = Field(description="OpenTelemetry collector endpoint URL. Must use HTTPS.")
    headers: list[Header] | None = Field(default=None, description="HTTP headers for authentication and configuration. Total size limit 2KB. Required when `authType` is `HEADER`.")
    integration_type: Annotated[Literal["OTEL"], BeforeValidator(upper_case)] = Field(alias="integrationType", description="Type of metric integration. Identifies which protocol will be used for the integration. This value cannot be modified after the integration is created.")
    metric_selection: list[Annotated[Literal["ATLAS_STREAM_PROCESSING", "MONGODB_METRICS", "HARDWARE_METRICS"], BeforeValidator(upper_case)]] = Field(alias="metricSelection", description="Array of metric categories to export. Determines which types of metrics are sent to the integration.")
    oauth: OAuthConfigRequest | None = None
    provider_type: Annotated[Literal["CUSTOM", "DATADOG", "DYNATRACE", "NEW_RELIC"], BeforeValidator(upper_case)] = Field(alias="providerType", description="The provider type for the metric integration. Identifies the third-party service provider.")
