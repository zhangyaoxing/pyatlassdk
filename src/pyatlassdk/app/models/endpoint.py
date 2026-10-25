"""Generated model for Endpoint. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.app._enums import upper_case
from pyatlassdk.app.models.endpoint_data_format import EndpointDataFormat

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class Endpoint(BaseModel):
    """Generated model for Endpoint."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    route: str
    http_method: Annotated[Literal["GET", "POST", "PUT", "PATCH", "DELETE", "*"], BeforeValidator(upper_case)]
    function_id: str = Field(description="The endpoint function's unique ID.")
    validation_method: Annotated[Literal["NO_VALIDATION", "SECRET_AS_QUERY_PARAM", "VERIFY_PAYLOAD"], BeforeValidator(upper_case)]
    secret_id: str | None = Field(default=None, description="If `validation_method` is set to `\"SECRET_AS_QUERY_PARAM\"`\nor `\"VERIFY_PAYLOAD\"`, this is the `_id` of the\n[Secret](https://www.mongodb.com/docs/atlas/app-services/values-and-secrets/)\nthat authorizes requests.")
    return_type: EndpointDataFormat = Field(description="The default [data format](https://mongodb.com/docs/atlas/app-services/data-api/#data-formats) returned by custom HTTPS endpoints.")
    respond_result: bool
    fetch_custom_user_data: bool | None = None
    create_user_on_auth: bool | None = None
    disabled: bool
    id: str | None = Field(default=None, alias="_id", description="The endpoint's unique ID.")
