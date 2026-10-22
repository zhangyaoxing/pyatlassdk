"""Generated model for TeamEventTypeViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class TeamEventTypeViewForNdsGroup(str, Enum):
    """Unique identifier of event type."""
    TEAM_ADDED_TO_GROUP = "TEAM_ADDED_TO_GROUP"
    TEAM_REMOVED_FROM_GROUP = "TEAM_REMOVED_FROM_GROUP"
    TEAM_ROLES_MODIFIED = "TEAM_ROLES_MODIFIED"
