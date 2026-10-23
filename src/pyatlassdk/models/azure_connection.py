"""Generated model for AzureConnection. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AzureConnection(BaseModel):
    """Azure-specific configuration for the connection."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    region: str | None = Field(default=None, description="Azure region where the storage account is located.")
    service_principal_id: str | None = Field(default=None, alias="servicePrincipalId", description="Unique ID of the Azure Service Principal that has access to the storage account.")
    storage_account_name: str | None = Field(default=None, alias="storageAccountName", description="Name of the Azure Storage Account to connect to.")
