#!/usr/bin/env python3
"""Print Atlas Performance Advisor index suggestions as a Markdown table.

The SDK loads the nearest ``.env`` file automatically. Provide Atlas API
credentials and the target project/cluster through environment variables:

    MONGO_ATLAS_PUBLIC_KEY=...
    MONGO_ATLAS_PRIVATE_KEY=...
    MONGO_ATLAS_GROUP_ID=...
    MONGO_ATLAS_CLUSTER_NAME=...

``MONGO_ATLAS_GROUP_ID`` and ``MONGO_ATLAS_CLUSTER_NAME`` can be overridden
with ``--group-id`` and ``--cluster-name``.
"""

from __future__ import annotations

import argparse
import json
import os
from collections.abc import Mapping, Sequence
from typing import Any

from pyatlassdk import AtlasAdminClient
from pyatlassdk.admin.models.performance_advisor_index import PerformanceAdvisorIndex


def _escape(value: object) -> str:
    """Make a value safe for a Markdown table cell."""
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def _format_index(index: Sequence[Mapping[str, int]] | None) -> str:
    if not index:
        return ""
    fields = [f"{field}: {direction}" for item in index for field, direction in item.items()]
    return ", ".join(fields)


def _format_weight(weight: float | None) -> str:
    if weight is None:
        return ""
    return f"{weight:g}"


def _format_size(size: float | None) -> str:
    if size is None:
        return ""
    return f"{size:,.0f} B"


def _format_collation(collation: dict[str, Any] | None) -> str:
    if not collation:
        return "default"
    return json.dumps(collation, sort_keys=True, separators=(",", ":"))


def render_markdown(suggestions: list[PerformanceAdvisorIndex]) -> str:
    """Render suggestions as a GitHub-flavored Markdown table."""
    lines = [
        "| Namespace | Impact | Suggested index | Avg object size | Collation |",
        "| --- | ---: | --- | ---: | --- |",
    ]
    for suggestion in suggestions:
        index = _format_index(suggestion.index)
        index_cell = f"`{_escape(index)}`" if index else ""
        collation = _format_collation(suggestion.collation)
        lines.append(
            f"| {_escape(suggestion.namespace)} "
            f"| {_format_weight(suggestion.weight)} "
            f"| {index_cell} "
            f"| {_format_size(suggestion.avg_obj_size)} "
            f"| `{_escape(collation)}` |"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print Atlas Performance Advisor index suggestions as Markdown.",
    )
    parser.add_argument(
        "--group-id",
        default=os.getenv("MONGO_ATLAS_GROUP_ID"),
        help="Atlas project/group ID (default: MONGO_ATLAS_GROUP_ID).",
    )
    parser.add_argument(
        "--cluster-name",
        default=os.getenv("MONGO_ATLAS_CLUSTER_NAME"),
        help="Atlas cluster name (default: MONGO_ATLAS_CLUSTER_NAME).",
    )
    args = parser.parse_args()

    if not args.group_id or not args.cluster_name:
        parser.error(
            "set MONGO_ATLAS_GROUP_ID and MONGO_ATLAS_CLUSTER_NAME "
            "or pass --group-id and --cluster-name"
        )

    with AtlasAdminClient() as client:
        if client.auth_mode == "anonymous":
            parser.error(
                "no Atlas credentials found; set MONGO_ATLAS_PUBLIC_KEY and "
                "MONGO_ATLAS_PRIVATE_KEY (or OAuth service account variables)"
            )
        response = (
            client.performance_advisor.list_group_cluster_performance_advisor_suggested_indexes(
                cluster_name=args.cluster_name,
                group_id=args.group_id,
            )
        )

    suggestions = response.content.suggested_indexes or []
    if not suggestions:
        print("_No index suggestions returned by Performance Advisor._")
        return 0
    print(render_markdown(suggestions))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
