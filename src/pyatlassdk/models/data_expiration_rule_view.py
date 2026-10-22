"""Generated model for DataExpirationRuleView. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class DataExpirationRuleView(BaseModel):
    """Rule for specifying when data should be deleted from the archive."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    expire_after_days: int | None = Field(default=None, alias="expireAfterDays", description="Number of days used in the date criteria for nominating documents for deletion.")
