"""Generated model for HostingConstructor. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class HostingConstructor(BaseModel):
    """Generated model for HostingConstructor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool
    custom_domain: str | None = None
    default_error_path: str | None = None
    default_error_code: str | None = None
