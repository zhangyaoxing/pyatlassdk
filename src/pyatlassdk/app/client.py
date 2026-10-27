"""Generated Atlas App Services Admin API client. Do not edit manually."""

from __future__ import annotations

import datetime as dt
from typing import Any, Mapping

import httpx
from pydantic import BaseModel, TypeAdapter

from pyatlassdk.app.resources.admin import Admin
from pyatlassdk.app.resources.apikeys import Apikeys
from pyatlassdk.app.resources.apps import Apps
from pyatlassdk.app.resources.authproviders import Authproviders
from pyatlassdk.app.resources.billing import Billing
from pyatlassdk.app.resources.custom_user_data import CustomUserData
from pyatlassdk.app.resources.data_api import DataApi
from pyatlassdk.app.resources.dependencies import Dependencies
from pyatlassdk.app.resources.deploy import Deploy
from pyatlassdk.app.resources.email import Email
from pyatlassdk.app.resources.endpoints import Endpoints
from pyatlassdk.app.resources.environments import Environments
from pyatlassdk.app.resources.event_subscriptions import EventSubscriptions
from pyatlassdk.app.resources.functions import Functions
from pyatlassdk.app.resources.graphql import Graphql
from pyatlassdk.app.resources.hosting import Hosting
from pyatlassdk.app.resources.log_forwarders import LogForwarders
from pyatlassdk.app.resources.logs import Logs
from pyatlassdk.app.resources.metrics import Metrics
from pyatlassdk.app.resources.notifications import Notifications
from pyatlassdk.app.resources.rules import Rules
from pyatlassdk.app.resources.schemas import Schemas
from pyatlassdk.app.resources.secrets import Secrets
from pyatlassdk.app.resources.security import Security
from pyatlassdk.app.resources.services import Services
from pyatlassdk.app.resources.sync import Sync
from pyatlassdk.app.resources.triggers import Triggers
from pyatlassdk.app.resources.users import Users
from pyatlassdk.app.resources.values import Values
from pyatlassdk.app.resources.webhooks import Webhooks

from pyatlassdk.app._errors import AtlasApiError

DEFAULT_BASE_URL = "https://services.cloud.mongodb.com/api/admin/v3.0"
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


def _json_object(response: httpx.Response, context: str) -> dict[str, Any]:
    try:
        payload = response.json()
    except ValueError as exc:
        raise AtlasApiError(
            response.status_code, f"{context} returned non-JSON", _payload(response)
        ) from exc
    if not isinstance(payload, dict):
        raise AtlasApiError(
            response.status_code, f"{context} returned a non-object", payload
        )
    return payload


class AtlasAppAdminClient:
    """Synchronous client for the MongoDB Atlas App Services Admin API."""

    def __init__(
        self,
        access_token: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
    ) -> None:
        if not access_token or not access_token.strip():
            raise ValueError("access_token must not be empty")
        self.auth_mode = "bearer"
        self._http = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers={"Authorization": f"Bearer {access_token}"},
        )
        self.admin = Admin(self)
        self.apikeys = Apikeys(self)
        self.apps = Apps(self)
        self.authproviders = Authproviders(self)
        self.billing = Billing(self)
        self.custom_user_data = CustomUserData(self)
        self.data_api = DataApi(self)
        self.dependencies = Dependencies(self)
        self.deploy = Deploy(self)
        self.email = Email(self)
        self.endpoints = Endpoints(self)
        self.environments = Environments(self)
        self.event_subscriptions = EventSubscriptions(self)
        self.functions = Functions(self)
        self.graphql = Graphql(self)
        self.hosting = Hosting(self)
        self.log_forwarders = LogForwarders(self)
        self.logs = Logs(self)
        self.metrics = Metrics(self)
        self.notifications = Notifications(self)
        self.rules = Rules(self)
        self.schemas = Schemas(self)
        self.secrets = Secrets(self)
        self.security = Security(self)
        self.services = Services(self)
        self.sync = Sync(self)
        self.triggers = Triggers(self)
        self.users = Users(self)
        self.values = Values(self)
        self.webhooks = Webhooks(self)

    @classmethod
    def login(
        cls,
        username: str,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        timeout: float = 30.0,
    ) -> AtlasAppAdminClient:
        """Exchange App Services API key credentials for an access token."""
        with httpx.Client(base_url=base_url, timeout=timeout) as http:
            response = http.post(
                "/auth/providers/mongodb-cloud/login",
                json={"username": username, "apiKey": api_key},
                headers={
                    "Accept": DEFAULT_ACCEPT,
                    "Content-Type": DEFAULT_CONTENT_TYPE,
                },
            )
        if response.status_code >= 300:
            raise AtlasApiError(
                response.status_code, response.text, _payload(response)
            )
        payload = _json_object(response, "App Services login")
        token = payload.get("access_token")
        if not isinstance(token, str) or not token:
            raise AtlasApiError(
                500, "Login response did not contain an access_token", payload
            )
        return cls(access_token=token, base_url=base_url, timeout=timeout)

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self._http.close()

    def __enter__(self) -> AtlasAppAdminClient:
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
