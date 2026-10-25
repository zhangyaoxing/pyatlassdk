"""Generated model for LogsSyncClientWrite. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Any, Literal
from pyatlassdk.app._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LogsSyncClientWrite(BaseModel):
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
    user_id: str | None = Field(default=None, description="The user account ID of the user that initiated the logged operation.\n")
    remote_ip_address: str | None = Field(default=None, description="The IP address that the logged operation originated from.\n")
    status: float | None = Field(default=None, description="The HTTP status code returned in the operation response.\n")
    error: str | None = Field(default=None, description="If a runtime error occurred in the logged operation,\nthis is a message that describes the issue.\n")
    error_code: str | None = Field(default=None, description="If a runtime error occurred in the logged operation,\nthis is the error's short code.\n")
    platform: str | None = Field(default=None, description="The name of the platform that the client was running on.\n")
    platform_version: Any | None = Field(default=None, description="The version of the platform that the client was running on.\n")
    sdk_name: Any | None = Field(default=None, description="The name of the Realm SDK used to make the request.\n")
    sdk_version: Any | None = Field(default=None, description="The version number of the Realm SDK used to make the request.\n")
    function_call_location: str | None = Field(default=None, description="The global region where the function was executed.\n")
    function_call_provider_region: str | None = Field(default=None, description="The cloud provider deployment region where the function was\nexecuted.\n")
    function_call: dict[str, Any] | None = None
    function_id: str | None = None
    function_name: str | None = None
    messages: list[str] | None = Field(default=None, description="A list of logs or other messages associated with the operation.\n")
    sync_query: dict[str, Any] | None = Field(default=None, description="The current subscription queries for this Device Sync\nsession. This object maps object type names to the query for\nthat type.\n")
    sync_session_metrics: dict[str, Any] | None = Field(default=None, description="Usage metrics for the current Device Sync session.\n")
    type: Annotated[Literal["SYNC_CLIENT_WRITE"], BeforeValidator(upper_case)] | None = None
