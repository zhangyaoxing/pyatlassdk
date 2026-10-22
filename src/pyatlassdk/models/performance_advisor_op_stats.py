"""Generated model for PerformanceAdvisorOpStats. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

class PerformanceAdvisorOpStats(BaseModel):
    """Details that this resource returned about the specified query."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    ms: int | None = Field(default=None, description="Length of time expressed during which the query finds suggested indexes among the managed namespaces in the cluster. This parameter expresses its value in milliseconds. This parameter relates to the **duration** query parameter.")
    n_returned: int | None = Field(default=None, alias="nReturned", description="Number of results that the query returns.")
    n_scanned: int | None = Field(default=None, alias="nScanned", description="Number of documents that the query read.")
    ts: int | None = Field(default=None, description="Date and time from which the query retrieves the suggested indexes. This parameter expresses its value in the number of seconds that have elapsed since the UNIX epoch. This parameter relates to the **since** query parameter.")
