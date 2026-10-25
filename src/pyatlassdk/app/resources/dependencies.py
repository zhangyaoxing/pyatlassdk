"""Generated resource for Dependencies. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import quote
from pyatlassdk.app.models.dependencies_summary import DependenciesSummary

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Dependencies:
    """Manage your application's [external dependencies](https://www.mongodb.com/docs/atlas/app-services/functions/dependencies/)."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_get_all_dependencies(
        self,
        app_id: str,
        group_id: str,
    ) -> DependenciesSummary:
        """
        List external dependencies

        List [external
        dependencies](https://www.mongodb.com/docs/atlas/app-services/functions/dependencies/) uploaded
        to the Atlas App Services App.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/dependencies"
        return self._client.request(
            method="GET",
            path=path,
            response_model=DependenciesSummary,
        )
