"""Generated model for ThirdPartyIntegration. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.datadog import Datadog
from pyatlassdk.models.microsoft_teams import MicrosoftTeams
from pyatlassdk.models.new_relic import NewRelic
from pyatlassdk.models.ops_genie import OpsGenie
from pyatlassdk.models.pager_duty import PagerDuty
from pyatlassdk.models.prometheus import Prometheus
from pyatlassdk.models.slack import Slack
from pyatlassdk.models.victor_ops import VictorOps
from pyatlassdk.models.webhook import Webhook

ThirdPartyIntegration: TypeAlias = PagerDuty | Slack | Datadog | NewRelic | OpsGenie | VictorOps | Webhook | Prometheus | MicrosoftTeams
