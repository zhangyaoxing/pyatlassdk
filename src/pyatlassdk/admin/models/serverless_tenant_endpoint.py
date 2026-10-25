"""Generated model for ServerlessTenantEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.serverless_aws_tenant_endpoint import ServerlessAWSTenantEndpoint
from pyatlassdk.admin.models.serverless_azure_tenant_endpoint import ServerlessAzureTenantEndpoint

ServerlessTenantEndpoint: TypeAlias = ServerlessAWSTenantEndpoint | ServerlessAzureTenantEndpoint
