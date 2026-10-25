"""Generated model for ClusterEventTypeViewForNdsGroup. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin._enums import CaseInsensitiveEnum

class ClusterEventTypeViewForNdsGroup(CaseInsensitiveEnum):
    """Unique identifier of event type."""
    CLUSTER_MONGOS_IS_PRESENT = "CLUSTER_MONGOS_IS_PRESENT"
    CLUSTER_MONGOS_IS_MISSING = "CLUSTER_MONGOS_IS_MISSING"
