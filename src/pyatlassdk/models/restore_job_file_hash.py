"""Generated model for RestoreJobFileHash. Do not edit manually."""

from __future__ import annotations

from typing import Literal
from pyatlassdk.models.link import Link

from pydantic import BaseModel, ConfigDict, Field

class RestoreJobFileHash(BaseModel):
    """Key and value pair that map one restore file to one hashed checksum. This parameter applies after you download the corresponding `delivery.url`."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    file_name: str | None = Field(default=None, alias="fileName", description="Human-readable label that identifies the hashed file.")
    hash: str | None = Field(default=None, description="Hashed checksum that maps to the restore file.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    type_name: Literal["SHA1"] | None = Field(default=None, alias="typeName", description="Human-readable label that identifies the hashing algorithm used to compute the hash value.")
