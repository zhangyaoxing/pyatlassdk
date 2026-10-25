"""Generated model for PushPullAppConfig. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.all_environment_values import AllEnvironmentValues
from pyatlassdk.app.models.app_environment import AppEnvironment
from pyatlassdk.app.models.auth_provider_constructor import AuthProviderConstructor
from pyatlassdk.app.models.cloud_provider_region_id import CloudProviderRegionId
from pyatlassdk.app.models.custom_user_data_constructor import CustomUserDataConstructor
from pyatlassdk.app.models.data_api_config import DataApiConfig
from pyatlassdk.app.models.data_source_constructor import DataSourceConstructor
from pyatlassdk.app.models.deployment_model import DeploymentModel
from pyatlassdk.app.models.endpoint_constructor import EndpointConstructor
from pyatlassdk.app.models.flexible_sync import FlexibleSync
from pyatlassdk.app.models.full_schema import FullSchema
from pyatlassdk.app.models.function_constructor import FunctionConstructor
from pyatlassdk.app.models.graph_ql_constructor import GraphQLConstructor
from pyatlassdk.app.models.hosting_constructor import HostingConstructor
from pyatlassdk.app.models.log_forwarder_constructor import LogForwarderConstructor
from pyatlassdk.app.models.third_party_service_constructor import ThirdPartyServiceConstructor
from pyatlassdk.app.models.trigger_constructor import TriggerConstructor
from pyatlassdk.app.models.value_constructor import ValueConstructor

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class PushPullAppConfig(BaseModel):
    """Generated model for PushPullAppConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="The App's name.")
    provider_region: CloudProviderRegionId
    deployment_model: DeploymentModel
    environment: AppEnvironment | None = Field(default=None, description="The App's environment tag. If not specified, the App has no environment tag.")
    auth_providers: list[AuthProviderConstructor]
    custom_user_data: CustomUserDataConstructor | None | None = None
    data_api_config: DataApiConfig | None | None = None
    data_sources: list[DataSourceConstructor]
    endpoints: list[EndpointConstructor]
    environments: AllEnvironmentValues
    functions: list[FunctionConstructor]
    graphql: GraphQLConstructor
    hosting: HostingConstructor
    https_endpoints: list[ThirdPartyServiceConstructor] = Field(description="[Deprecated] A list of legacy HTTP services. This is for backwards compatibility only.")
    log_forwarders: list[LogForwarderConstructor]
    schemas: list[FullSchema]
    services: list[ThirdPartyServiceConstructor] = Field(description="[Deprecated] A list of legacy third-party non-HTTP services. This is for backwards compatibility only.")
    sync: FlexibleSync
    triggers: list[TriggerConstructor]
    values: list[ValueConstructor]
