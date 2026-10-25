"""Generated model for NullableAppEnvironment. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class NullableAppEnvironment(str, Enum):
    """The application's environment. An empty string indicates that the app does not have a specified environment."""
    VALUE_0 = ""
    DEVELOPMENT = "development"
    TESTING = "testing"
    QA = "qa"
    PRODUCTION = "production"
