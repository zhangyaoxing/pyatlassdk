"""Generated model for AssetMetadata. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.metadata_attribute import MetadataAttribute

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AssetMetadata(BaseModel):
    """Generated model for AssetMetadata."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    path: str | None = Field(default=None, description="The resource path of the asset")
    size: int | None = Field(default=None, description="The size of the asset in bytes")
    attrs: list[MetadataAttribute] | None = Field(default=None, description="An array of documents that each describe a [metadata\nattribute](https://www.mongodb.com/docs/atlas/app-services/hosting/file-metadata-attributes)\nthat applies to the asset.")
    hash: str | None = Field(default=None, description="The MD5 checksum hash for the asset")
