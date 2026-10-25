"""Generated model for EventViewForOrg. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.alert_audit import AlertAudit
from pyatlassdk.admin.models.alert_config_audit import AlertConfigAudit
from pyatlassdk.admin.models.api_user_event_view_for_org import ApiUserEventViewForOrg
from pyatlassdk.admin.models.atlas_resource_policy_audit_for_org import AtlasResourcePolicyAuditForOrg
from pyatlassdk.admin.models.billing_event_view_for_org import BillingEventViewForOrg
from pyatlassdk.admin.models.default_event_view_for_org import DefaultEventViewForOrg
from pyatlassdk.admin.models.nds_audit_view_for_org import NDSAuditViewForOrg
from pyatlassdk.admin.models.org_event_view_for_org import OrgEventViewForOrg
from pyatlassdk.admin.models.resource_event_view_for_org import ResourceEventViewForOrg
from pyatlassdk.admin.models.service_account_org_events import ServiceAccountOrgEvents
from pyatlassdk.admin.models.team_event import TeamEvent
from pyatlassdk.admin.models.user_event_view_for_org import UserEventViewForOrg

EventViewForOrg: TypeAlias = DefaultEventViewForOrg | AlertAudit | AlertConfigAudit | ApiUserEventViewForOrg | ServiceAccountOrgEvents | BillingEventViewForOrg | NDSAuditViewForOrg | OrgEventViewForOrg | TeamEvent | UserEventViewForOrg | ResourceEventViewForOrg | AtlasResourcePolicyAuditForOrg
