"""Generated model for LogIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.azure_log_integration_request import AzureLogIntegrationRequest
from pyatlassdk.admin.models.datadog_log_integration_request import DatadogLogIntegrationRequest
from pyatlassdk.admin.models.gcs_log_integration_request import GcsLogIntegrationRequest
from pyatlassdk.admin.models.otel_log_integration_request import OtelLogIntegrationRequest
from pyatlassdk.admin.models.s3_log_integration_request import S3LogIntegrationRequest
from pyatlassdk.admin.models.splunk_log_integration_request import SplunkLogIntegrationRequest

LogIntegrationRequest: TypeAlias = S3LogIntegrationRequest | DatadogLogIntegrationRequest | GcsLogIntegrationRequest | OtelLogIntegrationRequest | SplunkLogIntegrationRequest | AzureLogIntegrationRequest
