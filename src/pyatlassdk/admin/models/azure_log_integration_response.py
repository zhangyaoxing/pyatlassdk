"""Generated model for AzureLogIntegrationResponse. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AzureLogIntegrationResponse(BaseModel):
    """Details to integrate Azure Blob Storage log export with one Atlas project."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str = Field(description="Unique 24-character hexadecimal digit string that identifies the log integration configuration.")
    log_types: list[Annotated[Literal["MONGOD", "MONGOS", "MONGOD_AUDIT", "MONGOS_AUDIT", "EVENTS"], BeforeValidator(upper_case)]] = Field(alias="logTypes", description="Array of log types exported by this integration.")
    type: Annotated[Literal["AZURE_LOG_EXPORT"], BeforeValidator(upper_case)] = Field(description="Human-readable label that identifies the service to which you want to integrate with Atlas. The value must match the log integration type. This value cannot be modified after the integration is created.")
    prefix_path: str = Field(alias="prefixPath", description="Path prefix where the log files will be stored. Atlas will add further sub-directories based on the log type.")
    role_id: str = Field(alias="roleId", description="Unique 24-character hexadecimal string that identifies the Atlas Cloud Provider Access role.")
    storage_account_name: str = Field(alias="storageAccountName", description="Storage account name where logs will be stored.")
    storage_container_name: str = Field(alias="storageContainerName", description="Storage container name for log files.")
