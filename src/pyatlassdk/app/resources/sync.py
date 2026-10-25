"""Generated resource for Sync. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.pbs_sync_response import PbsSyncResponse
from pyatlassdk.app.models.sync_data_response import SyncDataResponse

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Sync:
    """Get information about [sync](https://www.mongodb.com/docs/atlas/app-services/sync/) for your application."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_flex_sync(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> SyncDataResponse:
        """
        Get Flexible Sync information

        Retrieve sync data for a specific Atlas App Services App when using
        [Flexible Sync](https://www.mongodb.com/docs/atlas/app-services/sync/get-started/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/service/{quote(str(service_id), safe='')}/config"
        return self._client.request(
            method="GET",
            path=path,
            response_model=SyncDataResponse,
        )

    def admin_get_sync(
        self,
        app_id: str,
        group_id: str,
        *,
        service_id: str,
    ) -> PbsSyncResponse:
        """
        Get Partition-Based Sync information

        Retrieve partition field data when using 
        [Partition-Based Sync](https://www.mongodb.com/docs/atlas/app-services/reference/partition-based-sync).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The Service ID for the linked cluster.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/sync/data"
        params = {
            "service_id": service_id,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=PbsSyncResponse,
        )
