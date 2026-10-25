"""Generated resource for Hosting. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.hosted_asset_metadata import HostedAssetMetadata
from pyatlassdk.app.models.hosting_configuration import HostingConfiguration

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Hosting:
    """
    Manage your application's [hosted files](https://www.mongodb.com/docs/atlas/app-services/hosting/).

    ## Asset Metadata Document Example

    Asset metadata documents describe hosted asset files.

    ```json
    {
      "path": "<Asset Resource Path>",
      "hash": "<Asset MD5 Checksum Hash>",
      "size": <File size in bytes>,
      "attrs": [
          {
            "name": "<Metadata Attribute Name>",
            "value": "<Metadata Attribute Value>",
          }
      ]
    }
    ```
    """

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_all_hosted_assets(
        self,
        app_id: str,
        group_id: str,
    ) -> list[HostedAssetMetadata]:
        """
        List all hosted assets

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/hosting/assets"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[HostedAssetMetadata],
        )

    def admin_move_copy_hosted_asset(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
    ) -> None:
        """
        Move or copy a hosted asset

        Move or copy a hosted asset to a new resource path.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The hosted asset file and its metadata. (Must use `Content-Type: multipart/mixed`)
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/hosting/assets"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_get_hosted_asset(
        self,
        app_id: str,
        group_id: str,
        *,
        path: str,
        prefix: str | None = None,
    ) -> HostedAssetMetadata:
        """
        Retrieve metadata for a specific hosted asset

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            path: The resource path of a hosted asset.
            prefix: Return only those assets where the resource path begins with the specified prefix.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/hosting/assets/asset"
        params = {
            "path": path,
            "prefix": prefix,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=HostedAssetMetadata,
        )

    def admin_update_hosted_asset(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
        *,
        path: str,
    ) -> None:
        """
        Update the metadata attributes of a hosted asset

        Update the metadata attributes of a hosted asset at a specific resource
        path.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            path: The resource path of a hosted asset.
            body: The new metadata attributes for the hosted asset. These attributes replace all existing attributes for the file.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/hosting/assets/asset"
        params = {
            "path": path,
        }
        return self._client.request(
            method="PATCH",
            path=path,
            params=params,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_upload_hosted_asset(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
        *,
        path: str,
    ) -> None:
        """
        Upload or replace a hosted asset

        Upload or replace a hosted asset at a specific resource path.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            path: The resource path of a hosted asset.
            body: The hosted asset file and its metadata. (Must use `Content-Type: multipart/mixed`)
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/hosting/assets/asset"
        params = {
            "path": path,
        }
        return self._client.request(
            method="PUT",
            path=path,
            params=params,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_get_hosting_config(
        self,
        app_id: str,
        group_id: str,
    ) -> HostingConfiguration:
        """
        Get Hosting Configuration

        Returns the current hosting configuration. Hosting is active
        if the response includes `status: "setup_ok"`.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/hosting/config"
        return self._client.request(
            method="GET",
            path=path,
            response_model=HostingConfiguration,
        )

    def admin_enable_disable_hosting(
        self,
        app_id: str,
        group_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> None:
        """
        Enable/Disable Hosting

        Enable or disable App Services Hosting for your app.
        Changes to hosting can take up to 15 minutes to take effect.
        This endpoint does not notify you when the changes have taken effect,
        only that the change operation was successfully received by the server.

        You can see if the hosting enablement/disablement is complete
        by calling the [Get Hosting Configuration](#operation/adminGetHostingConfig) endpoint.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/hosting/config"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
