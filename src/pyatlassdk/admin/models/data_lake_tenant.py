"""Generated model for DataLakeTenant. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.data_lake_cloud_provider_config import DataLakeCloudProviderConfig
from pyatlassdk.admin.models.data_lake_data_process_region import DataLakeDataProcessRegion
from pyatlassdk.admin.models.data_lake_storage import DataLakeStorage
from pyatlassdk.admin.models.private_endpoint_hostname import PrivateEndpointHostname

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeTenant(BaseModel):
    """Generated model for DataLakeTenant."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider_config: DataLakeCloudProviderConfig | None = Field(default=None, alias="cloudProviderConfig")
    data_process_region: DataLakeDataProcessRegion | None = Field(default=None, alias="dataProcessRegion")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    hostnames: list[str] | None = Field(default=None, description="List that contains the hostnames assigned to the Federated Database Instance.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the Federated Database Instance.")
    private_endpoint_hostnames: list[PrivateEndpointHostname] | None = Field(default=None, alias="privateEndpointHostnames", description="List that contains the sets of private endpoints and hostnames.")
    state: Annotated[Literal["UNVERIFIED", "ACTIVE", "DELETED"], BeforeValidator(upper_case)] | None = Field(default=None, description="Label that indicates the status of the Federated Database Instance.")
    storage: DataLakeStorage | None = None
