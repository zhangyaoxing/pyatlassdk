"""Generated model for ProjectSettingItemView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ProjectSettingItemView(BaseModel):
    """Generated model for ProjectSettingItemView."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool = Field(description="Flag that indicates whether someone enabled the regionalized private endpoint setting for the specified project.\n\n- Set this value to `true` to enable regionalized private endpoints. This allows you to create more than one private endpoint in a cloud provider region. You need to enable this setting to connect to multi-region and global MongoDB Cloud sharded clusters. Enabling regionalized private endpoints introduces the following limitations:\n  - Your applications must use the new connection strings for existing multi-region and global sharded clusters. This might cause downtime.\n  - Your MongoDB Cloud project can't contain replica sets nor can you create new replica sets in this project.\n\n  - You can't disable this setting if you have:\n    - more than one private endpoint in more than one region\n    - more than one private endpoint in one region and one private endpoint in one or more regions.\n\n- Set this value to `false` to disable regionalized private endpoints.")
