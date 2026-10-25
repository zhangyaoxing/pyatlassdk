"""Generated model for ZoneMapping. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class ZoneMapping(BaseModel):
    """Human-readable label that identifies the subset of a global cluster."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    location: str = Field(description="Code that represents a location that maps to a zone in your global cluster. MongoDB Cloud represents this location with a ISO 3166-2 location and subdivision codes when possible.")
    zone: str = Field(description="Human-readable label that identifies the zone in your global cluster. This zone maps to a location code.")
