"""Generated model for Principal. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Principal(BaseModel):
    """Information about a principal, such as an OAuth application, that triggered the event through delegated access."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, description="The identifier of this principal.")
    name: str | None = Field(default=None, description="The human-readable name of this principal.")
    on_behalf_of: Principal | None = Field(default=None, alias="onBehalfOf")

Principal.model_rebuild()
