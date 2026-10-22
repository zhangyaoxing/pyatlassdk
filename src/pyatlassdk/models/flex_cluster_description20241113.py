"""Generated model for FlexClusterDescription20241113. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from datetime import datetime
from pyatlassdk.models.flex_backup_settings20241113 import FlexBackupSettings20241113
from pyatlassdk.models.flex_connection_strings20241113 import FlexConnectionStrings20241113
from pyatlassdk.models.flex_provider_settings20241113 import FlexProviderSettings20241113
from pyatlassdk.models.link import Link
from pyatlassdk.models.resource_tag import ResourceTag

from pydantic import BaseModel, ConfigDict, Field

class FlexClusterDescription20241113(BaseModel):
    """Group of settings that configure a MongoDB Flex cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    backup_settings: FlexBackupSettings20241113 | None = Field(default=None, alias="backupSettings")
    cluster_type: Literal["REPLICASET"] | None = Field(default=None, alias="clusterType", description="Flex cluster topology.")
    connection_strings: FlexConnectionStrings20241113 | None = Field(default=None, alias="connectionStrings")
    create_date: datetime | None = Field(default=None, alias="createDate", description="Date and time when MongoDB Cloud created this instance. This parameter expresses its value in ISO 8601 format in UTC.")
    database_edition: Literal["CORE", "INFINITE"] | None = Field(default=None, alias="databaseEdition", description="Available in Public Preview: Optional field that indicates whether your tenant cluster will be upgraded to Atlas INFINITE or CORE.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the instance.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    mongo_db_version: str | None = Field(default=None, alias="mongoDBVersion", description="Version of MongoDB that the instance runs.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the instance.")
    provider_settings: FlexProviderSettings20241113 = Field(alias="providerSettings")
    state_name: Literal["IDLE", "CREATING", "UPDATING", "DELETING", "REPAIRING"] | None = Field(default=None, alias="stateName", description="Human-readable label that indicates any current activity being taken on this cluster by the Atlas control plane. With the exception of CREATING and DELETING states, clusters should always be available and have a Primary node even when in states indicating ongoing activity.\n\n - `IDLE`: Atlas is making no changes to this cluster and all changes requested via the UI or API can be assumed to have been applied.\n - `CREATING`: A cluster being provisioned for the very first time returns state CREATING until it is ready for connections. Ensure IP Access List and DB Users are configured before attempting to connect.\n - `UPDATING`: A change requested via the UI, API, AutoScaling, or other scheduled activity is taking place.\n - `DELETING`: The cluster is in the process of deletion and will soon be deleted.\n - `REPAIRING`: One or more nodes in the cluster are being returned to service by the Atlas control plane. Other nodes should continue to provide service as normal.")
    tags: list[ResourceTag] | None = Field(default=None, description="List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the instance.")
    termination_protection_enabled: bool | None = Field(default=None, alias="terminationProtectionEnabled", description="Flag that indicates whether termination protection is enabled on the cluster. If set to `true`, MongoDB Cloud won't delete the cluster. If set to `false`, MongoDB Cloud will delete the cluster.")
    version_release_system: Literal["LTS"] | None = Field(default=None, alias="versionReleaseSystem", description="Method by which the cluster maintains the MongoDB versions.")
