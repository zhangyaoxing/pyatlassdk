"""Generated model for GroupServiceAccountRequest. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class GroupServiceAccountRequest(BaseModel):
    """Generated model for GroupServiceAccountRequest."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    description: str = Field(description="Human readable description for the Service Account.")
    name: str = Field(description="Human-readable name for the Service Account. The name is modifiable and does not have to be unique.")
    roles: list[str] = Field(description="A list of project-level roles for the Service Account.")
    secret_expires_after_hours: int | None = Field(default=None, alias="secretExpiresAfterHours", description="The expiration time of the new Service Account secret, provided in hours. The minimum and maximum allowed expiration times are subject to change and are controlled by the organization's settings. Required unless `withoutInitialSecret` is true.")
    without_initial_secret: bool | None = Field(default=None, alias="withoutInitialSecret", description="If true, creates the Service Account without generating an initial secret. `secretExpiresAfterHours` must not be set when this is true. Defaults to false, which preserves existing behavior: a secret is generated and returned in the response. Use the `CreateGroupServiceAccountSecret` endpoint to add a secret later.")
