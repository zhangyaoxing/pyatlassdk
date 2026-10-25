"""Generated model for CreateEndpointRequest. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.create_aws_endpoint_request import CreateAWSEndpointRequest
from pyatlassdk.admin.models.create_azure_endpoint_request import CreateAzureEndpointRequest
from pyatlassdk.admin.models.create_gcp_endpoint_group_request import CreateGCPEndpointGroupRequest

CreateEndpointRequest: TypeAlias = CreateAWSEndpointRequest | CreateAzureEndpointRequest | CreateGCPEndpointGroupRequest
