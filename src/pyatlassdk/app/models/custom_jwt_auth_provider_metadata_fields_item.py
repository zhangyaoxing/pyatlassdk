"""Generated model for CustomJwtAuthProviderMetadataFieldsItem. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class CustomJwtAuthProviderMetadataFieldsItem(BaseModel):
    """Generated model for CustomJwtAuthProviderMetadataFieldsItem."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    required: bool | None = Field(default=None, description="If `true`, this value must always be present in the external JWT.")
    name: str | None = Field(default=None, description="The name of the field in the external JWT that contains the data.\n\nTo specify a field in an embedded object, use [dot notation](https://www.mongodb.com/docs/manual/core/document/#dot-notation).")
    field_name: str | None = Field(default=None, description="The name of the field in User object that holds the value.")
