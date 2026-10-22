"""Generated model for MatcherFieldView. Do not edit manually."""

from __future__ import annotations

from typing import Literal, TypeAlias

MatcherFieldView: TypeAlias = Literal["APPLICATION_ID"] | Literal["CLUSTER_NAME"] | Literal["TYPE_NAME", "HOSTNAME", "PORT", "HOSTNAME_AND_PORT", "REPLICA_SET_NAME", "ATLAS_NODE_TYPE"] | Literal["REPLICA_SET_NAME", "SHARD_NAME", "CLUSTER_NAME"] | Literal["INSTANCE_NAME", "PROCESSOR_NAME"] | Literal["RULE_ID"] | Literal["SOFTWARE_TYPE"]
