"""Generated model for DiskBackupRestoreMember. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.models.api_private_download_delivery_url import ApiPrivateDownloadDeliveryUrl

from pydantic import BaseModel, ConfigDict, Field

class DiskBackupRestoreMember(BaseModel):
    """Generated model for DiskBackupRestoreMember."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    download_url: str | None = Field(default=None, alias="downloadUrl", description="One Uniform Resource Locator that points to the compressed snapshot files for manual download. MongoDB Cloud returns this parameter when `\"deliveryType\" : \"download\"`.")
    private_download_delivery_urls: list[ApiPrivateDownloadDeliveryUrl] | None = Field(default=None, alias="privateDownloadDeliveryUrls", description="One or more Uniform Resource Locators (URLs) that point to the compressed snapshot files for manual download and the corresponding private endpoint(s). MongoDB Cloud returns this parameter when `\"deliveryType\" : \"download\"` and the download can be performed privately.")
    replica_set_name: str | None = Field(default=None, alias="replicaSetName", description="Human-readable label that identifies the replica set on the sharded cluster.")
