"""Generated model for HardwareSpec20240805. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.aws_hardware_spec20240805 import AWSHardwareSpec20240805
from pyatlassdk.models.azure_hardware_spec20240805 import AzureHardwareSpec20240805
from pyatlassdk.models.gcp_hardware_spec20240805 import GCPHardwareSpec20240805
from pyatlassdk.models.tenant_hardware_spec20240805 import TenantHardwareSpec20240805

HardwareSpec20240805: TypeAlias = AWSHardwareSpec20240805 | AzureHardwareSpec20240805 | GCPHardwareSpec20240805 | TenantHardwareSpec20240805
