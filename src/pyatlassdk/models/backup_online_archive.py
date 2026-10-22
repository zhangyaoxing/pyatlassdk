"""Generated model for BackupOnlineArchive. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.criteria_view import CriteriaView
from pyatlassdk.models.data_expiration_rule_view import DataExpirationRuleView
from pyatlassdk.models.data_process_region_view import DataProcessRegionView
from pyatlassdk.models.online_archive_schedule import OnlineArchiveSchedule
from pyatlassdk.models.partition_field_view import PartitionFieldView

from pydantic import BaseModel, ConfigDict, Field

class BackupOnlineArchive(BaseModel):
    """Generated model for BackupOnlineArchive."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal digit string that identifies the online archive.")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster that contains the collection for which you want to create an online archive.")
    coll_name: str | None = Field(default=None, alias="collName", description="Human-readable label that identifies the collection for which you created the online archive.")
    collection_type: Literal["TIMESERIES", "STANDARD"] | None = Field(default=None, alias="collectionType", description="Classification of MongoDB database collection that you want to return.\n\nIf you set this parameter to `TIMESERIES`, set `\"criteria.type\" : \"date\"` and `\"criteria.dateFormat\" : \"ISODATE\"`.")
    criteria: CriteriaView | None = None
    data_expiration_rule: DataExpirationRuleView | None = Field(default=None, alias="dataExpirationRule")
    data_process_region: DataProcessRegionView | None = Field(default=None, alias="dataProcessRegion")
    data_set_name: str | None = Field(default=None, alias="dataSetName", description="Human-readable label that identifies the dataset that Atlas generates for this online archive.")
    db_name: str | None = Field(default=None, alias="dbName", description="Human-readable label of the database that contains the collection that contains the online archive.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that contains the specified cluster. The specified cluster contains the collection for which to create the online archive.")
    partition_fields: list[PartitionFieldView] | None = Field(default=None, alias="partitionFields", description="List that contains document parameters to use to logically divide data within a collection. Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify parameters that you frequently query. If you specified `criteria.type`: `DATE` in the Create One Online Archive endpoint, then you can specify up to three parameters by which to query. One of these parameters must be the `DATE` value, which is required in this case. If you specified `criteria.type`: `CUSTOM` in the Create One Online Archive endpoint, then you can specify up to two parameters by which to query. Queries that don't use `criteria.type`: `DATE` or `criteria.type`: `CUSTOM` parameters cause MongoDB to scan a full collection of all archived documents. This takes more time and increases your costs.")
    paused: bool | None = Field(default=None, description="Flag that indicates whether this online archive exists in the paused state. A request to resume fails if the collection has another active online archive. To pause an active online archive or resume a paused online archive, you must include this parameter. To pause an active archive, set this to **true**. To resume a paused archive, set this to **false**.")
    schedule: OnlineArchiveSchedule | None = None
    state: Literal["PENDING", "ACTIVE", "PAUSING", "PAUSED", "DELETED", "ORPHANED"] | None = Field(default=None, description="Phase of the process to create this online archive when you made this request.\n\n| State       | Indication |\n|-------------|------------|\n| `PENDING`   | MongoDB Cloud has queued documents for archive. Archiving hasn't started. |\n| `ARCHIVING` | MongoDB Cloud started archiving documents that meet the archival criteria. |\n| `IDLE`      | MongoDB Cloud waits to start the next archival job. |\n| `PAUSING`   | Someone chose to stop archiving. MongoDB Cloud finishes the running archival job then changes the state to `PAUSED` when that job completes. |\n| `PAUSED`    | MongoDB Cloud has stopped archiving. Archived documents can be queried. The specified archiving operation on the active cluster cannot archive additional documents. You can resume archiving for paused archives at any time. |\n| `ORPHANED`  | Someone has deleted the collection associated with an active or paused archive. MongoDB Cloud doesn't delete the archived data. You must manually delete the online archives associated with the deleted collection. |\n| `DELETED`   | Someone has deleted the archive was deleted. When someone deletes an online archive, MongoDB Cloud removes all associated archived documents from the cloud object storage. |")
