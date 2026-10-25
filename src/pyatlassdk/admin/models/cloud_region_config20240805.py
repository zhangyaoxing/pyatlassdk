"""Generated model for CloudRegionConfig20240805. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.aws_region_config20240805 import AWSRegionConfig20240805
from pyatlassdk.admin.models.azure_region_config20240805 import AzureRegionConfig20240805
from pyatlassdk.admin.models.gcp_region_config20240805 import GCPRegionConfig20240805
from pyatlassdk.admin.models.tenant_region_config20240805 import TenantRegionConfig20240805

CloudRegionConfig20240805: TypeAlias = AWSRegionConfig20240805 | AzureRegionConfig20240805 | GCPRegionConfig20240805 | TenantRegionConfig20240805
