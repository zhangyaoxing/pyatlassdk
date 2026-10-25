"""Generated model for AtlasClusterServiceConfig. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.read_preferences_tag_set import ReadPreferencesTagSet

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AtlasClusterServiceConfig(BaseModel):
    """Generated model for AtlasClusterServiceConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_name: str = Field(alias="clusterName", description="The cluster name of the data source within. The name may be at\nmost 64 characters long and must only contain ASCII letters, numbers,\nunderscores, and hyphens.")
    read_preference: Literal["primary", "primaryPreferred", "secondary", "secondaryPreferred", "nearest"] = Field(alias="readPreference", description="The [read preference](https://www.mongodb.com/docs/atlas/app-services/mongodb/read-preference/) mode for read requests to the data source.")
    read_preference_tag_sets: list[ReadPreferencesTagSet] | None = Field(default=None, alias="readPreferenceTagSets", description="Target read operations to specific members of a replica set.")
    wire_protocol_enabled: bool = Field(alias="wireProtocolEnabled", description="If true, clients may [connect to the app over the MongoDB Wire Protocol [Deprecated]](https://www.mongodb.com/docs/atlas/app-services/mongodb/wire-protocol/#connect-over-the-wire-protocol).")
