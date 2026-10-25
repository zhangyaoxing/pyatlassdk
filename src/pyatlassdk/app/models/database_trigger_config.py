"""Generated model for DatabaseTriggerConfig. Do not edit manually."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTriggerConfig(BaseModel):
    """Generated model for DatabaseTriggerConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    service_id: str = Field(description="The `_id` value of a linked MongoDB data source that\ncontains the watched collection.\n\nYou can list services with the\n[Get all services endpoint](#operation/adminListServices).\n\nData sources are services whose `type` is \"mongodb-atlas\".\nUse the `_id` value for the data source you want to link to\nthe Trigger.\n")
    database: str | None = Field(default=None, description="The name of a database in the linked data source. If you\nomit this parameter, the Source Type changes to\n\"Deployment.\" However, shared tier infrastructure does not\nsupport deployment changestreams. If you omit the 'database'\nparameter, you receive the 'deployment changestreams are\nnot supported on shared tier clusters' error. Supply the\ndatabase parameter to resolve this error.")
    collection: str | None = Field(default=None, description="The name of a collection in the specified database. The\ntrigger listens to events from this collection. If you omit\nthis parameter, the Source Type changes to \"Database.\"")
    operation_types: list[str] = Field(description="The types of MongoDB change event that the trigger\nlistens for.\n\nValid operation types for all triggers include:\n\n- `\"INSERT\"`\n- `\"UPDATE\"`\n- `\"REPLACE\"`\n- `\"DELETE\"`\n\nAdditional valid operation types for database and\ndeployment triggers include: \n\n- `\"CREATE_COLLECTION\"`\n- `\"MODIFY_COLLECTION\"`\n- `\"RENAME_COLLECTION\"`\n- `\"DROP_COLLECTION\"`\n- `\"SHARD_COLLECTION\"`\n- `\"RESHARD_COLLECTION\"`\n- `\"REFINE_COLLECTION_SHARD_KEY\"`\n\nAdditional valid operation types for deployment triggers\ninclude:\n\n- `\"DROP_DATABASE\"`\n\nFor more information, refer to\n[Trigger Configuration](https://www.mongodb.com/docs/atlas/app-services/triggers/database-triggers/#configuration).")
    match: dict[str, Any] | None = Field(default=None, description="A [$match](https://www.mongodb.com/docs/manual/reference/operator/aggregation/match)\nexpression filters change events. The trigger will only\nfire if the expression evaluates to true for a given\nchange event.")
    project: dict[str, Any] | None = Field(default=None, description="A [$project](https://www.mongodb.com/docs/manual/reference/operator/aggregation/project/) \nexpression returns only the specified fields. You can include \nor exclude specific fields, or include newly-computed fields.")
    full_document: bool | None = Field(default=None, description="If `true`, indicates that `UPDATE` change events should\ninclude the most current\n[majority-committed](https://www.mongodb.com/docs/manual/reference/read-concern-majority/)\nversion of the modified document in the `fullDocument`\nfield.")
    full_document_before_change: bool | None = Field(default=None, description="If true, indicates that `UPDATE` change events should\ninclude a snapshot of the modified document from\nimmediately before the update was applied.\n\nYou must enable [document\npreimages](https://www.mongodb.com/docs/atlas/app-services/mongodb/preimages/)\nfor your cluster to include these snapshots.")
    skip_catchup_events: bool | None = Field(default=None, description="If `true`, enabling the Trigger after it was disabled\nwill not invoke events that occurred while the Trigger\nwas disabled.")
    tolerate_resume_errors: bool | None = Field(default=None, description="If `true`, when this Trigger's resume token\ncannot be found in the cluster's oplog, the Trigger automatically resumes\nprocessing events at the next relevant change stream event.\nAll change stream events from when the Trigger was suspended until the Trigger\nresumes execution do not have the Trigger fire for them.")
    maximum_throughput: bool | None = Field(default=None, description="If `true`, the trigger will use the [maximize \nthroughput](https://www.mongodb.com/docs/atlas/app-services/triggers/database-triggers/#std-label-triggers-maximum-throughput) \noption.")
    unordered: bool | None = Field(default=None, description="If `true`, event ordering is disabled and this Trigger\ncan process events in parallel. If `false`, event\nordering is enabled and the Trigger executes events\nserially.")
