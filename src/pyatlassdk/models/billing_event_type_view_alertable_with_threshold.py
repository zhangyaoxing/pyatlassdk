"""Generated model for BillingEventTypeViewAlertableWithThreshold. Do not edit manually."""

from __future__ import annotations

from enum import Enum

class BillingEventTypeViewAlertableWithThreshold(str, Enum):
    """Event type that triggers an alert."""
    PENDING_INVOICE_OVER_THRESHOLD = "PENDING_INVOICE_OVER_THRESHOLD"
    DAILY_BILL_OVER_THRESHOLD = "DAILY_BILL_OVER_THRESHOLD"
    DAILY_BILLING_CHANGE_OVER_THRESHOLD = "DAILY_BILLING_CHANGE_OVER_THRESHOLD"
    WEEKLY_BILLING_CHANGE_OVER_THRESHOLD = "WEEKLY_BILLING_CHANGE_OVER_THRESHOLD"
    MONTHLY_BILLING_CHANGE_OVER_THRESHOLD = "MONTHLY_BILLING_CHANGE_OVER_THRESHOLD"
