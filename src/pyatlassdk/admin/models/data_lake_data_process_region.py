"""Generated model for DataLakeDataProcessRegion. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.base_atlas_data_lake_region import BaseAtlasDataLakeRegion

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataLakeDataProcessRegion(BaseModel):
    """Information about the cloud provider region to which the Federated Database Instance routes client connections."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] = Field(alias="cloudProvider", description="Name of the cloud service that hosts the Federated Database Instance's infrastructure.")
    region: BaseAtlasDataLakeRegion
