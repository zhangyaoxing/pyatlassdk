"""Generated model for SchemaRegistryAuthentication. Do not edit manually."""

from __future__ import annotations

from typing import TypeAlias
from pyatlassdk.models.confluent_sasl_inherit_authentication import ConfluentSaslInheritAuthentication
from pyatlassdk.models.confluent_user_info_authentication import ConfluentUserInfoAuthentication

SchemaRegistryAuthentication: TypeAlias = ConfluentUserInfoAuthentication | ConfluentSaslInheritAuthentication
