"""Generated model for TeamEventTypeViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class TeamEventTypeViewForNdsGroup(CaseInsensitiveEnum):
    """Unique identifier of event type."""
    TEAM_ADDED_TO_GROUP = "TEAM_ADDED_TO_GROUP"
    TEAM_REMOVED_FROM_GROUP = "TEAM_REMOVED_FROM_GROUP"
    TEAM_ROLES_MODIFIED = "TEAM_ROLES_MODIFIED"
