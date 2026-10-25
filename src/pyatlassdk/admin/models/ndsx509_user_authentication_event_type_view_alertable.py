"""Generated model for NDSX509UserAuthenticationEventTypeViewAlertable. Do not edit manually."""

from __future__ import annotations

from pyatlassdk.admin._enums import CaseInsensitiveEnum

class NDSX509UserAuthenticationEventTypeViewAlertable(CaseInsensitiveEnum):
    """Event type that triggers an alert."""
    NDS_X509_USER_AUTHENTICATION_CUSTOMER_CA_EXPIRATION_CHECK = "NDS_X509_USER_AUTHENTICATION_CUSTOMER_CA_EXPIRATION_CHECK"
    NDS_X509_USER_AUTHENTICATION_CUSTOMER_CRL_EXPIRATION_CHECK = "NDS_X509_USER_AUTHENTICATION_CUSTOMER_CRL_EXPIRATION_CHECK"
    NDS_X509_USER_AUTHENTICATION_MANAGED_USER_CERTS_EXPIRATION_CHECK = "NDS_X509_USER_AUTHENTICATION_MANAGED_USER_CERTS_EXPIRATION_CHECK"
