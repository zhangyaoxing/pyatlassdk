"""Generated model for ApiPrivateDownloadDeliveryUrl. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiPrivateDownloadDeliveryUrl(BaseModel):
    """One Uniform Resource Locator (URL) that points to the compressed snapshot files for manual download and the corresponding private endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    delivery_url: str | None = Field(default=None, alias="deliveryUrl", description="One Uniform Resource Locator that points to the compressed snapshot files for manual download.")
    endpoint_id: str | None = Field(default=None, alias="endpointId", description="Unique 22-character alphanumeric string that identifies the private endpoint.")
