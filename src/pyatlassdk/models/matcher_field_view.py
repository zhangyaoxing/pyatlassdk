"""Generated model for MatcherFieldView. Do not edit manually."""

from __future__ import annotations

from typing import Annotated, Literal, TypeAlias
from pyatlassdk._enums import upper_case

from pydantic import BeforeValidator

MatcherFieldView: TypeAlias = Annotated[Literal["APPLICATION_ID"], BeforeValidator(upper_case)] | Annotated[Literal["CLUSTER_NAME"], BeforeValidator(upper_case)] | Annotated[Literal["TYPE_NAME", "HOSTNAME", "PORT", "HOSTNAME_AND_PORT", "REPLICA_SET_NAME", "ATLAS_NODE_TYPE"], BeforeValidator(upper_case)] | Annotated[Literal["REPLICA_SET_NAME", "SHARD_NAME", "CLUSTER_NAME"], BeforeValidator(upper_case)] | Annotated[Literal["INSTANCE_NAME", "PROCESSOR_NAME"], BeforeValidator(upper_case)] | Annotated[Literal["RULE_ID"], BeforeValidator(upper_case)] | Annotated[Literal["SOFTWARE_TYPE"], BeforeValidator(upper_case)]
