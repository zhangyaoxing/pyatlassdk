"""Generated resource for DataApi. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.data_api_config import DataApiConfig
from pyatlassdk.app.models.data_api_version import DataApiVersion

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class DataApi:
    """
    Manage your app's generated [Data API endpoints](https://www.mongodb.com/docs/atlas/app-services/data-api/generated-endpoints/).

    ## Construct a Data API Base URL

    Data API requests use a base URL that's specific to your App and
    deployment model.

    For a globally deployed app, the base URL has the following format:

    ```
    https://data.mongodb-api.com/app/{ClientAppID}/endpoint/data/{DataAPIVersion}
    ```

    A locally deployed app uses a similar base URL also includes the
    App's deployment region and cloud provider:

    ```
    https://{Region}.{Cloud}.data.mongodb-api.com/app/{ClientAppID}/endpoint/data/{DataAPIVersion}
    ```

    You can find an App's `Region`, `Cloud`, and `ClientAppId` in the
    [App Configuration](#tag/apps/operation/adminGetApplication):

    ```sh
    curl -X GET https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId} \\
      -h 'Authorization: Bearer <AccessToken>'
    ```

    You can see a list of all `DataAPIVersion` values supported by an App in
    the `versions` field of its [Data API
    Configuration](#tag/data-api/operation/adminGetDataApiConfig):

    ```sh
    curl -X GET "https://services.cloud.mongodb.com/api/admin/v3.0/groups/{groupId}/apps/{appId}/data_api/config" \\
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

    This App would use the following base URL for Data API v1 requests:

    ```text
    https://us-east-1.aws.data.mongodb-api.com/app/myapp-abcde/endpoint/data/v1
    ```
    """

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_data_api_config(
        self,
        app_id: str,
        group_id: str,
    ) -> DataApiConfig:
        """
        Get the Data API Configuration

        Get your app's [Data API](https://www.mongodb.com/docs/atlas/app-services/data-api/generated-endpoints/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/data_api/config"
        return self._client.request(
            method="GET",
            path=path,
            response_model=DataApiConfig,
        )

    def admin_modify_data_api_config(
        self,
        app_id: str,
        group_id: str,
        body: DataApiConfig,
    ) -> None:
        """
        Modify the Data API

        Update your app's [Data API](https://www.mongodb.com/docs/atlas/app-services/data-api/generated-endpoints/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A valid [configuration object](https://www.mongodb.com/docs/atlas/app-services/reference/config/https_endpoints/#data-api-configuration) for the endpoint.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/data_api/config"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_create_data_api_config(
        self,
        app_id: str,
        group_id: str,
        body: DataApiConfig,
    ) -> DataApiConfig:
        """
        Enable the Data API

        Create your app's [Data API](https://www.mongodb.com/docs/atlas/app-services/data-api/generated-endpoints/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A valid [configuration object](https://www.mongodb.com/docs/atlas/app-services/reference/config/https_endpoints/#data-api-configuration) for the endpoint.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/data_api/config"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=DataApiConfig,
            content_type="application/json",
        )

    def admin_get_data_api_versions(
        self,
        app_id: str,
        group_id: str,
    ) -> list[DataApiVersion]:
        """
        List Data API versions

        List all possible Data API versions.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/data_api/versions"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[DataApiVersion],
        )
