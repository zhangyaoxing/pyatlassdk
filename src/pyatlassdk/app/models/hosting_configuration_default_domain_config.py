"""Generated model for HostingConfigurationDefaultDomainConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class HostingConfigurationDefaultDomainConfig(BaseModel):
    """Generated model for HostingConfigurationDefaultDomainConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    app_default_domain: str | None = Field(default=None, description="Default domain of hosted Atlas App Services App provided by App Services.")
