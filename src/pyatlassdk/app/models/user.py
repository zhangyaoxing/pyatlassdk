"""Generated model for User. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal
from pyatlassdk.app.models.user_identity import UserIdentity

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class User(BaseModel):
    """Generated model for User."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="The unique user account ID")
    identities: list[UserIdentity] | None = Field(default=None, description="A list of authentication provider identities associated with the user account.")
    type: Literal["normal", "server"] | None = Field(default=None, description="The user type. Most users are `normal` and represent a\nspecific human user. Users created through the `api-key`\nprovider have the type `server` because they are typically\nused for programmatic access from a server.")
    creation_date: int | None = Field(default=None, description="The date and time that the user account was created.\nRepresented by the number of seconds since the UNIX epoch.")
    last_authentication_date: int | None = Field(default=None, description="The date and time that the user account last logged in or\nauthenticated a request. Represented by the number of\nseconds since the UNIX epoch.")
    disabled: bool | None = Field(default=None, description="If `true`, the user account is inactive and cannot login or interact with App Services.")
    data: dict[str, Any] | None = Field(default=None, description="Metadata that describes the user. This field combines the\ndata for all authentication identities associated with the\nuser. The exact field names and values depend on which\nauthentication providers the user has authenticated with.\n\nFor example, if a user has linked an email/password account\nwith their Google account, this object might contain their\n`email` as well as metadata fields from Google like `name`\nand `picture`.")
