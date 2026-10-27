"""Generated Atlas API client. Do not edit manually."""

from __future__ import annotations

import datetime as dt
import threading
import time
from typing import Any, Mapping

import httpx
from pydantic import BaseModel, TypeAdapter

from pyatlassdk.admin.resources.ai_model_api_keys import AIModelAPIKeys
from pyatlassdk.admin.resources.ai_model_rate_limits import AIModelRateLimits
from pyatlassdk.admin.resources.aws_clusters_dns import AWSClustersDNS
from pyatlassdk.admin.resources.access_tracking import AccessTracking
from pyatlassdk.admin.resources.activity_feed import ActivityFeed
from pyatlassdk.admin.resources.alert_configurations import AlertConfigurations
from pyatlassdk.admin.resources.alerts import Alerts
from pyatlassdk.admin.resources.atlas_search import AtlasSearch
from pyatlassdk.admin.resources.auditing import Auditing
from pyatlassdk.admin.resources.cloud_backups import CloudBackups
from pyatlassdk.admin.resources.cloud_migration_service import CloudMigrationService
from pyatlassdk.admin.resources.cloud_provider_access import CloudProviderAccess
from pyatlassdk.admin.resources.cluster_outage_simulation import ClusterOutageSimulationResource
from pyatlassdk.admin.resources.clusters import Clusters
from pyatlassdk.admin.resources.collection_level_metrics import CollectionLevelMetrics
from pyatlassdk.admin.resources.custom_database_roles import CustomDatabaseRoles
from pyatlassdk.admin.resources.data_federation import DataFederation
from pyatlassdk.admin.resources.database_users import DatabaseUsers
from pyatlassdk.admin.resources.encryption_at_rest_using_customer_key_management import EncryptionAtRestUsingCustomerKeyManagement
from pyatlassdk.admin.resources.events import Events
from pyatlassdk.admin.resources.federated_authentication import FederatedAuthentication
from pyatlassdk.admin.resources.flex_clusters import FlexClusters
from pyatlassdk.admin.resources.flex_restore_jobs import FlexRestoreJobs
from pyatlassdk.admin.resources.flex_snapshots import FlexSnapshots
from pyatlassdk.admin.resources.global_clusters import GlobalClusters
from pyatlassdk.admin.resources.invoices import Invoices
from pyatlassdk.admin.resources.ldap_configuration import LDAPConfiguration
from pyatlassdk.admin.resources.legacy_backup import LegacyBackup
from pyatlassdk.admin.resources.maintenance_windows import MaintenanceWindows
from pyatlassdk.admin.resources.metric_integrations import MetricIntegrations
from pyatlassdk.admin.resources.mongo_db_cloud_users import MongoDBCloudUsers
from pyatlassdk.admin.resources.monitoring_and_logs import MonitoringAndLogs
from pyatlassdk.admin.resources.network_peering import NetworkPeering
from pyatlassdk.admin.resources.online_archive import OnlineArchive
from pyatlassdk.admin.resources.organizations import Organizations
from pyatlassdk.admin.resources.overload_protection_simulation import OverloadProtectionSimulation
from pyatlassdk.admin.resources.performance_advisor import PerformanceAdvisor
from pyatlassdk.admin.resources.private_endpoint_services import PrivateEndpointServices
from pyatlassdk.admin.resources.programmatic_api_keys import ProgrammaticAPIKeys
from pyatlassdk.admin.resources.project_ip_access_list import ProjectIPAccessList
from pyatlassdk.admin.resources.projects import Projects
from pyatlassdk.admin.resources.push_based_log_export import PushBasedLogExport
from pyatlassdk.admin.resources.query_shape_insights import QueryShapeInsights
from pyatlassdk.admin.resources.rate_limiting import RateLimiting
from pyatlassdk.admin.resources.remote_mcp_configurations import RemoteMCPConfigurations
from pyatlassdk.admin.resources.resource_policies import ResourcePolicies
from pyatlassdk.admin.resources.rolling_index import RollingIndex
from pyatlassdk.admin.resources.root import Root
from pyatlassdk.admin.resources.serverless_instances import ServerlessInstances
from pyatlassdk.admin.resources.serverless_private_endpoints import ServerlessPrivateEndpoints
from pyatlassdk.admin.resources.service_accounts import ServiceAccounts
from pyatlassdk.admin.resources.streams import Streams
from pyatlassdk.admin.resources.teams import Teams
from pyatlassdk.admin.resources.third_party_integrations import ThirdPartyIntegrations
from pyatlassdk.admin.resources.x509_authentication import X509Authentication

