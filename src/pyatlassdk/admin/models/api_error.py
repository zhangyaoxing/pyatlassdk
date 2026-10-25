"""Generated model for ApiError. Do not edit manually."""

from __future__ import annotations

from typing import Any
from pyatlassdk.admin.models.bad_request_detail import BadRequestDetail

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ApiError(BaseModel):
    """Generated model for ApiError."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    bad_request_detail: BadRequestDetail | None = Field(default=None, alias="badRequestDetail")
    detail: str | None = Field(default=None, description="Describes the specific conditions or reasons that cause each type of error.")
    error: int = Field(description="HTTP status code returned with this error.")
    error_code: str = Field(alias="errorCode", description="Application error code returned with this error.")
    parameters: list[dict[str, Any]] | None = Field(default=None, description="Parameters used to give more information about the error.")
    reason: str | None = Field(default=None, description="Application error message returned with this error.")
