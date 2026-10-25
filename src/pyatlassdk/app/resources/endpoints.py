"""Generated resource for Endpoints. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.endpoint import Endpoint

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Endpoints:
    """
    View and manage your app's custom [HTTPS endpoints](https://www.mongodb.com/docs/atlas/app-services/data-api/custom-endpoints/).

    ## Construct a Custom HTTPS Endpoint Base URL

    HTTPS Endpoint requests use a base URL that's specific to your App and
    deployment model.

    For a globally deployed app, the base URL has the following format:

    ```
    https://data.mongodb-api.com/app/{ClientAppID}/endpoint
    ```

    A locally deployed app uses a similar base URL also includes the
    App's deployment region and cloud provider:

    ```
    https://{Region}.{Cloud}.data.mongodb-api.com/app/{ClientAppID}/endpoint
    ```

    You can find an App's `Region`, `Cloud`, and `ClientAppId` by
    calling the [Get an App](#tag/apps/operation/adminGetApplication) endpoint:

    ```sh
    curl -X GET https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId} \\
      -h 'Authorization: Bearer <AccessToken>'
    ```

    For example, consider an App that has the following configuration:

    ```json
    {
      "client_app_id": "myapp-abcde",
      "deployment_model": "LOCAL",
      "provider_region": "aws-us-east-1",
      ...
    }
    ```

    This App would use the following base URL for incoming custom HTTPS endpoint requests:

    ```text
    https://us-east-1.aws.data.mongodb-api.com/app/myapp-abcde/endpoint
    ```
    """

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_all_endpoints(
        self,
        app_id: str,
        group_id: str,
    ) -> list[dict[str, Any]]:
        """
        Get all endpoints

        Get all [endpoint](https://www.mongodb.com/docs/atlas/app-services/data-api/custom-endpoints/) configurations.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/endpoints"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[dict[str, Any]],
        )

    def admin_create_endpoint(
        self,
        app_id: str,
        group_id: str,
        body: Endpoint,
    ) -> dict[str, Any]:
        """
        Create an endpoint

        Create a new [endpoint](https://www.mongodb.com/docs/atlas/app-services/data-api/custom-endpoints/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A valid [configuration object](https://www.mongodb.com/docs/atlas/app-services/reference/config/https_endpoints/) for the new endpoint.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/endpoints"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_delete_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        group_id: str,
    ) -> dict[str, Any]:
        """
        Delete an endpoint

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            endpoint_id: The unique `_id` value of an endpoint
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/endpoints/{quote(str(endpoint_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=dict[str, Any],
        )

    def admin_get_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        group_id: str,
    ) -> dict[str, Any]:
        """
        Get an endpoint

        Get a specific [endpoint](https://www.mongodb.com/docs/atlas/app-services/data-api/custom-endpoints/)'s configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            endpoint_id: The unique `_id` value of an endpoint
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/endpoints/{quote(str(endpoint_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=dict[str, Any],
        )

    def admin_modify_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        group_id: str,
        body: Endpoint,
    ) -> dict[str, Any]:
        """
        Modify an endpoint

        Modify an existing [endpoint](https://www.mongodb.com/docs/atlas/app-services/data-api/custom-endpoints/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            endpoint_id: The unique `_id` value of an endpoint
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A valid, updated [configuration object](https://www.mongodb.com/docs/atlas/app-services/reference/config/https_endpoints/) for the endpoint.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/endpoints/{quote(str(endpoint_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )
