"""Generated model for OrgUserResponse. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.org_active_user_response import OrgActiveUserResponse
from pyatlassdk.admin.models.org_pending_user_response import OrgPendingUserResponse

OrgUserResponse: TypeAlias = OrgPendingUserResponse | OrgActiveUserResponse
