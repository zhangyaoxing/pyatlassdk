"""Generated model for DataApiConfig. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Any, Literal
from pyatlassdk.app._enums import upper_case
from pyatlassdk.app.models.data_api_version import DataApiVersion
from pyatlassdk.app.models.endpoint_data_format import EndpointDataFormat

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DataApiConfig(BaseModel):
    """Generated model for DataApiConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    disabled: bool
    versions: list[DataApiVersion]
    return_type: EndpointDataFormat = Field(description="The default [data format](https://mongodb.com/docs/atlas/app-services/data-api/#data-formats) returned by Data API endpoints.")
    create_user_on_auth: bool | None = None
    run_as_user_id: str | None = Field(default=None, description="An application user's account ID. If defined, endpoints will always run as the specified user.")
    run_as_user_id_script_source: str | None = Field(default=None, description="Stringified source code for a function that returns an\napplication user's account ID. If defined, endpoints execute\nthe function on every request and run as the user with the\nID returned from the function.")
    validation_method: Annotated[Literal["NO_VALIDATION", "SECRET_AS_QUERY_PARAM", "VERIFY_PAYLOAD"], BeforeValidator(upper_case)]
    secret_name: str | None = Field(default=None, description="If `validation_method` is set to `\"SECRET_AS_QUERY_PARAM\"`\nor `\"VERIFY_PAYLOAD\"`, this is the `name` of the\n[Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/)\nthat authorizes requests.")
    can_evaluate: dict[str, Any] | None = Field(default=None, description="A JSON expression that evaluates to `true` if an endpoint is\nallowed to run in response to an incoming request.")
