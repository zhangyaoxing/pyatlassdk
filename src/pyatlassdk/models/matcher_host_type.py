"""Generated model for MatcherHostType. Do not edit manually."""

from __future__ import annotations

from pyatlassdk._enums import CaseInsensitiveEnum

class MatcherHostType(CaseInsensitiveEnum):
    """Value to match or exceed using the specified `matchers.operator`."""
    STANDALONE = "STANDALONE"
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"
    ARBITER = "ARBITER"
    MONGOS = "MONGOS"
    CONFIG = "CONFIG"
    MONGOT = "MONGOT"
