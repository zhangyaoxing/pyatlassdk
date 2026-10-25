"""Generated model for StreamsAutoscaling. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.admin._enums import upper_case
from pyatlassdk.admin.models.link import Link

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class StreamsAutoscaling(BaseModel):
    """Autoscaling configuration for a stream processor."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether autoscaling is enabled.\n\n- **Omitted, `null`, or `false`:**\n  - On `CREATE`: a no-op, there is no persisted setting yet to disable or clear.\n  - On `MODIFY` or `:startWith`: omitted preserves the current setting. `null` or `false` disables autoscaling and clears its configuration.\n- **`true`** on `CREATE`, `MODIFY`, or `:startWith`: enables autoscaling.")
    links: list[Link] | None = Field(default=None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    max_tier: Annotated[Literal["SP50", "SP30", "SP10", "SP5", "SP2"], BeforeValidator(upper_case)] | None = Field(default=None, alias="maxTier", description="Tier ceiling for autoscaling (scale-up limit).\n\n- **Omitted:**\n  - On `CREATE`: falls back to the workspace max tier (there is no current bound to preserve).\n  - On `MODIFY` or `:startWith`: the current bound is preserved.\n- **`null`** on `CREATE`, `MODIFY`, or `:startWith`: resets the bound to the workspace max tier.\n- **A tier value** on `CREATE`, `MODIFY`, or `:startWith`: sets the bound to that tier.")
    min_tier: Annotated[Literal["SP50", "SP30", "SP10", "SP5", "SP2"], BeforeValidator(upper_case)] | None = Field(default=None, alias="minTier", description="Tier floor for autoscaling (scale-down limit).\n\n- **Omitted:**\n  - On `CREATE`: defaults to the lower of the processor `tier` and the workspace default tier (there is no current bound to preserve).\n  - On `MODIFY` or `:startWith`: the current bound is preserved.\n- **`null`** on `CREATE`, `MODIFY`, or `:startWith`: resets the bound to the lower of the processor `tier` and the workspace default tier.\n- **A tier value** on `CREATE`, `MODIFY`, or `:startWith`: sets the bound to that tier.")
