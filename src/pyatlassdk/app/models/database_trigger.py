"""Generated model for DatabaseTrigger. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.app._enums import upper_case
from pyatlassdk.app.models.database_trigger_config import DatabaseTriggerConfig
from pyatlassdk.app.models.database_trigger_error_handler import DatabaseTriggerErrorHandler
from pyatlassdk.app.models.database_trigger_event_processors import DatabaseTriggerEventProcessors

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class DatabaseTrigger(BaseModel):
    """Generated model for DatabaseTrigger."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="The trigger's name.")
    type: Annotated[Literal["DATABASE"], BeforeValidator(upper_case)] = Field(description="The trigger type. For database triggers, this value is always `\"DATABASE\"`.")
    disabled: bool | None = Field(default=None, description="If `true`, the trigger is disabled and does not listen for events or execute.")
    config: DatabaseTriggerConfig
    function_id: str | None = Field(default=None, description="The ID of the function that the trigger calls when it fires.\n\nThis value is the same as `event_processors.FUNCTION.function_id`.\nYou can either define the value here or in `event_processors.FUNCTION.function_id`.\nThe App Services backend duplicates the value to the configuration location where you did not define it.\n\nFor example, if you define `function_id`, the backend duplicates it to `event_processors.FUNCTION.function_id`.\n\nIf you define `function_id`, `event_processors` is not required. You must provide either `function_id` or\n`event_processors` when updating a trigger.")
    function_name: str | None = Field(default=None, description="The name of the function that the trigger calls when it\nfires, i.e. the function described by `function_id`.\n\nThis value is the same as `event_processors.FUNCTION.function_name`.\nYou can either define the value here or in `event_processors.FUNCTION.function_name`.\nThe App Services backend duplicates the value to the configuration location where you did not define it.\n\nFor example, if you define `function_name`, the backend duplicates it to `event_processors.FUNCTION.function_name`.\n\nIf you define `function_name`, `event_processors` is not required. You must provide either `function_name` or\n`event_processors` when updating a trigger.")
    event_processors: DatabaseTriggerEventProcessors = Field(description="An object where each field name is an event processor ID and\neach value is an object that configures its corresponding\nevent processor. For an example configuration object, see\n[Send Trigger Events to AWS\nEventBridge](https://www.mongodb.com/docs/atlas/app-services/triggers/aws-eventbridge#std-label-event_processor_example).")
    error_handler: DatabaseTriggerErrorHandler | None = Field(default=None, description="An object that defines custom error handling for an AWS \nEventBridge trigger. Valid only for `\"DATABASE\"` type triggers \nwith `\"AWS_EVENTBRIDGE\"` event processors. ")