from pyatlassdk.admin._errors import AtlasApiError

DEFAULT_BASE_URL = "https://cloud.mongodb.com/api/atlas/v2"
DEFAULT_OAUTH_TOKEN_URL = "https://cloud.mongodb.com/api/oauth/token"
DEFAULT_ACCEPT = "application/vnd.atlas.2025-03-12+json"
DEFAULT_CONTENT_TYPE = "application/vnd.atlas.2025-03-12+json"


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


class AtlasAdminClient:
    """Synchronous client for the MongoDB Atlas Administration API.

    Supports HTTP Digest authentication with Atlas API keys and OAuth 2.0
    client-credentials authentication with Atlas service account credentials.
    """

    def __init__(
        self,
        public_key: str | None = None,
        private_key: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str = DEFAULT_BASE_URL,
        oauth_token_url: str = DEFAULT_OAUTH_TOKEN_URL,
        timeout: float = 30.0,
    ) -> None:
        has_api_key = public_key is not None or private_key is not None
        has_service_account = client_id is not None or client_secret is not None
        if has_api_key and has_service_account:
            raise ValueError(
                "Pass either Atlas API keys or service account credentials, not both"
            )
        if has_api_key and not (public_key and private_key):
            raise ValueError(
                "Both public_key and private_key are required for Digest authentication"
            )
        if has_service_account and not (client_id and client_secret):
            raise ValueError(
                "Both client_id and client_secret are required for OAuth 2.0 authentication"
            )

        if public_key and private_key:
            self.auth_mode = "digest"
        elif client_id and client_secret:
            self.auth_mode = "oauth2"
        else:
            self.auth_mode = "anonymous"

        self._oauth_client_id = client_id
        self._oauth_client_secret = client_secret
        self._oauth_token_url = oauth_token_url
        self._oauth_token: str | None = None
        self._oauth_expires_at = 0.0
        self._oauth_lock = threading.Lock()

        auth = (
            httpx.DigestAuth(public_key, private_key)
            if public_key and private_key
            else None
        )
        self._http = httpx.Client(base_url=base_url, auth=auth, timeout=timeout)
        self.ai_model_api_keys = AIModelAPIKeys(self)
        self.ai_model_rate_limits = AIModelRateLimits(self)
        self.aws_clusters_dns = AWSClustersDNS(self)
        self.access_tracking = AccessTracking(self)
        self.activity_feed = ActivityFeed(self)
        self.alert_configurations = AlertConfigurations(self)
        self.alerts = Alerts(self)
        self.atlas_search = AtlasSearch(self)
        self.auditing = Auditing(self)
        self.cloud_backups = CloudBackups(self)
        self.cloud_migration_service = CloudMigrationService(self)
        self.cloud_provider_access = CloudProviderAccess(self)
        self.cluster_outage_simulation = ClusterOutageSimulationResource(self)
        self.clusters = Clusters(self)
        self.collection_level_metrics = CollectionLevelMetrics(self)
        self.custom_database_roles = CustomDatabaseRoles(self)
        self.data_federation = DataFederation(self)
        self.database_users = DatabaseUsers(self)
        self.encryption_at_rest_using_customer_key_management = EncryptionAtRestUsingCustomerKeyManagement(self)
        self.events = Events(self)
        self.federated_authentication = FederatedAuthentication(self)
        self.flex_clusters = FlexClusters(self)
        self.flex_restore_jobs = FlexRestoreJobs(self)
        self.flex_snapshots = FlexSnapshots(self)
        self.global_clusters = GlobalClusters(self)
        self.invoices = Invoices(self)
        self.ldap_configuration = LDAPConfiguration(self)
        self.legacy_backup = LegacyBackup(self)
        self.maintenance_windows = MaintenanceWindows(self)
        self.metric_integrations = MetricIntegrations(self)
        self.mongo_db_cloud_users = MongoDBCloudUsers(self)
        self.monitoring_and_logs = MonitoringAndLogs(self)
        self.network_peering = NetworkPeering(self)
        self.online_archive = OnlineArchive(self)
        self.organizations = Organizations(self)
        self.overload_protection_simulation = OverloadProtectionSimulation(self)
        self.performance_advisor = PerformanceAdvisor(self)
        self.private_endpoint_services = PrivateEndpointServices(self)
        self.programmatic_api_keys = ProgrammaticAPIKeys(self)
        self.project_ip_access_list = ProjectIPAccessList(self)
        self.projects = Projects(self)
        self.push_based_log_export = PushBasedLogExport(self)
        self.query_shape_insights = QueryShapeInsights(self)
        self.rate_limiting = RateLimiting(self)
        self.remote_mcp_configurations = RemoteMCPConfigurations(self)
        self.resource_policies = ResourcePolicies(self)
        self.rolling_index = RollingIndex(self)
        self.root = Root(self)
        self.serverless_instances = ServerlessInstances(self)
        self.serverless_private_endpoints = ServerlessPrivateEndpoints(self)
        self.service_accounts = ServiceAccounts(self)
        self.streams = Streams(self)
        self.teams = Teams(self)
        self.third_party_integrations = ThirdPartyIntegrations(self)
        self.x509_authentication = X509Authentication(self)

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self._http.close()

    def __enter__(self) -> AtlasAdminClient:
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def _access_token(self, *, refresh: bool = False) -> str:
        """Return a cached OAuth 2.0 token, fetching a new one when needed."""
        with self._oauth_lock:
            now = time.monotonic()
            if not refresh and self._oauth_token is not None and now < self._oauth_expires_at:
                return self._oauth_token
            if self._oauth_client_id is None or self._oauth_client_secret is None:
                raise AtlasApiError(401, "OAuth 2.0 credentials are not configured")
            response = self._http.post(
                self._oauth_token_url,
                data={
                    "grant_type": "client_credentials",
                    "client_id": self._oauth_client_id,
                    "client_secret": self._oauth_client_secret,
                },
            )
            if response.status_code >= 300:
                raise AtlasApiError(
                    response.status_code,
                    "Failed to obtain an OAuth 2.0 access token",
                    _payload(response),
                )
            payload = _json_object(response, "OAuth token endpoint")
            token = payload.get("access_token")
            if not isinstance(token, str) or not token:
                raise AtlasApiError(
                    500,
                    "OAuth 2.0 response did not contain an access_token",
                    payload,
                )
            try:
                lifetime = float(payload.get("expires_in", 3600))
            except (TypeError, ValueError):
                lifetime = 3600.0
            self._oauth_token = token
            self._oauth_expires_at = now + max(lifetime - 60.0, 1.0)
            return token

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
        if self.auth_mode == "oauth2":
            headers["Authorization"] = f"Bearer {self._access_token()}"

        request_kwargs: dict[str, Any] = {
            "params": {
                key: value for key, value in (params or {}).items() if value is not None
            },
            "json": _serialize(json),
            "headers": headers,
        }
        response = self._http.request(method, path, **request_kwargs)
        if response.status_code == 401 and self.auth_mode == "oauth2":
            headers["Authorization"] = f"Bearer {self._access_token(refresh=True)}"
            response = self._http.request(method, path, **request_kwargs)
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
