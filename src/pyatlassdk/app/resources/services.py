"""Generated resource for Services. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.atlas_cluster import AtlasCluster
from pyatlassdk.app.models.atlas_cluster_service_config_instance import AtlasClusterServiceConfigInstance
from pyatlassdk.app.models.atlas_cluster_service_constructor import AtlasClusterServiceConstructor
from pyatlassdk.app.models.atlas_federated_instance import AtlasFederatedInstance
from pyatlassdk.app.models.build_info import BuildInfo
from pyatlassdk.app.models.linking_data_source_constructor import LinkingDataSourceConstructor
from pyatlassdk.app.models.third_party_service import ThirdPartyService
from pyatlassdk.app.models.third_party_service_constructor import ThirdPartyServiceConstructor

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Services:
    """View and manage your application's [data sources](https://www.mongodb.com/docs/atlas/app-services/mongodb/) and [third-party services [Deprecated]](https://www.mongodb.com/docs/atlas/app-services/reference/services/)"""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_link_multi_data_sources(
        self,
        app_id: str,
        group_id: str,
        *,
        body: list[LinkingDataSourceConstructor] | None = None,
    ) -> None:
        """
        Link multiple data sources

        Call this endpoint to link multiple data sources to an App. The total 
        limit of linked data sources per App is 100. Data Sources linked by this
        endpoint will have `ReadAndWrite` default rules.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/multi_data_sources"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_list_services(
        self,
        app_id: str,
        group_id: str,
    ) -> Any:
        """
        List all data sources and third-party services

        List all [data sources](https://www.mongodb.com/docs/atlas/app-services/mongodb/) and [third-party
        services [Deprecated]](https://www.mongodb.com/docs/atlas/app-services/reference/services/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_create_service(
        self,
        app_id: str,
        group_id: str,
        *,
        body: AtlasClusterServiceConstructor | AtlasFederatedInstance | ThirdPartyServiceConstructor | None = None,
    ) -> AtlasCluster | AtlasFederatedInstance | ThirdPartyService:
        """
        Create a data source or third-party service

        Create a [data source](https://www.mongodb.com/docs/atlas/app-services/mongodb/) or [third-party
        service [Deprecated]](https://www.mongodb.com/docs/atlas/app-services/reference/services/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=AtlasCluster | AtlasFederatedInstance | ThirdPartyService,
            content_type="application/json",
        )

    def admin_delete_service(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> None:
        """
        Delete a data source or third-party service

        Delete a [data source](https://www.mongodb.com/docs/atlas/app-services/mongodb/)
        or [third-party service [Deprecated]](https://www.mongodb.com/docs/atlas/app-services/reference/services/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_service(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> AtlasCluster | AtlasFederatedInstance | ThirdPartyService:
        """
        Get a data source or third-party service

        Get a [data source](https://www.mongodb.com/docs/atlas/app-services/mongodb/) or [third-party service [Deprecated]](https://www.mongodb.com/docs/atlas/app-services/reference/services/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=AtlasCluster | AtlasFederatedInstance | ThirdPartyService,
        )

    def admin_update_service(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> None:
        """
        Update a service

        Update a service.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}"
        return self._client.request(
            method="PATCH",
            path=path,
            response_model=None,
        )

    def get_build_info(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> BuildInfo:
        """
        Get information about the underlying Atlas mongod

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/commands/build_info"
        return self._client.request(
            method="GET",
            path=path,
            response_model=BuildInfo,
        )

    def admin_generate_schema(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
        body: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Generate a JSON schema from sample

        Sample a subset of documents in a collection to generate a JSON schema.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/commands/generate_schema"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_run_command(
        self,
        app_id: str,
        command_name: str,
        group_id: str,
        service_id: str,
    ) -> None:
        """
        Run a command associated with a service

        Run a command associated with a
        [service](https://www.mongodb.com/docs/atlas/app-services/reference/services).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            command_name: Command name
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/commands/{quote(str(command_name), safe='')}"
        return self._client.request(
            method="POST",
            path=path,
            response_model=None,
        )

    def admin_get_service_config(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
    ) -> Any:
        """
        Get a Service Configuration

        Get configuration of [data
        sources](https://www.mongodb.com/docs/atlas/app-services/mongodb/)
        and [third-party services [Deprecated]](https://www.mongodb.com/docs/atlas/app-services/reference/services/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/config"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_update_service_config(
        self,
        app_id: str,
        group_id: str,
        service_id: str,
        *,
        body: AtlasClusterServiceConfigInstance | AtlasFederatedInstance | ThirdPartyServiceConstructor | None = None,
    ) -> None:
        """
        Update a Service Configuration

        Update a [Data Source](https://www.mongodb.com/docs/atlas/app-services/mongodb/) or
        [Third-Party Service [Deprecated]](https://www.mongodb.com/docs/atlas/app-services/reference/services/)
        configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            service_id: The unique `_id` value of a service.
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/services/{quote(str(service_id), safe='')}/config"
        return self._client.request(
            method="PATCH",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
