"""Generated model for DataExplorerAccessedEventTypeView. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class DataExplorerAccessedEventTypeView(str, Enum):
    """Unique identifier of event type."""
    DATA_EXPLORER = "DATA_EXPLORER"
    DATA_EXPLORER_CRUD_ATTEMPT = "DATA_EXPLORER_CRUD_ATTEMPT"
    DATA_EXPLORER_CRUD_ERROR = "DATA_EXPLORER_CRUD_ERROR"
    DATA_EXPLORER_CRUD = "DATA_EXPLORER_CRUD"
