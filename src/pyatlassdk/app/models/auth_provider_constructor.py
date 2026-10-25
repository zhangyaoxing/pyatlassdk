"""Generated model for AuthProviderConstructor. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.app.models.anonymous_auth_provider import AnonymousAuthProvider
from pyatlassdk.app.models.api_key_auth_provider import ApiKeyAuthProvider
from pyatlassdk.app.models.apple_auth_provider import AppleAuthProvider
from pyatlassdk.app.models.custom_function_auth_provider import CustomFunctionAuthProvider
from pyatlassdk.app.models.custom_jwt_auth_provider import CustomJwtAuthProvider
from pyatlassdk.app.models.email_password_auth_provider import EmailPasswordAuthProvider
from pyatlassdk.app.models.facebook_auth_provider import FacebookAuthProvider
from pyatlassdk.app.models.google_auth_provider import GoogleAuthProvider

AuthProviderConstructor: TypeAlias = AnonymousAuthProvider | EmailPasswordAuthProvider | ApiKeyAuthProvider | CustomJwtAuthProvider | CustomFunctionAuthProvider | AppleAuthProvider | GoogleAuthProvider | FacebookAuthProvider
