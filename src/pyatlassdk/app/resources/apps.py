"""Generated resource for Apps. Do not edit manually."""

from __future__ import annotations

from typing import Literal, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.app_constructor import AppConstructor
from pyatlassdk.app.models.app_instance import AppInstance
from pyatlassdk.app.models.push_pull_app_config import PushPullAppConfig

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Apps:
    """View and manage applications in an Atlas project."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_list_applications(
        self,
        group_id: str,
        *,
        product: Literal["standard", "atlas", "data-api", "device-sync"] | None = None,
    ) -> list[AppInstance]:
        """
        List all App Services Apps in an Atlas project/group

        List all App Services Apps within an Atlas
        [project/group](https://docs.atlas.mongodb.com/tutorial/manage-projects/).

        Args:
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            product: One or more specific App Services product types. If specified, this endpoint only returns Apps of the specified product type(s). Most apps use the `standard` product type, which this endpoint returns by default. The `atlas`, `data-api`, and `device-sync` product types represent special apps for [Atlas Triggers](https://docs.mongodb.com/atlas/triggers), [Atlas Data API](https://docs.mongodb.com/atlas/api/data-api/), and [Atlas Device Sync](https://www.mongodb.com/docs/atlas/app-services/sync/) that you can access through the Atlas UI. You can specify multiple product types as a comma-separated list: ``` /groups/{groupId}/apps?product=atlas,data-api ```
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps"
        params = {
            "product": product,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=list[AppInstance],
        )

    def admin_create_application(
        self,
        group_id: str,
        body: AppConstructor,
        *,
        defaults: bool | None = None,
        product: Literal["standard", "atlas", "data-api", "device-sync"] | None = None,
    ) -> AppInstance:
        """
        Create a new app

        Args:
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            defaults: Whether or not to create a default application.
            product: The App's product type. Apps use the `standard` product type by default. For most apps, you do not need to specify a `product` at all, or should specify `standard`. The `atlas`, `data-api`, and `device-sync` product types represent special apps for [Atlas Triggers](https://docs.mongodb.com/atlas/triggers), [Atlas Data API](https://docs.mongodb.com/atlas/api/data-api/), and [Atlas Device Sync](https://www.mongodb.com/docs/atlas/app-services/sync/) that you can access through the Atlas UI.
            body: The application to create.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps"
        params = {
            "defaults": defaults,
            "product": product,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=AppInstance,
            content_type="application/json",
        )

    def admin_delete_application(
        self,
        app_id: str,
        group_id: str,
    ) -> None:
        """
        Delete an app

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_application(
        self,
        app_id: str,
        group_id: str,
    ) -> AppInstance:
        """
        Get an app

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=AppInstance,
        )

    def admin_export_application(
        self,
        app_id: str,
        group_id: str,
        *,
        deployment: str | None = None,
        source_control: bool | None = None,
        template: bool | None = None,
        version: str | None = None,
    ) -> None:
        """
        Export an app as a zip file

        **The Export Endpoint is deprecated. Instead, call the [Pull App
        Configuration Files](#operation/adminPullAppConfiguration)
        endpoint with an ``Accept: application/zip`` header.**

        [Export](https://www.mongodb.com/docs/atlas/app-services/apps/export/)
        an application as a zip file.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            deployment: The `_id` of a specific deployment to export. If not specified, export the latest deployment.
            source_control: If `true`, the exported directory is suitable for automatic deployment from GitHub or other source control. Cannot be used with the `template` query parameter.
            template: If `true`, the exported directory does not include any identifiers or other data that would tie the app to a specific deployment instance. Cannot be used with the `source_control` query parameter.
            version: The configuration file schema version to export. This value corresponds to `config_version` in `root_config.json`.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/export"
        params = {
            "deployment": deployment,
            "source_control": source_control,
            "template": template,
            "version": version,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=None,
        )

    def admin_pull_app_configuration(
        self,
        app_id: str,
        group_id: str,
    ) -> PushPullAppConfig | str:
        """
        Pull App Configuration Files

        Download the current App configuration. You can choose to
        download in two different formats:

        - A compressed zip file that contains the configuration file
          directory. This is most useful when you're working with the
          CLI, a version control system, or another environment based on
          the file system.

        - A single JSON object that contains the entire configuration.
          This is most useful when you're working with the API or
          another environment that can parse JSON.

        You specify which format to download by setting the `Accept`
        header.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/pull"
        return self._client.request(
            method="GET",
            path=path,
            response_model=PushPullAppConfig | str,
        )

    def admin_push_app_configuration(
        self,
        app_id: str,
        group_id: str,
        *,
        body: PushPullAppConfig | None = None,
    ) -> None:
        """
        Push App Configuration Files

        Upload a new full App configuration. This operation overwrites
        the entire existing App configuration.

        **Note:** If your App configuration includes any references to a
        Secret, you must [create the
        Secret](#operation/adminCreateASecret) before you push the
        configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/push"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
