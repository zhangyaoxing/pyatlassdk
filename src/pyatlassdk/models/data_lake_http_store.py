"""Generated model for DataLakeHTTPStore. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class DataLakeHTTPStore(BaseModel):
    """Group of settings that define where the data is stored."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="Human-readable label that identifies the data store. The **databases.[n].collections.[n].dataSources.[n].storeName** field references this values as part of the mapping configuration. To use MongoDB Cloud as a data store, the data lake requires a serverless instance or an `M10` or higher cluster.")
    provider: str
    allow_insecure: bool | None = Field(default=None, alias="allowInsecure", description="Flag that validates the scheme in the specified URLs. If `true`, allows insecure `HTTP` scheme, doesn't verify the server's certificate chain and hostname, and accepts any certificate with any hostname presented by the server. If `false`, allows secure `HTTPS` scheme only.")
    default_format: str | None = Field(default=None, alias="defaultFormat", description="Default format that Data Lake assumes if it encounters a file without an extension while searching the `storeName`. If omitted, Data Lake attempts to detect the file type by processing a few bytes of the file. The specified format only applies to the URLs specified in the **databases.[n].collections.[n].dataSources** object.")
    urls: list[str] | None = Field(default=None, description="Comma-separated list of publicly accessible HTTP URLs where data is stored. You can't specify URLs that require authentication.")
