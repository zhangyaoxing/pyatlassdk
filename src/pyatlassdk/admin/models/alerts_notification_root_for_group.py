"""Generated model for AlertsNotificationRootForGroup. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.datadog_notification import DatadogNotification
from pyatlassdk.admin.models.email_notification import EmailNotification
from pyatlassdk.admin.models.group_notification import GroupNotification
from pyatlassdk.admin.models.hip_chat_notification import HipChatNotification
from pyatlassdk.admin.models.microsoft_teams_notification import MicrosoftTeamsNotification
from pyatlassdk.admin.models.ops_genie_notification import OpsGenieNotification
from pyatlassdk.admin.models.org_notification import OrgNotification
from pyatlassdk.admin.models.pager_duty_notification import PagerDutyNotification
from pyatlassdk.admin.models.sms_notification import SMSNotification
from pyatlassdk.admin.models.slack_notification import SlackNotification
from pyatlassdk.admin.models.team_notification import TeamNotification
from pyatlassdk.admin.models.user_notification import UserNotification
from pyatlassdk.admin.models.victor_ops_notification import VictorOpsNotification
from pyatlassdk.admin.models.webhook_notification import WebhookNotification

AlertsNotificationRootForGroup: TypeAlias = DatadogNotification | EmailNotification | GroupNotification | HipChatNotification | MicrosoftTeamsNotification | OpsGenieNotification | OrgNotification | PagerDutyNotification | SlackNotification | SMSNotification | TeamNotification | UserNotification | VictorOpsNotification | WebhookNotification
