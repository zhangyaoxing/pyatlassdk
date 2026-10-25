"""Generated resource for Billing. Do not edit manually."""

from __future__ import annotations

from typing import Any, Literal, TYPE_CHECKING
from urllib.parse import quote

if TYPE_CHECKING:
    from pyatlassdk.app.client import AtlasAppAdminClient


class Billing:
    """View billed usage of your applications."""

    def __init__(self, client: AtlasAppAdminClient) -> None:
        self._client = client

    def admin_app_measurements(
        self,
        app_id: str,
        group_id: str,
        *,
        end: str | None = None,
        granularity: Literal["P31D", "PT1H"] | None = None,
        start: str | None = None,
    ) -> dict[str, Any]:
        """
        List app billing usage

        List the request, compute, sync, data transfer, and memory usage of a
        specific app in a given period for
        [billing](https://www.mongodb.com/docs/atlas/app-services/billing) purposes.

        Args:
            app_id: The ObjectID of your application. [The App Services API Project and Application IDs section](#section/Project-and-Application-IDs) demonstrates how to find this value.
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            end: The ISO 8601 date and time of the end of the query period. Default is 23:59:59 UTC on the last day of the current month.
            granularity: Specifies the granularity of the query period, either P31D (31 day) or PT1H (1 hour). Default is P31D.
            start: The ISO 8601 date and time of the start of the query period. Default is 00:00:00 UTC on the first day of the current month.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/apps/{quote(str(app_id), safe='')}/measurements"
        params = {
            "end": end,
            "granularity": granularity,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=dict[str, Any],
        )

    def admin_measurements(
        self,
        group_id: str,
        *,
        end: str | None = None,
        granularity: Literal["P31D", "PT1H"] | None = None,
        start: str | None = None,
    ) -> dict[str, Any]:
        """
        List group billing usage in a given period

        List the request, compute, sync, and data transfer usage in a given
        period for [billing](https://www.mongodb.com/docs/atlas/app-services/billing) purposes.

        Args:
            group_id: An Atlas [Project/Group ID](https://docs.atlas.mongodb.com/tutorial/manage-projects/).
            end: The ISO 8601 date and time of the end of the query period. Default is 23:59:59 UTC on the last day of the current month.
            granularity: Specifies the granularity of the query period, either P31D (31 day) or PT1H (1 hour). Default is P31D.
            start: The ISO 8601 date and time of the start of the query period. Default is 00:00:00 UTC on the first day of the current month.
        """
        path = f"/groups/{quote(str(group_id), safe='')}/measurements"
        params = {
            "end": end,
            "granularity": granularity,
            "start": start,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=dict[str, Any],
        )
