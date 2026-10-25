"""Generated model for HostingConfiguration. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.app.models.hosting_configuration_default_domain import HostingConfigurationDefaultDomain

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class HostingConfiguration(BaseModel):
    """Generated model for HostingConfiguration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = None
    status: Literal["setup_ok", "change_in_progress", "change_failed", "change_failed_fatal"] | None = None
    default_domain: HostingConfigurationDefaultDomain | None = None
