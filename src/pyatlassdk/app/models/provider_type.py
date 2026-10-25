"""Generated model for ProviderType. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class ProviderType(str, Enum):
    """Generated enum for ProviderType."""
    ANON_USER = "anon-user"
    LOCAL_USERPASS = "local-userpass"
    API_KEY = "api-key"
    OAUTH2_APPLE = "oauth2-apple"
    OAUTH2_GOOGLE = "oauth2-google"
    OAUTH2_FACEBOOK = "oauth2-facebook"
    CUSTOM_TOKEN = "custom-token"
    CUSTOM_FUNCTION = "custom-function"
