"""Generated model for AlertsNotificationRootForGroup. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.datadog_notification import DatadogNotification
from pyatlassdk.models.email_notification import EmailNotification
from pyatlassdk.models.group_notification import GroupNotification
from pyatlassdk.models.hip_chat_notification import HipChatNotification
from pyatlassdk.models.microsoft_teams_notification import MicrosoftTeamsNotification
from pyatlassdk.models.ops_genie_notification import OpsGenieNotification
from pyatlassdk.models.org_notification import OrgNotification
from pyatlassdk.models.pager_duty_notification import PagerDutyNotification
from pyatlassdk.models.sms_notification import SMSNotification
from pyatlassdk.models.slack_notification import SlackNotification
from pyatlassdk.models.team_notification import TeamNotification
from pyatlassdk.models.user_notification import UserNotification
from pyatlassdk.models.victor_ops_notification import VictorOpsNotification
from pyatlassdk.models.webhook_notification import WebhookNotification

AlertsNotificationRootForGroup: TypeAlias = DatadogNotification | EmailNotification | GroupNotification | HipChatNotification | MicrosoftTeamsNotification | OpsGenieNotification | OrgNotification | PagerDutyNotification | SlackNotification | SMSNotification | TeamNotification | UserNotification | VictorOpsNotification | WebhookNotification
