"""Generated resource for Graphql. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.custom_resolver import CustomResolver
from pyatlassdk.app.models.graph_ql_config import GraphQLConfig
from pyatlassdk.app.models.graph_ql_validation_settings import GraphQLValidationSettings

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Graphql:
    """Configure and run GraphQL API operations."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_run_graph_ql_operation(
        self,
        app_id: str,
        group_id: str,
        *,
        body: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """
        Run a query or mutation

        Run a query or mutation as a system user that bypasses
        authentication and data access rules. You can access metadata
        about your API, including its schema, with an
        [introspection](https://graphql.org/learn/introspection/) query.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body:
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/graphql"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_get_graph_ql_config(
        self,
        app_id: str,
        group_id: str,
    ) -> GraphQLConfig:
        """
        Get GraphQL API Configuration

        Get your app's [GraphQL API](https://www.mongodb.com/docs/atlas/app-services/graphql/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/graphql/config"
        return self._client.request(
            method="GET",
            path=path,
            response_model=GraphQLConfig,
        )

    def admin_update_graph_ql_config(
        self,
        app_id: str,
        group_id: str,
        body: GraphQLConfig,
    ) -> None:
        """
        Update GraphQL API Configuration

        Update your app's [GraphQL API](https://www.mongodb.com/docs/atlas/app-services/graphql/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A valid [GraphQL API configuration object](https://www.mongodb.com/docs/atlas/app-services/reference/config/graphql#std-label-appconfig-graphql).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/graphql/config"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_get_all_custom_resolvers(
        self,
        app_id: str,
        group_id: str,
    ) -> list[CustomResolver]:
        """
        Get all custom resolvers

        Get all [custom resolver](https://www.mongodb.com/docs/atlas/app-services/graphql/custom-resolvers/) configurations from your app's GraphQL API.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/graphql/custom_resolvers"
        return self._client.request(
            method="GET",
            path=path,
            response_model=list[CustomResolver],
        )

    def admin_create_custom_resolver(
        self,
        app_id: str,
        group_id: str,
        body: CustomResolver,
    ) -> CustomResolver:
        """
        Create a custom resolver

        Create a new [custom resolver](https://www.mongodb.com/docs/atlas/app-services/graphql/custom-resolvers/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A valid [custom resolver configuration](https://www.mongodb.com/docs/atlas/app-services/reference/config/graphql#std-label-appconfig-custom-resolver) object.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/graphql/custom_resolvers"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=CustomResolver,
            content_type="application/json",
        )

    def admin_delete_custom_resolver(
        self,
        app_id: str,
        custom_resolver_id: str,
        group_id: str,
    ) -> None:
        """
        Delete a custom resolver

        Delete an existing [custom resolver](https://www.mongodb.com/docs/atlas/app-services/graphql/custom-resolvers/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            custom_resolver_id: The unique `_id` value of a custom resolver.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/graphql/custom_resolvers/{quote(str(custom_resolver_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_custom_resolver(
        self,
        app_id: str,
        custom_resolver_id: str,
        group_id: str,
    ) -> CustomResolver:
        """
        Get a custom resolver

        Get a specific [custom resolver](https://www.mongodb.com/docs/atlas/app-services/graphql/custom-resolvers/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            custom_resolver_id: The unique `_id` value of a custom resolver.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/graphql/custom_resolvers/{quote(str(custom_resolver_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=CustomResolver,
        )

    def admin_modify_custom_resolver(
        self,
        app_id: str,
        custom_resolver_id: str,
        group_id: str,
        body: CustomResolver,
    ) -> None:
        """
        Modify a custom resolver

        Modify an existing [custom resolver](https://www.mongodb.com/docs/atlas/app-services/graphql/custom-resolvers/) configuration.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            custom_resolver_id: The unique `_id` value of a custom resolver.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: A valid, updated [custom resolver configuration](https://www.mongodb.com/docs/atlas/app-services/reference/config/graphql#std-label-appconfig-custom-resolver) object.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/graphql/custom_resolvers/{quote(str(custom_resolver_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )

    def admin_get_graph_ql_validation_settings(
        self,
        app_id: str,
        group_id: str,
    ) -> GraphQLValidationSettings:
        """
        Get validation settings

        Get the current validation level and action for reads and writes.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/validation_settings/graphql"
        return self._client.request(
            method="GET",
            path=path,
            response_model=GraphQLValidationSettings,
        )

    def admin_set_graph_ql_validation_settings(
        self,
        app_id: str,
        group_id: str,
        body: GraphQLValidationSettings,
    ) -> None:
        """
        Modify validation settings

        Set the validation level and action for reads and writes.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The updated validation levels and actions.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/validation_settings/graphql"
        return self._client.request(
            method="PUT",
            path=path,
            json=body,
            response_model=None,
            content_type="application/json",
        )
