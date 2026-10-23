"""Generated model for HostMatcherField. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class HostMatcherField(CaseInsensitiveEnum):
    """Name of the parameter in the target object that MongoDB Cloud checks. The parameter must match all rules for MongoDB Cloud to check for alert configurations."""
    TYPE_NAME = "TYPE_NAME"
    HOSTNAME = "HOSTNAME"
    PORT = "PORT"
    HOSTNAME_AND_PORT = "HOSTNAME_AND_PORT"
    REPLICA_SET_NAME = "REPLICA_SET_NAME"
    ATLAS_NODE_TYPE = "ATLAS_NODE_TYPE"
