"""Generated model for EventViewForOrg. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.alert_audit import AlertAudit
from pyatlassdk.models.alert_config_audit import AlertConfigAudit
from pyatlassdk.models.api_user_event_view_for_org import ApiUserEventViewForOrg
from pyatlassdk.models.atlas_resource_policy_audit_for_org import AtlasResourcePolicyAuditForOrg
from pyatlassdk.models.billing_event_view_for_org import BillingEventViewForOrg
from pyatlassdk.models.default_event_view_for_org import DefaultEventViewForOrg
from pyatlassdk.models.nds_audit_view_for_org import NDSAuditViewForOrg
from pyatlassdk.models.org_event_view_for_org import OrgEventViewForOrg
from pyatlassdk.models.resource_event_view_for_org import ResourceEventViewForOrg
from pyatlassdk.models.service_account_org_events import ServiceAccountOrgEvents
from pyatlassdk.models.team_event import TeamEvent
from pyatlassdk.models.user_event_view_for_org import UserEventViewForOrg

EventViewForOrg: TypeAlias = DefaultEventViewForOrg | AlertAudit | AlertConfigAudit | ApiUserEventViewForOrg | ServiceAccountOrgEvents | BillingEventViewForOrg | NDSAuditViewForOrg | OrgEventViewForOrg | TeamEvent | UserEventViewForOrg | ResourceEventViewForOrg | AtlasResourcePolicyAuditForOrg
