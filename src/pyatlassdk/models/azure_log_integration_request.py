"""Generated model for AzureLogIntegrationRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class AzureLogIntegrationRequest(BaseModel):
    """Request schema for creating or updating an Azure Blob Storage log export integration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    log_types: list[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Literal["AZURE_LOG_EXPORT"] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    prefix_path: str = Field(alias="prefixPath", description="Path prefix where the log files will be stored. Atlas will add further sub-directories based on the log type.")
    role_id: str = Field(alias="roleId", description="Unique 24-character hexadecimal string that identifies the Atlas Cloud Provider Access role.")
    storage_account_name: str = Field(alias="storageAccountName", description="Storage account name where logs will be stored.")
    storage_container_name: str = Field(alias="storageContainerName", description="Storage container name for log files.")
