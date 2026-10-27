"""Generated model for EmailPasswordAuthProviderConfigVariant2. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EmailPasswordAuthProviderConfigVariant2(BaseModel):
    """Generated model for EmailPasswordAuthProviderConfigVariant2."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_confirm: Literal[True] | None = Field(default=None, alias="autoConfirm", description="If `true`, automatically confirm new user accounts without additional verification.")
    run_reset_function: Literal[True] | None = Field(default=None, alias="runResetFunction", description="If `true`, use a custom function that you define to handle\nthe password reset process.")
    reset_function_name: str | None = Field(default=None, alias="resetFunctionName", description="The name of the custom function that handles the password\nreset process.")
