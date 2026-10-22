"""Generated model for AWSCustomDNSEnabledView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class AWSCustomDNSEnabledView(BaseModel):
    """Generated model for AWSCustomDNSEnabledView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool = Field(description="Flag that indicates whether the project's clusters deployed to Amazon Web Services (AWS) use a custom Domain Name System (DNS).\nWhen `\"enabled\": true`, connect to your cluster using Private IP for Peering connection strings.")
