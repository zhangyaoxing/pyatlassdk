"""Generated model for AppServiceEventTypeViewAlertableNoThreshold. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class AppServiceEventTypeViewAlertableNoThreshold(CaseInsensitiveEnum):
    """Event type that triggers an alert."""
    URL_CONFIRMATION = "URL_CONFIRMATION"
    SUCCESSFUL_DEPLOY = "SUCCESSFUL_DEPLOY"
    DEPLOYMENT_FAILURE = "DEPLOYMENT_FAILURE"
    REQUEST_RATE_LIMIT = "REQUEST_RATE_LIMIT"
    LOG_FORWARDER_FAILURE = "LOG_FORWARDER_FAILURE"
    SYNC_FAILURE = "SYNC_FAILURE"
    TRIGGER_FAILURE = "TRIGGER_FAILURE"
    TRIGGER_AUTO_RESUMED = "TRIGGER_AUTO_RESUMED"
    DEPLOYMENT_MODEL_CHANGE_SUCCESS = "DEPLOYMENT_MODEL_CHANGE_SUCCESS"
    DEPLOYMENT_MODEL_CHANGE_FAILURE = "DEPLOYMENT_MODEL_CHANGE_FAILURE"
