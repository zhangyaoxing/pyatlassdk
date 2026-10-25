"""Generated resource for Status. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyatlassdk.status.models.overall_status_response import OverallStatusResponse
from pyatlassdk.status.models.status_summary_response import StatusSummaryResponse

if TYPE_CHECKING:
    from pyatlassdk.status.client import AtlasStatusClient


class Status:
    """MongoDB Atlas status operations including overall status, components, incidents, and scheduled maintenance"""

    def __init__(self, client: AtlasStatusClient) -> None:
        self._client = client

    def get_overall_status(
        self,
    ) -> OverallStatusResponse:
        """
        Get Overall Status

        Retrieves the overall status rollup for the entire page.
        """
        path = "/status.json"
        return self._client.request(
            method="GET",
            path=path,
            response_model=OverallStatusResponse,
        )

    def get_status_summary(
        self,
    ) -> StatusSummaryResponse:
        """
        Get Status Summary

        Retrieves a summary of the status page, including the overall status indicator,       
        component statuses, unresolved incidents, and upcoming or in-progress scheduled maintenances.
        """
        path = "/summary.json"
        return self._client.request(
            method="GET",
            path=path,
            response_model=StatusSummaryResponse,
        )
