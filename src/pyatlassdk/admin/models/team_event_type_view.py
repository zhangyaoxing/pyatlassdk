"""Generated model for TeamEventTypeView. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin._enums import CaseInsensitiveEnum

class TeamEventTypeView(CaseInsensitiveEnum):
    """Unique identifier of event type."""
    TEAM_CREATED = "TEAM_CREATED"
    TEAM_DELETED = "TEAM_DELETED"
    TEAM_UPDATED = "TEAM_UPDATED"
    TEAM_NAME_CHANGED = "TEAM_NAME_CHANGED"
    TEAM_ADDED_TO_GROUP = "TEAM_ADDED_TO_GROUP"
    TEAM_REMOVED_FROM_GROUP = "TEAM_REMOVED_FROM_GROUP"
    TEAM_ROLES_MODIFIED = "TEAM_ROLES_MODIFIED"
