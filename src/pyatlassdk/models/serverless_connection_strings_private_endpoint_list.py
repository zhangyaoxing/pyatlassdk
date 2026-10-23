"""Generated model for ServerlessConnectionStringsPrivateEndpointList. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.serverless_connection_strings_private_endpoint_item import ServerlessConnectionStringsPrivateEndpointItem

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ServerlessConnectionStringsPrivateEndpointList(BaseModel):
    """Private endpoint connection string that you can use to connect to this serverless instance through a private endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    endpoints: list[ServerlessConnectionStringsPrivateEndpointItem] | None = Field(default=None, description="List that contains the private endpoints through which you connect to MongoDB Cloud when you use `connectionStrings.privateEndpoint[n].srvConnectionString`.")
    srv_connection_string: str | None = Field(default=None, alias="srvConnectionString", description="Private endpoint-aware connection string that uses the `mongodb+srv://` protocol to connect to MongoDB Cloud through a private endpoint. The `mongodb+srv` protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS).")
    type: Annotated[Literal["MONGOS"], BeforeValidator(upper_case)] | None = Field(default=None, description="MongoDB process type to which your application connects.")
