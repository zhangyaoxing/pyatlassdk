"""Generated model for EmailPasswordAuthProviderConfigVariant6. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EmailPasswordAuthProviderConfigVariant6(BaseModel):
    """Generated model for EmailPasswordAuthProviderConfigVariant6."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_confirm: Literal[false] | None = Field(default=None, alias="autoConfirm", description="If `true`, automatically confirm new user accounts without\nadditional verification. For custom function account\nconfirmation, set this value to `false`.")
    run_confirmation_function: bool | None = Field(default=None, alias="runConfirmationFunction", description="If `true`, new email/password user account registrations use\na custom function that you define to handle the confirmation\nprocess.")
    confirmation_function_name: str | None = Field(default=None, alias="confirmationFunctionName", description="The name of the custom function that handles the\nconfirmation process.")
    run_reset_function: Literal[true] | None = Field(default=None, alias="runResetFunction", description="If `true`, use a custom function that you define to handle\nthe password reset process.")
    reset_function_name: str | None = Field(default=None, alias="resetFunctionName", description="The name of the custom function that handles the password\nreset process.")
