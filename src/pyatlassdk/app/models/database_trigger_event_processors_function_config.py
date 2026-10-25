"""Generated model for DatabaseTriggerEventProcessorsFUNCTIONConfig. Do not edit manually."""

from __future__ import annotations

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTriggerEventProcessorsFUNCTIONConfig(BaseModel):
    """Generated model for DatabaseTriggerEventProcessorsFUNCTIONConfig."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    function_id: str | None = Field(default=None, description="The ID of the function that the trigger calls when it fires.\n\nThis value is the same as the root-level `function_id`.\nYou can either define the value here or in `function_id`.\nThe App Services backend duplicates the value to the configuration location where you did not define it.\n\nFor example, if you define `event_processors.FUNCTION.function_id`, the backend duplicates it to `function_id`.\n\nIf you define `function_id`, `event_processors` is not required. You must provide either `function_id` or\n`event_processors` when updating a trigger.")
    function_name: str | None = Field(default=None, description="The name of the function that the trigger calls when it\nfires, i.e. the function described by `function_id`.\n\nThis value is the same as the root-level `function_name`.\nYou can either define the value here or in `function_name`.\nThe App Services backend duplicates the value to the configuration location where you did not define it.\n\nFor example, if you define `event_processors.FUNCTION.function_name`, the backend duplicates it to `function_name`.\n\nIf you define `function_name`, `event_processors` is not required. You must provide either `function_name` or\n`event_processors` when updating a trigger.")
