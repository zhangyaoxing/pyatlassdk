"""Generated resource for Functions. Do not edit manually."""

from __future__ import annotations

from typing import Any, TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.function import Function
from pyatlassdk.app.models.function_constructor import FunctionConstructor

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Functions:
    """View and manage your app's [functions](https://www.mongodb.com/docs/atlas/app-services/functions/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_execute_function(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
        *,
        run_as_system: bool,
        user_id: str,
    ) -> dict[str, Any]:
        """
        Execute a function

        Execute a [function](https://www.mongodb.com/docs/atlas/app-services/functions/) for testing.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            run_as_system: Determine whether or not to run as system user. Either `run_as_system` or `user_id` is required. You cannot specify both.
            user_id: The user as which to execute the function. Either `user_id` or `run_as_system` is required. You cannot specify both.
            body: The function to execute.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/debug/execute_function"
        params = {
            "run_as_system": run_as_system,
            "user_id": user_id,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_execute_function_source(
        self,
        app_id: str,
        group_id: str,
        body: dict[str, Any],
        *,
        run_as_system: bool,
        user_id: str,
    ) -> dict[str, Any]:
        """
        Execute a function's source code for testing

        Execute a [function](https://www.mongodb.com/docs/atlas/app-services/functions/)'s source code
        for testing.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            run_as_system: Determine whether or not to run as system user. Either `run_as_system` or `user_id` is required. You cannot specify both.
            user_id: The user as which to execute the function. Either `user_id` or `run_as_system` is required. You cannot specify both.
            body: The source to execute.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/debug/execute_function_source"
        params = {
            "run_as_system": run_as_system,
            "user_id": user_id,
        }
        return self._client.request(
            method="POST",
            path=path,
            params=params,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_list_functions(
        self,
        app_id: str,
        group_id: str,
    ) -> Any:
        """
        List Functions

        List [Functions](https://www.mongodb.com/docs/atlas/app-services/functions/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/functions"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Any,
        )

    def admin_create_function(
        self,
        app_id: str,
        group_id: str,
        body: FunctionConstructor,
    ) -> dict[str, Any]:
        """
        Create a new Function

        Create a new [Function](https://www.mongodb.com/docs/atlas/app-services/functions/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            body: The function to create
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/functions"
        return self._client.request(
            method="POST",
            path=path,
            json=body,
            response_model=dict[str, Any],
            content_type="application/json",
        )

    def admin_delete_function(
        self,
        app_id: str,
        function_id: str,
        group_id: str,
    ) -> None:
        """
        Delete a Function

        Delete a [Function](https://www.mongodb.com/docs/atlas/app-services/functions/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            function_id: The unique `_id` value of a function.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/functions/{quote(str(function_id), safe='')}"
        return self._client.request(
            method="DELETE",
            path=path,
            response_model=None,
        )

    def admin_get_function(
        self,
        app_id: str,
        function_id: str,
        group_id: str,
    ) -> Function:
        """
        Retrieve a Function

        Retrieve a [Function](https://www.mongodb.com/docs/atlas/app-services/functions/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            function_id: The unique `_id` value of a function.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/functions/{quote(str(function_id), safe='')}"
        return self._client.request(
            method="GET",
            path=path,
            response_model=Function,
        )

    def admin_update_function(
        self,
        app_id: str,
        function_id: str,
        group_id: str,
    ) -> FunctionConstructor:
        """
        Update a Function

        Update a [Function](https://www.mongodb.com/docs/atlas/app-services/functions/).

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            function_id: The unique `_id` value of a function.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/functions/{quote(str(function_id), safe='')}"
        return self._client.request(
            method="PUT",
            path=path,
            response_model=FunctionConstructor,
        )
