"""Generated model for AuthenticationTriggerConfig. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.app._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuthenticationTriggerConfig(BaseModel):
    """Generated model for AuthenticationTriggerConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    operation_type: Annotated[Literal["LOGIN", "CREATE", "DELETE"], BeforeValidator(upper_case)] = Field(description="The type of authentication event that the trigger listens for.")
    providers: Literal["anon-user", "api-key", "custom-token", "custom-function", "local-userpass", "oauth2-apple", "oauth2-facebook", "oauth2-google"] = Field(description="The type(s) of authentication provider that the trigger listens to.")
