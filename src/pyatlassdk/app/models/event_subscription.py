"""Generated model for EventSubscription. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.app.models.event_subscription_variant2 import EventSubscriptionVariant2
from pyatlassdk.app.models.trigger import Trigger

EventSubscription: TypeAlias = Trigger | EventSubscriptionVariant2
