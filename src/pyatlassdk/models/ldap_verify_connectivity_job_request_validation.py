"""Generated model for LDAPVerifyConnectivityJobRequestValidation. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LDAPVerifyConnectivityJobRequestValidation(BaseModel):
    """One test that MongoDB Cloud runs to test verification of the provided Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS) configuration details."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    status: Annotated[Literal["FAIL", "OK"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable string that indicates the result of this verification test.")
    validation_type: Annotated[Literal["AUTHENTICATE", "AUTHORIZATION_ENABLED", "CONNECT", "PARSE_AUTHZ_QUERY", "QUERY_SERVER", "SERVER_SPECIFIED", "TEMPLATE"], BeforeValidator(upper_case)] | None = Field(default=None, alias="validationType", description="Human-readable label that identifies this verification test that MongoDB Cloud runs.")
