"""Generated model for ResourceEventTypeView. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class ResourceEventTypeView(str, Enum):
    """Unique identifier of event type."""
    TAGS_MODIFIED = "TAGS_MODIFIED"
    CLUSTER_TAGS_MODIFIED = "CLUSTER_TAGS_MODIFIED"
    GROUP_TAGS_MODIFIED = "GROUP_TAGS_MODIFIED"
