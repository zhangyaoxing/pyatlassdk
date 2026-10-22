"""Generated model for SearchDeploymentAuditTypeView. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class SearchDeploymentAuditTypeView(str, Enum):
    """Unique identifier of event type."""
    SEARCH_DEPLOYMENT_CREATED = "SEARCH_DEPLOYMENT_CREATED"
    SEARCH_DEPLOYMENT_UPDATED = "SEARCH_DEPLOYMENT_UPDATED"
    SEARCH_DEPLOYMENT_DELETED = "SEARCH_DEPLOYMENT_DELETED"
