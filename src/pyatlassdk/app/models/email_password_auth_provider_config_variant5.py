"""Generated model for EmailPasswordAuthProviderConfigVariant5. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EmailPasswordAuthProviderConfigVariant5(BaseModel):
    """Generated model for EmailPasswordAuthProviderConfigVariant5."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_confirm: Literal[False] | None = Field(default=None, alias="autoConfirm", description="If `true`, automatically confirm new user accounts without\nadditional verification. For custom function account\nconfirmation, set this value to `false`.")
    run_confirmation_function: bool | None = Field(default=None, alias="runConfirmationFunction", description="If `true`, new email/password user account registrations use\na custom function that you define to handle the confirmation\nprocess.")
    confirmation_function_name: str | None = Field(default=None, alias="confirmationFunctionName", description="The name of the custom function that handles the\nconfirmation process.")
    reset_password_url: str | None = Field(default=None, alias="resetPasswordUrl", description="The URL included in the email sent to users as part\nof the built-in password reset flow. The email also\nadds a unique password reset `token` and `tokenId` as\nquery parameters.\n\nThis URL should handle user confirmation by passing\nthe password reset token to a Realm SDK's `resetPassword`\nfunction.")
    reset_password_subject: str | None = Field(default=None, alias="resetPasswordSubject", description="The subject line of the email sent to users as\npart of the built-in password reset flow.")
