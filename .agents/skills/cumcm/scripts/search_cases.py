#!/usr/bin/env python3
"""Search CUMCM cards by mathematical structure, not topic-name lookup."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CONCEPTS = {
    "small-sample": ("small sample", "small-sample", "small_sample", "小样本"),
    "nonlinear": ("nonlinear", "non-linear", "非线性"),
    "prediction": ("prediction", "forecast", "regression", "预测", "回归"),
    "time-series": ("time series", "time-series", "时序", "时间序列"),
    "classification": ("classification", "分类"),
    "optimization": ("optimization", "optimisation", "优化", "规划"),
    "mixed-integer": ("mixed integer", "mixed-integer", "integer", "整数", "离散", "二进制"),
    "decision-variable": ("decision variable", "decision-variable", "决策变量"),
    "constraints": ("constraint", "constraints", "约束"),
    "uncertainty": ("uncertainty", "stochastic", "robust", "不确定性", "随机", "鲁棒"),
    "simulation": ("simulation", "monte carlo", "仿真", "模拟"),
    "geometry": ("geometry", "geometric", "几何"),
    "mechanism": ("mechanism", "physics", "differential equation", "机理", "物理", "微分方程"),
    "network": ("network", "graph", "路径", "网络", "图模型"),
    "evaluation": ("evaluation", "ranking", "评价", "排序"),
    "validation": ("validation", "cross validation", "验证", "检验"),
    "sensitivity": ("sensitivity", "敏感性"),
}


def _frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    result: dict[str, object] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            result[key.strip()] = [
                item.strip().strip("'\"")
                for item in value[1:-1].split(",")
                if item.strip()
            ]
        elif value.isdigit():
            result[key.strip()] = int(value)
        else:
            result[key.strip()] = value.strip("'\"")
    return result


def _tokens(text: str) -> set[str]:
    lowered = text.lower().replace("_", "-")
    tokens = set(re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", lowered))
    tokens.update(part for token in tuple(tokens) for part in token.split("-"))
    for concept, forms in CONCEPTS.items():
        if any(form in lowered for form in forms):
            tokens.add(concept)
    return tokens


def _structural_text(text: str) -> str:
    signals = (
        "structure", "objective", "constraint", "variable", "baseline",
        "validation", "sensitivity", "robustness", "mathematical",
        "结构", "目标", "约束", "变量", "验证", "敏感性", "鲁棒",
    )
    return "\n".join(
        line for line in text.splitlines()
        if line.startswith("##") or any(signal in line.lower() for signal in signals)
    )


def search_cards(cards_dir: Path, query: str, top: int = 6) -> list[dict[str, object]]:
    """Return evidence-bearing cards ranked by structure and data conditions."""
    query_tokens = _tokens(query)
    results: list[dict[str, object]] = []
    for path in sorted(Path(cards_dir).glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta = _frontmatter(text)
        tags = meta.get("tags", [])
        tag_text = " ".join(tags) if isinstance(tags, list) else str(tags)
        metadata_text = " ".join(str(meta.get(key, "")) for key in ("title", "problem", "year"))
        tag_matches = query_tokens & _tokens(tag_text)
        structure_matches = query_tokens & _tokens(_structural_text(text))
        metadata_matches = query_tokens & _tokens(metadata_text)
        body_matches = query_tokens & _tokens(text)
        score = (
            8 * len(tag_matches)
            + 4 * len(structure_matches - tag_matches)
            + 2 * len(metadata_matches - tag_matches - structure_matches)
            + len(body_matches - tag_matches - structure_matches - metadata_matches)
        )
        if score <= 0:
            continue
        evidence = meta.get("source_evidence", [])
        if not isinstance(evidence, list):
            evidence = [str(evidence)] if evidence else []
        results.append({
            "path": path.as_posix(),
            "id": meta.get("id", path.stem),
            "title": meta.get("title", path.stem),
            "year": meta.get("year"),
            "problem": meta.get("problem"),
            "score": score,
            "matched_structure_terms": sorted(tag_matches | structure_matches),
            "evidence_ids": evidence,
        })
    results.sort(key=lambda row: (-int(row["score"]), str(row["path"])))
    return results[: max(0, top)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--cards", type=Path, default=Path("corpus/paper-cards"))
    parser.add_argument("--top", type=int, default=6)
    args = parser.parse_args()
    print(json.dumps(search_cards(args.cards, args.query, args.top), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
