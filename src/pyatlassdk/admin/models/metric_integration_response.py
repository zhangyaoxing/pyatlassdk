"""Generated model for MetricIntegrationResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.o_auth_config_response import OAuthConfigResponse
from pyatlassdk.admin.models.redacted_header import RedactedHeader

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class MetricIntegrationResponse(BaseModel):
    """Response schema for metric integration operations."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aggregation_temporality: Annotated[Literal["DELTA", "CUMULATIVE"], BeforeValidator(upper_case)] = Field(alias="aggregationTemporality", description="The temporality to send to the metric integration.")
    auth_type: Annotated[Literal["HEADER", "OAUTH2"], BeforeValidator(upper_case)] = Field(alias="authType", description="Authentication method the integration uses when exporting metrics to the endpoint.")
    endpoint: str = Field(description="OpenTelemetry collector endpoint URL.")
    headers_redacted: list[RedactedHeader] | None = Field(default=None, alias="headersRedacted", description="HTTP headers for authentication and configuration. Values are redacted and never returned in plaintext.")
    integration_type: Annotated[Literal["OTEL"], BeforeValidator(upper_case)] = Field(alias="integrationType", description="Type of metric integration. Identifies which protocol will be used for the integration.")
    metric_integration_id: str = Field(alias="metricIntegrationId", description="Unique identifier of the metric integration configuration.")
    metric_selection: list[Annotated[Literal["ATLAS_STREAM_PROCESSING", "MONGODB_METRICS", "HARDWARE_METRICS"], BeforeValidator(upper_case)]] = Field(alias="metricSelection", description="Array of metric categories to export. Determines which types of metrics are sent to the integration.")
    oauth: OAuthConfigResponse | None = None
    provider_type: Annotated[Literal["CUSTOM", "DATADOG", "DYNATRACE", "NEW_RELIC"], BeforeValidator(upper_case)] = Field(alias="providerType", description="The provider type for the metric integration. Identifies the third-party service provider.")
