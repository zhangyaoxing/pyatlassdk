"""Generated model for AuditLog. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk._enums import upper_case

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuditLog(BaseModel):
    """Generated model for AuditLog."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    audit_authorization_success: bool | None = Field(default=None, alias="auditAuthorizationSuccess", description="Flag that indicates whether someone set auditing to track successful authentications. This only applies to the `\"atype\" : \"authCheck\"` audit filter. Setting this parameter to `true` degrades cluster performance.")
    audit_filter: str | None = Field(default=None, alias="auditFilter", description="JSON document that specifies which events to record. Escape any characters that may prevent parsing, such as single or double quotes, using a backslash (`\\`).")
    configuration_type: Annotated[Literal["NONE", "FILTER_BUILDER", "FILTER_JSON"], BeforeValidator(upper_case)] | None = Field(default=None, alias="configurationType", description="Human-readable label that displays how to configure the audit filter.")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether someone enabled database auditing for the specified project.")
