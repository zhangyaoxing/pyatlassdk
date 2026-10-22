"""Generated model for StateReason. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class StateReason(BaseModel):
    """State reason of the Job. This is set when the job state is "Failed"."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    error_code: str | None = Field(default=None, alias="errorCode", description="Error code relating to state.")
    message: str | None = Field(default=None, description="Message describing error or state.")
