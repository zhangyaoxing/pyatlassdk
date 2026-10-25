"""Generated model for LogsPush. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.app._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsPush(BaseModel):
    """Common fields shared by all log types."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="A unique ID for the log entry.\n")
    co_id: str | None = Field(default=None, description="A correlation ID for the request that issued the logged\noperation.\n")
    domain_id: str | None = Field(default=None, description="The domain ID.\n")
    app_id: str | None = Field(default=None, description="The App's internal client ID value.\n")
    group_id: str | None = Field(default=None, description="The App's Atlas Project ID value.\n")
    request_url: str | None = Field(default=None, description="The URL that the incoming request was sent to.\n")
    request_method: str | None = Field(default=None, description="The HTTP method used by the incoming request.\n")
    started: str | None = Field(default=None, description="An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp for the start of the logged operation.\n")
    completed: str | None = Field(default=None, description="An [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp for the completion of the logged operation.\n")
    type: Annotated[Literal["PUSH"], BeforeValidator(upper_case)] | None = None
