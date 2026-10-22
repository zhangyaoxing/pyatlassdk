"""Generated model for ResourceTag. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class ResourceTag(BaseModel):
    """Key-value pair that tags and categorizes a MongoDB Cloud organization, project, or cluster. For example, `environment : production`."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    key: str = Field(description="Constant that defines the set of the tag. For example, `environment` in the `environment : production` tag.")
    value: str = Field(description="Variable that belongs to the set of the tag. For example, `production` in the `environment : production` tag.")
