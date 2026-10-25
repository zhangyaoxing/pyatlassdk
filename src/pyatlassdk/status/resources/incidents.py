"""Generated resource for Incidents. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyatlassdk.status.models.incidents_response import IncidentsResponse

if TYPE_CHECKING:
    from pyatlassdk.status.client import AtlasStatusClient


class Incidents:
    """Operations for Incidents."""

    def __init__(self, client: AtlasStatusClient) -> None:
        self._client = client

    def get_all_incidents(
        self,
    ) -> IncidentsResponse:
        """
        Get All Incidents

        Retrieves the 50 most recent incidents, including unresolved and resolved/postmortem states.
        """
        path = "/incidents.json"
        return self._client.request(
            method="GET",
            path=path,
            response_model=IncidentsResponse,
        )

    def get_unresolved_incidents(
        self,
    ) -> IncidentsResponse:
        """
        Get Unresolved Incidents

        Retrieves a list of unresolved incidents (in states: Investigating, Identified, or Monitoring).
        """
        path = "/incidents/unresolved.json"
        return self._client.request(
            method="GET",
            path=path,
            response_model=IncidentsResponse,
        )
