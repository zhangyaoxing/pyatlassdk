"""Generated model for HostingConfigurationDefaultDomain. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.hosting_configuration_default_domain_config import HostingConfigurationDefaultDomainConfig

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class HostingConfigurationDefaultDomain(BaseModel):
    """Generated model for HostingConfigurationDefaultDomain."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    provider_type: str | None = None
    config: HostingConfigurationDefaultDomainConfig | None = None
