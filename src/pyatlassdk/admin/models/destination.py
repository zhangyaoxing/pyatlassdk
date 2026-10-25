"""Generated model for Destination. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Destination(BaseModel):
    """Document that describes the destination of the migration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    cluster_name: str = Field(alias="clusterName", description="Label that identifies the destination cluster.")
    group_id: str = Field(alias="groupId", description="Unique 24-hexadecimal digit string that identifies the destination project.")
    hostname_schema_type: Annotated[Literal["PUBLIC", "PRIVATE_LINK", "VPC_PEERING"], BeforeValidator(upper_case)] = Field(alias="hostnameSchemaType", description="The network type to use between the migration host and the destination cluster.")
    private_link_id: str | None = Field(default=None, alias="privateLinkId", description="Represents the endpoint to use when the host schema type is `PRIVATE_LINK`.")
