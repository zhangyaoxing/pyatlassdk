"""Generated model for UserIdentity. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.provider_type import ProviderType

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class UserIdentity(BaseModel):
    """
    An authenticated identity from an authentication provider. This
    represents the user account within an individual auth provider
    and maps the account to external authentication systems.
    """
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = None
    provider_type: ProviderType | None = None
    provider_id: str | None = None
