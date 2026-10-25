"""Generated model for IncomingWebhookOptions. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class IncomingWebhookOptions(BaseModel):
    """Generated model for IncomingWebhookOptions."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    secret: str | None = None
    secret_as_query_param: bool | None = Field(default=None, alias="secretAsQueryParam")
