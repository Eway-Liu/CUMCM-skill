#!/usr/bin/env python3
"""Search evidence cards for each model stage and for their complete chain."""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
def _load_search_module():
    sibling = Path(__file__).with_name("search_cases.py")
    spec = importlib.util.spec_from_file_location("cumcm_search_cases", sibling)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {sibling}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_search_module = _load_search_module()
search_cards = _search_module.search_cards
_SUPPORT_CONCEPTS = {"constraints", "decision-variable", "validation", "sensitivity"}


def _anchored(rows: list[dict[str, object]], query: str) -> list[dict[str, object]]:
    """Reject hits supported only by generic validation or constraint language."""
    concepts = set(_search_module.CONCEPTS)
    anchors = (_search_module._tokens(query) & concepts) - _SUPPORT_CONCEPTS
    if not anchors:
        return rows
    return [
        row
        for row in rows
        if anchors & set(row.get("matched_structure_terms", []))
    ]


def search_chain(
    cards_dir: Path,
    stages: list[tuple[str, str]],
    chain_query: str | None = None,
    top: int = 6,
) -> dict[str, object]:
    """Keep per-stage evidence and return a deduplicated, provenance-tagged union."""
    if not stages:
        raise ValueError("at least one named stage is required")
    names = [name.strip() for name, _ in stages]
    if any(not name for name in names) or len(names) != len(set(names)):
        raise ValueError("stage names must be non-empty and unique")

    stage_results: dict[str, list[dict[str, object]]] = {}
    chain_results: list[dict[str, object]] = []
    union: dict[str, dict[str, object]] = {}

    def merge(rows: list[dict[str, object]], query_label: str) -> None:
        for row in rows:
            key = str(row.get("id") or row["path"])
            if key not in union:
                union[key] = {**row, "matched_queries": []}
            union[key]["score"] = max(
                int(union[key].get("score", 0)), int(row.get("score", 0))
            )
            labels = union[key]["matched_queries"]
            if query_label not in labels:
                labels.append(query_label)

    for (raw_name, query), name in zip(stages, names):
        rows = _anchored(search_cards(Path(cards_dir), query, top), query)
        stage_results[name] = rows
        merge(rows, f"stage:{name}")

    if chain_query and all(stage_results.values()):
        chain_results = _anchored(
            search_cards(Path(cards_dir), chain_query, top), chain_query
        )
        merge(chain_results, "chain")

    union_rows = sorted(
        union.values(), key=lambda row: (-int(row["score"]), str(row["path"]))
    )
    return {"stages": stage_results, "chain": chain_results, "union": union_rows}


def _stage(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("stage must be NAME=QUERY")
    name, query = (part.strip() for part in value.split("=", 1))
    if not name or not query:
        raise argparse.ArgumentTypeError("stage name and query must be non-empty")
    return name, query


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", action="append", type=_stage, required=True)
    parser.add_argument("--chain")
    parser.add_argument("--cards", type=Path, default=Path("corpus/paper-cards"))
    parser.add_argument("--top", type=int, default=6)
    args = parser.parse_args()
    result = search_chain(args.cards, args.stage, args.chain, args.top)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
