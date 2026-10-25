"""Generated model for FilterConstructor. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.app.models.expression import Expression
from pyatlassdk.app.models.projection import Projection
from pyatlassdk.app.models.query import Query

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FilterConstructor(BaseModel):
    """A filter that conditionally modifies incoming query operations before they run."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str | None = Field(default=None, description="The filter's name.")
    apply_when: Expression | None = Field(default=None, description="A rule expression that evaluates to `true` if the filter applies to an incoming query.")
    query: Query | None = Field(default=None, description="A MongoDB query object that is merged into an incoming query before the operation runs.")
    projection: Projection | None = Field(default=None, description="A MongoDB projection object that is merged into an incoming query before the operation runs.")
