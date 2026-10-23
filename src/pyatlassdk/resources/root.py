"""Generated resource for Root. Do not edit manually."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyatlassdk.models.control_plane_ip_addresses import ControlPlaneIPAddresses
from pyatlassdk.models.system_status import SystemStatus

if TYPE_CHECKING:
    from pyatlassdk.client import AtlasClient


class Root:
    """Returns details that describe the MongoDB Cloud build and the access token that requests this resource. This starts the MongoDB Cloud API."""

    def __init__(self, client: AtlasClient) -> None:
        self._client = client

    def get_system_status(
        self,
        *,
        envelope: bool | None = None,
        pretty: bool | None = None,
    ) -> SystemStatus:
        """
        Return the Status of This MongoDB Application

        This resource returns information about the MongoDB application along with API key meta data.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
            pretty: Flag that indicates whether the response body should be in the prettyprint format.
        """
        path = "/"
        params = {
            "envelope": envelope,
            "pretty": pretty,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=SystemStatus,
            accept="application/vnd.atlas.2023-01-01+json",
        )

    def list_control_plane_ip_addresses(
        self,
        *,
        envelope: bool | None = None,
    ) -> ControlPlaneIPAddresses:
        """
        Return All Control Plane IP Addresses

        Returns all control plane IP addresses.

        Args:
            envelope: Flag that indicates whether Application wraps the response in an `envelope` JSON object. Some API clients cannot access the HTTP response headers or status code. To remediate this, set envelope=true in the query. Endpoints that return a list of results use the results object as an envelope. Application adds the status parameter to the response body.
        """
        path = "/unauth/controlPlaneIPAddresses"
        params = {
            "envelope": envelope,
        }
        return self._client.request(
            method="GET",
            path=path,
            params=params,
            response_model=ControlPlaneIPAddresses,
            accept="application/vnd.atlas.2023-11-15+json",
        )
