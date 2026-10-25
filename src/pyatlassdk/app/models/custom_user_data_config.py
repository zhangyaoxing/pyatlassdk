"""Generated model for CustomUserDataConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomUserDataConfig(BaseModel):
    """Generated model for CustomUserDataConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    database_name: str | None = Field(default=None, description="The name of the database that contains custom user data.")
    collection_name: str | None = Field(default=None, description="The name of the collection that contains custom user data.")
    user_id_field: str | None = Field(default=None, description="The name of a field that appears in every custom user data\ndocument and that contains the user account ID of each\ndocument's corresponding user.")
    enabled: bool | None = Field(default=None, description="If `true`, custom user data is enabled.")
    mongo_service_id: str | None = Field(default=None, description="The _id value of a linked MongoDB data source.\n    \nYou can list services with the\n[Get all services endpoint](#operation/adminListServices).\n\nData sources are services whose `type` is \"mongodb-atlas\".\nUse the `_id` value for the data source you want to link to\nthe Trigger.")
    on_user_creation_function_id: str | None = Field(default=None, description="The `_id` value of a [user creation\nfunction](https://www.mongodb.com/docs/atlas/app-services/users/enable-custom-user-data/#std-label-user-creation-function)\nthat runs whenever a new user registers.")
