"""Generated model for AuthenticationTrigger. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal
from pyatlassdk.app._enums import upper_case
from pyatlassdk.app.models.authentication_trigger_config import AuthenticationTriggerConfig
from pyatlassdk.app.models.authentication_trigger_event_processors import AuthenticationTriggerEventProcessors

from pydantic import BaseModel, BeforeValidator, ConfigDict, Field

class AuthenticationTrigger(BaseModel):
    """Generated model for AuthenticationTrigger."""
    model_config = ConfigDict(populate_by_name=True, extra="allow")
    name: str = Field(description="The trigger's name.")
    type: Annotated[Literal["AUTHENTICATION"], BeforeValidator(upper_case)] = Field(description="The trigger type. For authentication triggers, this value is always `\"AUTHENTICATION\"`.")
    disabled: bool | None = Field(default=None, description="If `true`, the trigger is disabled and does not listen for events or execute.")
    config: AuthenticationTriggerConfig
    function_id: str | None = Field(default=None, description="The ID of the function that the trigger calls when it fires.\n\nThis value is the same as `event_processors.FUNCTION.function_id`.\nYou can either define the value here or in `event_processors.FUNCTION.function_id`.\nThe App Services backend duplicates the value to the configuration location where you did not define it.\n\nFor example, if you define `function_id`, the backend duplicates it to `event_processors.FUNCTION.function_id`.\n\nIf you define `function_id`, `event_processors` is not required. You must provide either `function_id` or\n`event_processors` when updating a trigger.")
    function_name: str | None = Field(default=None, description="The name of the function that the trigger calls when it\nfires, i.e. the function described by `function_id`.\n\nThis value is the same as `event_processors.FUNCTION.function_name`.\nYou can either define the value here or in `event_processors.FUNCTION.function_name`.\nThe App Services backend duplicates the value to the configuration location where you did not define it.\n\nFor example, if you define `function_name`, the backend duplicates it to `event_processors.FUNCTION.function_name`.\n\nIf you define `function_name`, `event_processors` is not required. You must provide either `function_name` or\n`event_processors` when updating a trigger.")
    event_processors: AuthenticationTriggerEventProcessors = Field(description="An object where each field name is an event processor ID and\neach value is an object that configures its corresponding\nevent processor. For an example configuration object, see\n[Send Trigger Events to AWS\nEventBridge](https://www.mongodb.com/docs/atlas/app-services/triggers/aws-eventbridge#std-label-event_processor_example).")
