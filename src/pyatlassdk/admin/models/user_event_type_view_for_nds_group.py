"""Generated model for UserEventTypeViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin._enums import CaseInsensitiveEnum

class UserEventTypeViewForNdsGroup(CaseInsensitiveEnum):
    """Unique identifier of event type."""
    JOINED_GROUP = "JOINED_GROUP"
    REMOVED_FROM_GROUP = "REMOVED_FROM_GROUP"
    INVITED_TO_GROUP = "INVITED_TO_GROUP"
    REQUESTED_TO_JOIN_GROUP = "REQUESTED_TO_JOIN_GROUP"
    GROUP_INVITATION_DELETED = "GROUP_INVITATION_DELETED"
    USER_ROLES_CHANGED_AUDIT = "USER_ROLES_CHANGED_AUDIT"
    JOIN_GROUP_REQUEST_DENIED_AUDIT = "JOIN_GROUP_REQUEST_DENIED_AUDIT"
    JOIN_GROUP_REQUEST_APPROVED_AUDIT = "JOIN_GROUP_REQUEST_APPROVED_AUDIT"
