"""Atlas Status API: every endpoint, request shape and response model."""

from __future__ import annotations

import httpx
import pytest

from conftest import Recorder, status_client
from pyatlassdk import AtlasStatusApiError, AtlasStatusClient
from pyatlassdk.status import client as status_module
from pyatlassdk.status.models.component import Component
from pyatlassdk.status.models.components_response import ComponentsResponse
from pyatlassdk.status.models.incidents_response import IncidentsResponse
from pyatlassdk.status.models.overall_status_response import OverallStatusResponse
from pyatlassdk.status.models.scheduled_maintenances_response import (
    ScheduledMaintenancesResponse,
)
from pyatlassdk.status.models.status_summary_response import StatusSummaryResponse

PAGE = {
    "id": "page-1",
    "name": "MongoDB Cloud Status",
    "url": "https://status.mongodb.com",
    "updated_at": "2026-01-01T00:00:00Z",
}
COMPONENT = {
    "id": "c1",
    "name": "Atlas Clusters",
    "status": "operational",
    "created_at": "2025-01-01T00:00:00Z",
    "updated_at": "2026-01-01T00:00:00Z",
    "position": 1,
    "showcase": True,
    "only_show_if_degraded": False,
    "page_id": "page-1",
}
INCIDENT_UPDATE = {
    "id": "u1",
    "incident_id": "i1",
    "body": "We are looking into it",
    "status": "investigating",
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-01T00:00:00Z",
    "display_at": "2026-01-01T00:00:00Z",
}
INCIDENT = {
    "id": "i1",
    "name": "Elevated errors",
    "status": "investigating",
    "impact": "minor",
    "shortlink": "https://stspg.io/abc",
    "page_id": "page-1",
    "created_at": "2026-01-01T00:00:00Z",
    "updated_at": "2026-01-01T00:00:00Z",
    "incident_updates": [INCIDENT_UPDATE],
}
MAINTENANCE = {
    **{k: v for k, v in INCIDENT.items() if k != "status"},
    "status": "scheduled",
    "impact": "maintenance",
    "scheduled_for": "2026-02-01T00:00:00Z",
    "scheduled_until": "2026-02-01T02:00:00Z",
}


def respond(recorder: Recorder, body: object, status: int = 200) -> None:
    recorder.response = lambda request: httpx.Response(status, json=body)


def test_defaults() -> None:
    with AtlasStatusClient() as client:
        assert client.auth_mode == "none"
        assert str(client._http.base_url).rstrip("/") == status_module.DEFAULT_BASE_URL
        assert "authorization" not in client._http.headers


def test_resources_are_attached() -> None:
    with AtlasStatusClient() as client:
        for name in ("components", "incidents", "maintenance", "status"):
            assert getattr(client, name)._client is client


def test_get_overall_status(recorder: Recorder) -> None:
    respond(recorder, {"page": PAGE, "status": {"description": "All Systems Operational", "indicator": "none"}})

    result = status_client(recorder).status.get_overall_status()

    assert isinstance(result, OverallStatusResponse)
    assert result.status.indicator == "none"
    assert result.page.name == "MongoDB Cloud Status"
    assert recorder.last.method == "GET"
    assert recorder.last.url.path == "/api/status.json"
    assert "authorization" not in recorder.last.headers


def test_get_status_summary(recorder: Recorder) -> None:
    respond(
        recorder,
        {
            "page": PAGE,
            "status": {"description": "Minor", "indicator": "minor"},
            "components": [COMPONENT],
            "incidents": [INCIDENT],
            "scheduled_maintenances": [],
        },
    )

    result = status_client(recorder).status.get_status_summary()

    assert isinstance(result, StatusSummaryResponse)
    assert recorder.last.url.path == "/api/summary.json"
    assert result.components[0].name == "Atlas Clusters"
    assert result.incidents[0].incident_updates[0].body == "We are looking into it"
    assert result.scheduled_maintenances == []


def test_list_components(recorder: Recorder) -> None:
    respond(recorder, {"page": PAGE, "components": [COMPONENT]})

    result = status_client(recorder).components.get_components()

    assert isinstance(result, ComponentsResponse)
    assert isinstance(result.components[0], Component)
    assert recorder.last.url.path == "/api/components.json"


def test_list_incidents_endpoints(recorder: Recorder) -> None:
    respond(recorder, {"page": PAGE, "incidents": [INCIDENT]})
    client = status_client(recorder)

    unresolved = client.incidents.get_unresolved_incidents()
    everything = client.incidents.get_all_incidents()

    assert isinstance(unresolved, IncidentsResponse)
    assert isinstance(everything, IncidentsResponse)
    assert [r.url.path for r in recorder.requests] == [
        "/api/incidents/unresolved.json",
        "/api/incidents.json",
    ]


@pytest.mark.parametrize(
    "method, path",
    [
        ("get_all_scheduled_maintenances", "/api/scheduled-maintenances.json"),
        ("get_upcoming_scheduled_maintenances", "/api/scheduled-maintenances/upcoming.json"),
        ("get_active_scheduled_maintenances", "/api/scheduled-maintenances/active.json"),
    ],
)
def test_maintenance_endpoints(recorder: Recorder, method: str, path: str) -> None:
    respond(recorder, {"page": PAGE, "scheduled_maintenances": [MAINTENANCE]})

    result = getattr(status_client(recorder).maintenance, method)()

    assert isinstance(result, ScheduledMaintenancesResponse)
    assert recorder.last.url.path == path
    assert result.scheduled_maintenances[0].status == "scheduled"


def test_server_error_is_raised(recorder: Recorder) -> None:
    respond(recorder, {"error": "down"}, status=503)

    with pytest.raises(AtlasStatusApiError) as excinfo:
        status_client(recorder).status.get_overall_status()

    assert excinfo.value.status_code == 503


@pytest.mark.parametrize("indicator", ["none", "minor", "major", "critical"])
def test_status_indicator_values_are_accepted(recorder: Recorder, indicator: str) -> None:
    respond(recorder, {"page": PAGE, "status": {"description": "d", "indicator": indicator}})

    assert status_client(recorder).status.get_overall_status().status.indicator == indicator


def test_unknown_status_indicator_is_rejected(recorder: Recorder) -> None:
    respond(recorder, {"page": PAGE, "status": {"description": "d", "indicator": "purple"}})

    with pytest.raises(Exception, match="indicator"):
        status_client(recorder).status.get_overall_status()


def test_unknown_response_fields_are_preserved(recorder: Recorder) -> None:
    respond(
        recorder,
        {"page": PAGE, "status": {"description": "d", "indicator": "none", "brand_new": 1}},
    )

    result = status_client(recorder).status.get_overall_status()

    assert result.status.model_extra == {"brand_new": 1}
