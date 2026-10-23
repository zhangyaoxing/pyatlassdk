"""Generated model for NDSAutoscalingMatcherField. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class NDSAutoscalingMatcherField(CaseInsensitiveEnum):
    """Name of the parameter in the target object that MongoDB Cloud checks. The parameter must match all rules for MongoDB Cloud to check for alert configurations."""
    CLUSTER_NAME = "CLUSTER_NAME"
