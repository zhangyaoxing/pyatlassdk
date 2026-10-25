"""Generated model for AppEnvironment. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class AppEnvironment(str, Enum):
    """The application's environment."""
    DEVELOPMENT = "development"
    TESTING = "testing"
    QA = "qa"
    PRODUCTION = "production"
