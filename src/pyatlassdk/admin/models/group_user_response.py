"""Generated model for GroupUserResponse. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.admin.models.group_active_user_response import GroupActiveUserResponse
from pyatlassdk.admin.models.group_pending_user_response import GroupPendingUserResponse

GroupUserResponse: TypeAlias = GroupPendingUserResponse | GroupActiveUserResponse
