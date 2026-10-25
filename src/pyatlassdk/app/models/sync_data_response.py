"""Generated model for SyncDataResponse. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.flexible_sync import FlexibleSync

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class SyncDataResponse(BaseModel):
    """Generated model for SyncDataResponse."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_id: str | None = Field(default=None, alias="clusterId", description="The Service ID for the linked cluster.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="The name of the linked cluster")
    cluster_type: Literal["atlas", "serverless"] | None = Field(default=None, alias="clusterType", description="The service type of the linked cluster (\"atlas\" by default)")
    flexible_sync: FlexibleSync | None = None
    group_name: str | None = Field(default=None, alias="groupName", description="The name of the App's Atlas Project.")
    org_name: str | None = Field(default=None, alias="orgName", description="The name of the App's Atlas Organization.")
    read_preference: Literal["primary", "primaryPreferred", "secondary", "secondaryPreferred", "nearest"] | None = Field(default=None, alias="readPreference")
    wire_protocol_enabled: bool | None = Field(default=None, alias="wireProtocolEnabled", description="If true, clients may [connect to the app over the\nMongoDB Wire\nProtocol](https://www.mongodb.com/docs/atlas/app-services/mongodb/wire-protocol/#connect-over-the-wire-protocol).")
