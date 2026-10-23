"""Generated model for FlexBackupSettings20241113. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class FlexBackupSettings20241113(BaseModel):
    """Flex backup configuration."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    enabled: bool | None = Field(default=None, description="Flag that indicates whether backups are performed for this flex cluster. Backup uses flex cluster backups.")
