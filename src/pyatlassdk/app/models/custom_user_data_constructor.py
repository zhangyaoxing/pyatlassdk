"""Generated model for CustomUserDataConstructor. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomUserDataConstructor(BaseModel):
    """Generated model for CustomUserDataConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    database_name: str | None = Field(default=None, description="The name of the database that contains custom user data.")
    collection_name: str | None = Field(default=None, description="The name of the collection that contains custom user data.")
    user_id_field: str | None = Field(default=None, description="The name of a field that appears in every custom user data\ndocument and that contains the user account ID of each\ndocument's corresponding user.")
    enabled: bool | None = Field(default=None, description="If `true`, custom user data is enabled.")
    mongo_service_name: str = Field(description="The name of the linked MongoDB data source that contains\ncustom user data.")
    on_user_creation_function_name: str | None = Field(default=None, description="The name of a [user creation\nfunction](https://www.mongodb.com/docs/atlas/app-services/users/enable-custom-user-data/#std-label-user-creation-function)\nthat runs whenever a new user registers.")
