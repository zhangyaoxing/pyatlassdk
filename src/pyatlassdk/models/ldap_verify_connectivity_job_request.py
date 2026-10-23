"""Generated model for LDAPVerifyConnectivityJobRequest. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case
from pyatlassdk.models.ldap_verify_connectivity_job_request_params import LDAPVerifyConnectivityJobRequestParams
from pyatlassdk.models.ldap_verify_connectivity_job_request_validation import LDAPVerifyConnectivityJobRequestValidation
from pyatlassdk.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class LDAPVerifyConnectivityJobRequest(BaseModel):
    """Generated model for LDAPVerifyConnectivityJobRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project associated with this Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS) configuration.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    request: LDAPVerifyConnectivityJobRequestParams | None = None
    request_id: str | None = Field(default=None, alias="requestId", description="Unique 24-hexadecimal digit string that identifies this request to verify an Lightweight Directory Access Protocol (LDAP) configuration.")
    status: Annotated[Literal["FAIL", "PENDING", "SUCCESS"], BeforeValidator(upper_case)] | None = Field(default=None, description="Human-readable string that indicates the status of the Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS) configuration.")
    validations: list[LDAPVerifyConnectivityJobRequestValidation] | None = Field(default=None, description="List that contains the validation messages related to the verification of the provided Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS) configuration details. The list contains a document for each test that MongoDB Cloud runs. MongoDB Cloud stops running tests after the first failure.")
