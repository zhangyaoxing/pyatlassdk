"""Generated model for ReplicaSetMatcherField. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class ReplicaSetMatcherField(str, Enum):
    """Name of the parameter in the target object that MongoDB Cloud checks. The parameter must match all rules for MongoDB Cloud to check for alert configurations."""
    REPLICA_SET_NAME = "REPLICA_SET_NAME"
    SHARD_NAME = "SHARD_NAME"
    CLUSTER_NAME = "CLUSTER_NAME"
