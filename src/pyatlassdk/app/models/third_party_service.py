"""Generated model for ThirdPartyService. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ThirdPartyService(BaseModel):
    """
    **THIRD-PARTY SERVICES ARE DEPRECATED**

    See [Third-Party Services](https://www.mongodb.com/docs/atlas/app-services/reference/services/) for more information.
    """
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="A unique ID for the third-party service.")
    name: str | None = Field(default=None, description="The third-party service name.")
    type: Literal["aws", "twilio", "github", "gcm"] | None = Field(default=None, description="The type of third party service.")
    version: int | None = None
