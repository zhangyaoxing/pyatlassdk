"""Generated model for Source. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class Source(BaseModel):
    """Document that describes the source of the migration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ca_certificate_path: str | None = Field(default=None, alias="caCertificatePath", description="Path to the CA certificate that signed SSL certificates use to authenticate to the source cluster.")
    cluster_name: str = Field(alias="clusterName", description="Label that identifies the source cluster name.")
    group_id: str = Field(alias="groupId", description="Unique 24-hexadecimal digit string that identifies the source project.")
    managed_authentication: bool = Field(alias="managedAuthentication", description="Flag that indicates whether MongoDB Automation manages authentication to the source cluster. If true, do not provide values for username and password.")
    password: str | None = Field(default=None, description="Password that authenticates the username to the source cluster.")
    ssl: bool = Field(description="Flag that indicates whether you have SSL enabled.")
    username: str | None = Field(default=None, description="Label that identifies the SCRAM-SHA user that connects to the source cluster.")
