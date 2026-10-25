"""Generated model for GoogleAuthProviderMetadataFieldsItemItem. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GoogleAuthProviderMetadataFieldsItemItem(BaseModel):
    """Generated model for GoogleAuthProviderMetadataFieldsItemItem."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    required: bool | None = Field(default=None, description="If `true`, include this metadata value in the OAuth JWT and the user's data.")
    name: str | None = Field(default=None, description="The name of a user metadata property accessible through OAuth, e.g. `email`.")
