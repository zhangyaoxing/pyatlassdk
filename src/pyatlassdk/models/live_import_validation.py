"""Generated model for LiveImportValidation. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class LiveImportValidation(BaseModel):
    """Generated model for LiveImportValidation."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    id: str | None = Field(default=None, alias="_id", description="Unique 24-hexadecimal digit string that identifies the validation.")
    error_message: str | None = Field(default=None, alias="errorMessage", description="Reason why the validation job failed.")
    group_id: str | None = Field(default=None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project to validate.")
    source_group_id: str | None = Field(default=None, alias="sourceGroupId", description="Unique 24-hexadecimal digit string that identifies the source project.")
    status: Literal["PENDING", "SUCCESS", "FAILED"] | None = Field(default=None, description="State of the specified validation job returned at the time of the request.")
