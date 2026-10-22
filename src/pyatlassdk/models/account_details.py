"""Generated model for AccountDetails. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.aws_account_details import AWSAccountDetails
from pyatlassdk.models.azure_account_details import AzureAccountDetails
from pyatlassdk.models.gcp_account_details import GCPAccountDetails

AccountDetails: TypeAlias = AWSAccountDetails | AzureAccountDetails | GCPAccountDetails
