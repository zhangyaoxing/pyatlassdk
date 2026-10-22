"""Generated model for MetricIntegrationResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.o_auth_config_response import OAuthConfigResponse
from pyatlassdk.models.redacted_header import RedactedHeader

from pydantic import BaseModel, ConfigDict, Field

class MetricIntegrationResponse(BaseModel):
    """Response schema for metric integration operations."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    aggregation_temporality: Literal["DELTA", "CUMULATIVE"] = Field(alias="aggregationTemporality", description="The temporality to send to the metric integration.")
    auth_type: Literal["HEADER", "OAUTH2"] = Field(alias="authType", description="Authentication method the integration uses when exporting metrics to the endpoint.")
    endpoint: str = Field(description="OpenTelemetry collector endpoint URL.")
    headers_redacted: list[RedactedHeader] | None = Field(default=None, alias="headersRedacted", description="HTTP headers for authentication and configuration. Values are redacted and never returned in plaintext.")
    integration_type: Literal["OTEL"] = Field(alias="integrationType", description="Type of metric integration. Identifies which protocol will be used for the integration.")
    metric_integration_id: str = Field(alias="metricIntegrationId", description="Unique identifier of the metric integration configuration.")
    metric_selection: list[Literal["ATLAS_STREAM_PROCESSING", "MONGODB_METRICS", "HARDWARE_METRICS"]] = Field(alias="metricSelection", description="Array of metric categories to export. Determines which types of metrics are sent to the integration.")
    oauth: OAuthConfigResponse | None = None
    provider_type: Literal["CUSTOM", "DATADOG", "DYNATRACE", "NEW_RELIC"] = Field(alias="providerType", description="The provider type for the metric integration. Identifies the third-party service provider.")
