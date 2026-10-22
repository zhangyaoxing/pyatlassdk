"""Generated model for ClusterDescriptionConnectionStringsPrivateEndpoint. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.cluster_description_connection_strings_private_endpoint_endpoint import ClusterDescriptionConnectionStringsPrivateEndpointEndpoint

from pydantic import BaseModel, ConfigDict, Field

class ClusterDescriptionConnectionStringsPrivateEndpoint(BaseModel):
    """Private endpoint-aware connection string that you can use to connect to this cluster through a private endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    connection_string: str | None = Field(default=None, alias="connectionString", description="Private endpoint-aware connection string that uses the `mongodb://` protocol to connect to MongoDB Cloud through a private endpoint.")
    endpoints: list[ClusterDescriptionConnectionStringsPrivateEndpointEndpoint] | None = Field(default=None, description="List that contains the private endpoints through which you connect to MongoDB Cloud when you use `connectionStrings.privateEndpoint[n].connectionString` or `connectionStrings.privateEndpoint[n].srvConnectionString`.")
    srv_connection_string: str | None = Field(default=None, alias="srvConnectionString", description="Private endpoint-aware connection string that uses the `mongodb+srv://` protocol to connect to MongoDB Cloud through a private endpoint. The `mongodb+srv` protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your application supports it. If it doesn't, use `connectionStrings.privateEndpoint[n].connectionString`.")
    srv_shard_optimized_connection_string: str | None = Field(default=None, alias="srvShardOptimizedConnectionString", description="Private endpoint-aware connection string optimized for sharded clusters that uses the `mongodb+srv://` protocol to connect to MongoDB Cloud through a private endpoint. If the connection string uses this Uniform Resource Identifier (URI) format, you don't need to change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your application and Atlas cluster supports it. If it doesn't, use and consult the documentation for `connectionStrings.privateEndpoint[n].srvConnectionString`.")
    type: Literal["MONGOD", "MONGOS"] | None = Field(default=None, description="MongoDB process type to which your application connects. Use `MONGOD` for replica sets and `MONGOS` for sharded clusters.")
