"""Generated pydantic models. Do not edit manually."""

from __future__ import annotations

import importlib

_MODULES = {
    'Component': 'component',
    'ComponentsResponse': 'components_response',
    'Error': 'error',
    'Incident': 'incident',
    'IncidentUpdate': 'incident_update',
    'IncidentsResponse': 'incidents_response',
    'OverallStatusResponse': 'overall_status_response',
    'PageInfo': 'page_info',
    'ScheduledMaintenance': 'scheduled_maintenance',
    'ScheduledMaintenancesResponse': 'scheduled_maintenances_response',
    'StatusIndicator': 'status_indicator',
    'StatusSummaryResponse': 'status_summary_response',
}

__all__ = sorted(_MODULES)


def __getattr__(name: str) -> object:
    module_name = _MODULES.get(name)
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = importlib.import_module(f"{__name__}.{module_name}")
    value = getattr(module, name)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted(_MODULES)
