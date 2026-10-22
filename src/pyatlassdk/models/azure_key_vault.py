"""Generated model for AzureKeyVault. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AzureKeyVault(BaseModel):
    """Details that define the configuration of Encryption at Rest using Azure Key Vault (AKV)."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    azure_environment: Literal["AZURE", "AZURE_CHINA", "AZURE_US_GOVERNMENT"] | None = Field(default=None, alias="azureEnvironment", description="Azure environment in which your account credentials reside.")
    client_id: str | None = Field(default=None, alias="clientID", description="Unique 36-hexadecimal character string that identifies an Azure application associated with your Azure Active Directory tenant.")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether someone enabled encryption at rest for the specified  project. To disable encryption at rest using customer key management and remove the configuration details, pass only this parameter with a value of `false`.")
    key_identifier: str | None = Field(default=None, alias="keyIdentifier", description="Web address with a unique key that identifies for your Azure Key Vault.")
    key_vault_name: str | None = Field(default=None, alias="keyVaultName", description="Unique string that identifies the Azure Key Vault that contains your key. This field cannot be modified when you enable and set up private endpoint connections to your Azure Key Vault.")
    require_private_networking: bool | None = Field(default=None, alias="requirePrivateNetworking", description="Enable connection to your Azure Key Vault over private networking.")
    resource_group_name: str | None = Field(default=None, alias="resourceGroupName", description="Name of the Azure resource group that contains your Azure Key Vault. This field cannot be modified when you enable and set up private endpoint connections to your Azure Key Vault.")
    role_id: str | None = Field(default=None, alias="roleId", description="Unique 24-hexadecimal digit string that identifies the Azure Service Principal that MongoDB Cloud uses to access the Azure Key Vault.")
    secret: str | None = Field(default=None, description="Private data that you need secured and that belongs to the specified Azure Key Vault (AKV) tenant (`azureKeyVault.tenantID`). This data can include any type of sensitive data such as passwords, database connection strings, API keys, and the like. AKV stores this information as encrypted binary data.")
    subscription_id: str | None = Field(default=None, alias="subscriptionID", description="Unique 36-hexadecimal character string that identifies your Azure subscription. This field cannot be modified when you enable and set up private endpoint connections to your Azure Key Vault.")
    tenant_id: str | None = Field(default=None, alias="tenantID", description="Unique 36-hexadecimal character string that identifies the Azure Active Directory tenant within your Azure subscription.")
    valid: bool | None = Field(default=None, description="Flag that indicates whether the Azure encryption key can encrypt and decrypt data.")
