"""Generated model for ServerlessInstanceDescriptionConnectionStrings. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.serverless_connection_strings_private_endpoint_list import ServerlessConnectionStringsPrivateEndpointList

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ServerlessInstanceDescriptionConnectionStrings(BaseModel):
    """Collection of Uniform Resource Locators that point to the MongoDB database."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    private_endpoint: list[ServerlessConnectionStringsPrivateEndpointList] | None = Field(default=None, alias="privateEndpoint", description="List of private endpoint-aware connection strings that you can use to connect to this serverless instance through a private endpoint. This parameter returns only if you created a private endpoint for this serverless instance and it is AVAILABLE.")
    standard_srv: str | None = Field(default=None, alias="standardSrv", description="Public connection string that you can use to connect to this serverless instance. This connection string uses the `mongodb+srv://` protocol.")
