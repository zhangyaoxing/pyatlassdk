"""Generated model for EARPrivateEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.awskmsear_private_endpoint import AWSKMSEARPrivateEndpoint
from pyatlassdk.admin.models.azure_key_vault_ear_private_endpoint import AzureKeyVaultEARPrivateEndpoint

EARPrivateEndpoint: TypeAlias = AzureKeyVaultEARPrivateEndpoint | AWSKMSEARPrivateEndpoint
