"""Generated model for SearchDeploymentAuditTypeView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class SearchDeploymentAuditTypeView(CaseInsensitiveEnum):
    """Unique identifier of event type."""
    SEARCH_DEPLOYMENT_CREATED = "SEARCH_DEPLOYMENT_CREATED"
    SEARCH_DEPLOYMENT_UPDATED = "SEARCH_DEPLOYMENT_UPDATED"
    SEARCH_DEPLOYMENT_DELETED = "SEARCH_DEPLOYMENT_DELETED"
