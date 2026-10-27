"""Generated model for EmailPasswordAuthProviderConfigVariant3. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class EmailPasswordAuthProviderConfigVariant3(BaseModel):
    """Generated model for EmailPasswordAuthProviderConfigVariant3."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    auto_confirm: Literal[False] | None = Field(default=None, alias="autoConfirm", description="If `true`, automatically confirm new user accounts without\nadditional verification. For built-in email account\nconfirmation, set this value to `false`.")
    email_confirmation_url: str | None = Field(default=None, alias="emailConfirmationUrl", description="The URL included in the email sent to new users as part of\nthe built-in confirmation flow. The email also adds a unique\nconfirmation `token` and `tokenId` as query parameters.\n\nThis URL should handle user confirmation by passing the\nconfirmation token to a Realm SDK's `confirmUser` function\nor to the Admin API [Confirm a Pending Email/Password\nUser](#tag/email/operation/adminConfirmPendingUser)\nendpoint.")
    confirm_email_subject: str | None = Field(default=None, alias="confirmEmailSubject", description="The subject line of the email sent to new users as\npart of the built-in confirmation flow.")
    reset_password_url: str | None = Field(default=None, alias="resetPasswordUrl", description="The URL included in the email sent to users as part\nof the built-in password reset flow. The email also\nadds a unique password reset `token` and `tokenId` as\nquery parameters.\n\nThis URL should handle user confirmation by passing\nthe password reset token to a Realm SDK's `resetPassword`\nfunction.")
    reset_password_subject: str | None = Field(default=None, alias="resetPasswordSubject", description="The subject line of the email sent to users as\npart of the built-in password reset flow.")
