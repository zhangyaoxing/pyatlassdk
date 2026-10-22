"""Generated model for BaseAtlasDataLakeRegion. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.api_atlas_data_lake_aws_region_view import ApiAtlasDataLakeAWSRegionView
from pyatlassdk.models.atlas_data_federation_azure_region import AtlasDataFederationAzureRegion
from pyatlassdk.models.atlas_data_federation_gcp_region import AtlasDataFederationGCPRegion

BaseAtlasDataLakeRegion: TypeAlias = ApiAtlasDataLakeAWSRegionView | AtlasDataFederationAzureRegion | AtlasDataFederationGCPRegion
