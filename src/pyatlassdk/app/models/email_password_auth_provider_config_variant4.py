"""Generated model for EmailPasswordAuthProviderConfigVariant4. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EmailPasswordAuthProviderConfigVariant4(BaseModel):
    """Generated model for EmailPasswordAuthProviderConfigVariant4."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_confirm: Literal[false] | None = Field(default=None, alias="autoConfirm", description="If `true`, automatically confirm new user accounts without\nadditional verification. For built-in email account\nconfirmation, set this value to `false`.")
    email_confirmation_url: str | None = Field(default=None, alias="emailConfirmationUrl", description="The URL included in the email sent to new users as part of\nthe built-in confirmation flow. The email also adds a unique\nconfirmation `token` and `tokenId` as query parameters.\n\nThis URL should handle user confirmation by passing the\nconfirmation token to a Realm SDK's `confirmUser` function\nor to the Admin API [Confirm a Pending Email/Password\nUser](#tag/email/operation/adminConfirmPendingUser)\nendpoint.")
    confirm_email_subject: str | None = Field(default=None, alias="confirmEmailSubject", description="The subject line of the email sent to new users as\npart of the built-in confirmation flow.")
    run_reset_function: Literal[true] | None = Field(default=None, alias="runResetFunction", description="If `true`, use a custom function that you define to handle\nthe password reset process.")
    reset_function_name: str | None = Field(default=None, alias="resetFunctionName", description="The name of the custom function that handles the password\nreset process.")
