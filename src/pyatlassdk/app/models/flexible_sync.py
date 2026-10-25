"""Generated model for FlexibleSync. Do not edit manually."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FlexibleSync(BaseModel):
    """Generated model for FlexibleSync."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    state: str = Field(description="The state of the sync service (`\"enabled\"`, `\"disabled\"`, or empty if Sync is not configured).")
    database_name: str | None = Field(default=None, description="The name of a database in the synced cluster where App Services stores \ndata in Development Mode. App Services automatically generates a schema \nfor each synced type and maps each object type to a collection within the database.")
    queryable_fields_names: list[str] | None = Field(default=None, description="An array of \n[queryable field](https://www.mongodb.com/docs/atlas/app-services/sync/configure/sync-settings/#queryable-fields) \nnames on **any collection**.")
    indexed_queryable_fields_names: list[str] | None = Field(default=None, description="A list of field names to use as the \n[indexed queryable field](https://www.mongodb.com/docs/atlas/app-services/sync/configure/sync-settings/#queryable-fields). \nAlthough this property is an array, Sync currently supports only one indexed \nqueryable field. Therefore, this array may contain at most one element.\n\nThe indexed queryable field must be present in the schema and be the same eligible field type in \nevery collection you sync. The indexed queryable field name must also appear in `queryable_fields_names` \nsince this is a global queryable field.")
    collection_queryable_fields_names: dict[str, dict[str, str]] | None = Field(default=None, description="An array of \n[queryable field](https://www.mongodb.com/docs/atlas/app-services/sync/configure/sync-settings/#queryable-fields) \nnames on the specified collection.")
    permissions: dict[str, Any] | None = Field(default=None, description="**Deprecated**")
    last_disabled: str | None = Field(default=None, description="The last time Sync was disabled, represented by the number of seconds since the UNIX epoch.")
    client_max_offline_days: int | None = Field(default=None, description="The number of days the client can be offline before a client\n[reset](https://www.mongodb.com/docs/atlas/app-services/sync/error-handling/client-resets/)\nis required.")
    is_recovery_mode_disabled: bool | None = Field(default=None, description="Specifies whether the\n[client reset mode](https://www.mongodb.com/docs/atlas/app-services/sync/error-handling/client-resets/#recover-unsynced-changes)\nis disabled. By default, client reset mode is enabled and this value is `false`.")
    asymmetric_tables: list[str] | None = Field(default=None, description="An array of the names of collections that are defined as asymmetric \nwith [Data Ingest](https://www.mongodb.com/docs/atlas/app-services/sync/configure/sync-settings/#data-ingest), \nwhere clients can write data but not read.")
