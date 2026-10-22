"""Generated model for ClusterIPAddresses. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class ClusterIPAddresses(BaseModel):
    """List of IP addresses in a cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_name: str | None = Field(default=None, alias="clusterName", description="Human-readable label that identifies the cluster.")
    future_inbound: list[str] | None = Field(default=None, alias="futureInbound", description="List of future inbound IP addresses associated with the cluster. If your network allows outbound HTTP requests only to specific IP addresses, you must allow access to the following IP addresses so that your application can connect to your Atlas cluster.")
    future_outbound: list[str] | None = Field(default=None, alias="futureOutbound", description="List of future outbound IP addresses associated with the cluster. If your network allows inbound HTTP requests only from specific IP addresses, you must allow access from the following IP addresses so that your Atlas cluster can communicate with your webhooks and KMS.")
    inbound: list[str] | None = Field(default=None, description="List of inbound IP addresses associated with the cluster. If your network allows outbound HTTP requests only to specific IP addresses, you must allow access to the following IP addresses so that your application can connect to your Atlas cluster.")
    outbound: list[str] | None = Field(default=None, description="List of outbound IP addresses associated with the cluster. If your network allows inbound HTTP requests only from specific IP addresses, you must allow access from the following IP addresses so that your Atlas cluster can communicate with your webhooks and KMS.")
