"""Generated model for FunctionConstructor. Do not edit manually."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FunctionConstructor(BaseModel):
    """Generated model for FunctionConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    can_evaluate: dict[str, Any] | None = Field(default=None, description="A JSON expression that evaluates to `true` if the Function is allowed to\nrun in response to an incoming request.")
    name: str = Field(description="A unique name for the Function.")
    private: bool = Field(description="If `true`, the function is hidden from client applications. You can\nstill call a private function from JSON expressions and other functions,\nincluding incoming webhooks and triggers.")
    source: str = Field(description="The stringified source code for the function. The code must be valid\nES6.")
    run_as_system: bool | None = Field(default=None, description="If `true`, the function executes with full privileges, bypassing rules\non all services.")
    run_as_user_id: str | None = Field(default=None, description="An application user's account ID. If defined, endpoints will always \nrun as the specified user. Cannot be used with \n`run_as_user_id_script_source`.")
    run_as_user_id_script_source: str | None = Field(default=None, description="The stringified source code for a \n[function](https://www.mongodb.com/docs/atlas/app-services/functions/#std-label-functions)\nthat returns an application user's account ID. If defined, endpoints \nexecute the function on every request and run as the user with the \nID returned from the function. Cannot be used with `run_as_user_id`.")
