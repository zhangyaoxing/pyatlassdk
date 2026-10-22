"""Generated model for BaseStreamsRegion. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.api_streams_aws_region_view import ApiStreamsAWSRegionView
from pyatlassdk.models.api_streams_azure_region_view import ApiStreamsAzureRegionView
from pyatlassdk.models.api_streams_gcp_region_view import ApiStreamsGCPRegionView

BaseStreamsRegion: TypeAlias = ApiStreamsAWSRegionView | ApiStreamsAzureRegionView | ApiStreamsGCPRegionView
