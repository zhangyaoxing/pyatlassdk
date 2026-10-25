"""Generated model for DeploymentLocation. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app._enums import CaseInsensitiveEnum

class DeploymentLocation(CaseInsensitiveEnum):
    """
    An identifier of the location where an app server is physically
    deployed to, regardless of the cloud provider that hosts the
    app.
    """
    US_VA = "US-VA"
    US_OR = "US-OR"
    DE_FF = "DE-FF"
    IE = "IE"
    AU = "AU"
    IN_MB = "IN-MB"
    SG = "SG"
    BR_SP = "BR-SP"
