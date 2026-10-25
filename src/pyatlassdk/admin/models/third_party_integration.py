"""Generated model for ThirdPartyIntegration. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.datadog import Datadog
from pyatlassdk.admin.models.microsoft_teams import MicrosoftTeams
from pyatlassdk.admin.models.new_relic import NewRelic
from pyatlassdk.admin.models.ops_genie import OpsGenie
from pyatlassdk.admin.models.pager_duty import PagerDuty
from pyatlassdk.admin.models.prometheus import Prometheus
from pyatlassdk.admin.models.slack import Slack
from pyatlassdk.admin.models.victor_ops import VictorOps
from pyatlassdk.admin.models.webhook import Webhook

ThirdPartyIntegration: TypeAlias = PagerDuty | Slack | Datadog | NewRelic | OpsGenie | VictorOps | Webhook | Prometheus | MicrosoftTeams
