"""Generated Atlas Status API client. Do not edit manually."""

from __future__ import annotations

import datetime as dt
from typing import Any, Mapping

import httpx
from pydantic import BaseModel, TypeAdapter

from pyatlassdk.status.resources.components import Components
from pyatlassdk.status.resources.incidents import Incidents
from pyatlassdk.status.resources.maintenance import Maintenance
from pyatlassdk.status.resources.status import Status

from pyatlassdk.status._errors import AtlasApiError

DEFAULT_BASE_URL = "https://status.mongodb.com/api/v2"
DEFAULT_ACCEPT = "application/json"
DEFAULT_CONTENT_TYPE = "application/json"


def _serialize(value: Any) -> Any:
    if isinstance(value, BaseModel):
        return value.model_dump(mode="json", by_alias=True, exclude_none=True)
    if isinstance(value, list):
        return [_serialize(item) for item in value]
    if isinstance(value, dict):
        return {key: _serialize(item) for key, item in value.items()}
    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat()
    return value


def _payload(response: httpx.Response) -> Any:
    try:
        return response.json()
    except ValueError:
        return response.text


class AtlasStatusClient:
    """Synchronous client for the MongoDB Atlas Status API (public, no auth)."""

    def __init__(
        self,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
    ) -> None:
        self.auth_mode = "none"
        self._http = httpx.Client(base_url=base_url, timeout=timeout)
        self.components = Components(self)
        self.incidents = Incidents(self)
        self.maintenance = Maintenance(self)
        self.status = Status(self)

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self._http.close()

    def __enter__(self) -> AtlasStatusClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, Any] | None = None,
        json: Any = None,
        response_model: Any = None,
        accept: str | None = None,
        content_type: str | None = None,
    ) -> Any:
        """Send one request and validate the response into ``response_model``."""
        headers: dict[str, str] = {"Accept": accept or DEFAULT_ACCEPT}
        if json is not None:
            headers["Content-Type"] = content_type or DEFAULT_CONTENT_TYPE
        response = self._http.request(
            method,
            path,
            params={
                key: value for key, value in (params or {}).items() if value is not None
            },
            json=_serialize(json),
            headers=headers,
        )
        if response.status_code >= 300:
            raise AtlasApiError(
                response.status_code, response.text, _payload(response)
            )
        if not response.content:
            return None
        if response_model is None:
            return None
        if response_model is bytes:
            return response.content
        if response_model is str:
            media_type = response.headers.get("content-type", "").lower()
            if "json" in media_type:
                return TypeAdapter(str).validate_python(response.json())
            return response.text
        return TypeAdapter(response_model).validate_python(response.json())
