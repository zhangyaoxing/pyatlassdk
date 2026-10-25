"""Generated model for LogType. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class LogType(str, Enum):
    """Generated enum for LogType."""
    AUTH = "auth"
    ENDPOINT = "endpoint"
    FUNCTION = "function"
    GRAPHQL = "graphql"
    PUSH = "push"
    SCHEMA = "schema"
    SERVICE = "service"
    SYNC = "sync"
    TRIGGER = "trigger"
    TRIGGER_ERROR_HANDLER = "trigger_error_handler"
