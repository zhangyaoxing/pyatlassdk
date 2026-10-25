"""Generated model for DiskBackupCopySetting20240805. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.disk_backup_copy_policy_item import DiskBackupCopyPolicyItem

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DiskBackupCopySetting20240805(BaseModel):
    """Copy setting item in the desired backup policy."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cloud_provider: Annotated[Literal["AWS", "AZURE", "GCP"], BeforeValidator(upper_case)] | None = Field(default=None, alias="cloudProvider", description="Human-readable label that identifies the cloud provider that stores the snapshot copy.")
    copy_policy_items: list[DiskBackupCopyPolicyItem] | None = Field(default=None, alias="copyPolicyItems", description="List that contains a document for each copy policy item. Allowed only when `copyPolicyItemsEnabled` is true. Responses omit this field when `copyPolicyItemsEnabled` is false or omitted.")
    frequencies: list[Annotated[Literal["HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY", "ON_DEMAND"], BeforeValidator(upper_case)]] | None = Field(default=None, description="Deprecated: use `copyPolicyItems`, which defines which snapshots to copy and their retention. Allowed only when `copyPolicyItemsEnabled` is false or omitted. Responses omit this field when `copyPolicyItemsEnabled` is true.")
    last_number_of_snapshots: int | None = Field(default=None, alias="lastNumberOfSnapshots", description="Number of most recent snapshots to copy to the target region. If specified, Atlas copies this number of the most recent snapshots rather than using a frequency-based or policy-based copy schedule. This field is mutually exclusive with `frequencies` and `copyPolicyItems`.")
    region_name: str | None = Field(default=None, alias="regionName", description="Target region to copy snapshots belonging to `zoneId`. Please supply the 'Atlas Region'.")
    should_copy_oplogs: bool | None = Field(default=None, alias="shouldCopyOplogs", description="Flag that indicates whether to copy the oplogs to the target region. You can use the oplogs to perform point-in-time restores.")
    zone_id: str = Field(alias="zoneId", description="Unique 24-hexadecimal digit string that identifies the zone in a cluster. For global clusters, there can be multiple zones to choose from. For sharded clusters and replica set clusters, there is only one zone in the cluster. To find the Zone Id, do a GET request to Return One Cluster from One Project and consult the `replicationSpecs` array.")
