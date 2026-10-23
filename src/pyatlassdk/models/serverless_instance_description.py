"""Generated model for ServerlessInstanceDescription. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from datetime import datetime
from pyatlassdk._enums import upper_case
from pyatlassdk.models.cluster_serverless_backup_options import ClusterServerlessBackupOptions
from pyatlassdk.models.link import Link
from pyatlassdk.models.resource_tag import ResourceTag
from pyatlassdk.models.serverless_instance_description_connection_strings import ServerlessInstanceDescriptionConnectionStrings
from pyatlassdk.models.serverless_provider_settings import ServerlessProviderSettings

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ServerlessInstanceDescription(BaseModel):
    """Group of settings that configure a MongoDB serverless instance."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    connection_strings: ServerlessInstanceDescriptionConnectionStrings | None = Field(default=None, alias="connectionStrings")
    create_date: datetime | None = Field(default=None, alias="createDate", description="Date and time when MongoDB Cloud created this serverless instance. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal character string that identifies the project.")
    id: str | None = Field(default=None, description="Unique 24-hexadecimal digit string that identifies the serverless instance.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    mongo_db_version: str | None = Field(default=None, alias="mongoDBVersion", description="Version of MongoDB that the serverless instance runs.")
    name: str | None = Field(default=None, description="Human-readable label that identifies the serverless instance.")
    provider_settings: ServerlessProviderSettings = Field(alias="providerSettings")
    serverless_backup_options: ClusterServerlessBackupOptions | None = Field(default=None, alias="serverlessBackupOptions")
    state_name: Annotated[Literal["IDLE", "CREATING", "UPDATING", "DELETING", "REPAIRING"], BeforeValidator(upper_case)] | None = Field(default=None, alias="stateName", description="Human-readable label that indicates any current activity being taken on this cluster by the Atlas control plane. With the exception of CREATING and DELETING states, clusters should always be available and have a Primary node even when in states indicating ongoing activity.\n\n - `IDLE`: Atlas is making no changes to this cluster and all changes requested via the UI or API can be assumed to have been applied.\n - `CREATING`: A cluster being provisioned for the very first time returns state CREATING until it is ready for connections. Ensure IP Access List and DB Users are configured before attempting to connect.\n - `UPDATING`: A change requested via the UI, API, AutoScaling, or other scheduled activity is taking place.\n - `DELETING`: The cluster is in the process of deletion and will soon be deleted.\n - `REPAIRING`: One or more nodes in the cluster are being returned to service by the Atlas control plane. Other nodes should continue to provide service as normal.")
    tags: list[ResourceTag] | None = Field(default=None, description="List that contains key-value pairs between 1 to 255 characters in length for tagging and categorizing the serverless instance.")
    termination_protection_enabled: bool | None = Field(default=None, alias="terminationProtectionEnabled", description="Flag that indicates whether termination protection is enabled on the serverless instance. If set to `true`, MongoDB Cloud won't delete the serverless instance. If set to `false`, MongoDB Cloud will delete the serverless instance.")
