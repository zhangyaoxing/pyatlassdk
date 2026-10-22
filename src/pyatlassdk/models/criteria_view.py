"""Generated model for CriteriaView. Do not edit manually."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

class CriteriaView(BaseModel):
    """
    Rules by which MongoDB Cloud archives data.
    
    Use the `criteria.type` field to choose how MongoDB Cloud selects data to archive. Choose data using the age of the data or a MongoDB query.
    `"criteria.type": "DATE"` selects documents to archive based on a date.
    `"criteria.type": "CUSTOM"` selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support `"criteria.type": "CUSTOM"` when `"collectionType": "TIMESERIES"`.
    """
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    type: Literal["DATE", "CUSTOM"] | None = Field(default=None, description="Means by which MongoDB Cloud selects data to archive. Data can be chosen using the age of the data or a MongoDB query.\n`DATE` selects documents to archive based on a date.\n`CUSTOM` selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support `CUSTOM` when `\"collectionType\": \"TIMESERIES\"`.")
