"""Generated model for HostedAssetMetadata. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.metadata_attribute import MetadataAttribute

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class HostedAssetMetadata(BaseModel):
    """Generated model for HostedAssetMetadata."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    app_id: str | None = Field(default=None, alias="appId", description="The unique App ID of the Atlas App Services App that is hosting the file.")
    last_modified: int | None = Field(default=None, description="The time at which the hosted asset was last modified in [Unix\ntime](https://en.wikipedia.org/wiki/Unix_time) (number of seconds since\nJanuary 1, 1970 at 00:00 UTC).")
    url: str | None = Field(default=None, description="The full URL of the hosted asset.")
    path: str | None = Field(default=None, description="The resource path of the hosted asset")
    size: int | None = Field(default=None, description="The size of the hosted asset in bytes")
    attrs: list[MetadataAttribute] | None = Field(default=None, description="An array of documents that each describe a [metadata\nattribute](https://www.mongodb.com/docs/atlas/app-services/hosting/file-metadata-attributes)\nthat applies to the asset.")
    hash: str | None = Field(default=None, description="The MD5 checksum hash for the hosted asset")
