"""Generated resource for Components. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyatlassdk.status.models.components_response import ComponentsResponse

if TYPE_CHECKING:
    from pyatlassdk.status.client import AtlasStatusClient


class Components:
    """Operations for Components."""

    def __init__(self, client: AtlasStatusClient) -> None:
        self._client = client

    def get_components(
        self,
    ) -> ComponentsResponse:
        """
        Get Components

        Retrieves a list of components and their current statuses.
        """
        path = "/components.json"
        return self._client.request(
            method="GET",
            path=path,
            response_model=ComponentsResponse,
        )
