"""Generated model for OrgServiceAccountRequest. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class OrgServiceAccountRequest(BaseModel):
    """Organization Service Account that Atlas creates for this organization. If omitted, Atlas doesn't create an organization Service Account for this organization. If specified, this object requires all body parameters. Note that API Keys cannot be specified in the same request."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str = Field(description="Human readable description for the Service Account.")
    name: str = Field(description="Human-readable name for the Service Account. The name is modifiable and does not have to be unique.")
    roles: list[Literal["ORG_MEMBER", "ORG_READ_ONLY", "ORG_BILLING_ADMIN", "ORG_BILLING_READ_ONLY", "ORG_STREAM_PROCESSING_ADMIN", "ORG_GROUP_CREATOR", "ORG_OWNER"]] = Field(description="A list of organization-level roles for the Service Account.")
    secret_expires_after_hours: int | None = Field(default=None, alias="secretExpiresAfterHours", description="The expiration time of the new Service Account secret, provided in hours. The minimum and maximum allowed expiration times are subject to change and are controlled by the organization's settings. Required unless `withoutInitialSecret` is true.")
    without_initial_secret: bool | None = Field(default=None, alias="withoutInitialSecret", description="If true, creates the Service Account without generating an initial secret. `secretExpiresAfterHours` must not be set when this is true. Defaults to false, which preserves existing behavior: a secret is generated and returned in the response. Use the `CreateOrgServiceAccountSecret` endpoint to add a secret later.")
