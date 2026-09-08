#!/usr/bin/env python3
"""Validate CUMCM corpus cards, evidence links, and hold-out boundaries."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path


LABEL_RE = re.compile(r"\[(observed|inferred|expert-rule|unverified)\]|Evidence:\s*(observed|inferred|expert-rule|unverified)", re.I)
PAPER_HEADINGS = (
    "## Source and evidence quality",
    "## Subproblem objectives and dependencies",
    "## Assumptions, data, and preprocessing",
    "## Baseline, model, and algorithm",
    "## Validation, sensitivity/robustness, and figure purposes",
    "## Reported results, strengths, limitations, and transferable rules",
)
PROBLEM_HEADINGS = (
    "## Reality and deliverable",
    "## Questions and dependencies",
    "## Inputs, outputs, variables, parameters",
    "## Objectives, constraints, initial and boundary conditions",
    "## Data structure and file schema",
    "## Mathematical structure tags",
    "## Candidate validation evidence",
    "## Extraction limitations",
)


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
            result[key.strip()] = [item.strip().strip("'\"") for item in value[1:-1].split(",") if item.strip()]
        elif value.isdigit():
            result[key.strip()] = int(value)
        else:
            result[key.strip()] = value.strip("'\"")
    return result


def validate_card(path: Path) -> list[str]:
    text = Path(path).read_text(encoding="utf-8")
    meta = _frontmatter(text)
    errors: list[str] = []
    if not meta.get("id"):
        errors.append(f"{path}: missing id")
    if not meta.get("source_evidence"):
        errors.append(f"{path}: missing source_evidence")
    if not LABEL_RE.search(text):
        errors.append(f"{path}: missing evidence label")
    expected = PAPER_HEADINGS if "paper-cards" in path.parts else PROBLEM_HEADINGS if "problem-cards" in path.parts else ()
    for heading in expected:
        if heading not in text:
            errors.append(f"{path}: missing heading {heading}")
    return errors


def _paths(record: dict[str, object]) -> list[str]:
    result: list[str] = []
    if isinstance(record.get("local_path"), str):
        result.append(str(record["local_path"]))
    if isinstance(record.get("local_paths"), list):
        result.extend(str(item) for item in record["local_paths"])
    if isinstance(record.get("files"), list):
        result.extend(str(item["path"]) for item in record["files"] if isinstance(item, dict) and "path" in item)
    return result


def validate_corpus(corpus_dir: Path) -> list[str]:
    corpus_dir = Path(corpus_dir)
    errors: list[str] = []
    cards = sorted((corpus_dir / "problem-cards").glob("*.md")) + sorted((corpus_dir / "paper-cards").glob("*.md"))
    metadata: list[tuple[Path, dict[str, object]]] = []
    for card in cards:
        errors.extend(validate_card(card))
        metadata.append((card, _frontmatter(card.read_text(encoding="utf-8"))))
    for card_id, count in Counter(str(meta.get("id")) for _, meta in metadata if meta.get("id")).items():
        if count > 1:
            errors.append(f"duplicate card id: {card_id}")

    ledger_path = corpus_dir / "evidence-ledger.jsonl"
    records: list[dict[str, object]] = []
    if not ledger_path.exists():
        errors.append(f"missing evidence ledger: {ledger_path}")
    else:
        for number, line in enumerate(ledger_path.read_text(encoding="utf-8").splitlines(), 1):
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                errors.append(f"{ledger_path}:{number}: invalid JSON: {exc.msg}")

    evidence_ids = [str(record.get("evidence_id")) for record in records if record.get("evidence_id")]
    evidence_set = set(evidence_ids)
    for evidence_id, count in Counter(evidence_ids).items():
        if count > 1:
            errors.append(f"duplicate evidence id: {evidence_id}")
    for card, meta in metadata:
        refs = meta.get("source_evidence", [])
        if not isinstance(refs, list):
            refs = [refs]
        for ref in refs:
            if str(ref) not in evidence_set:
                errors.append(f"{card}: unknown source evidence {ref}")

    workspace = corpus_dir.parent
    for record in records:
        evidence_id = str(record.get("evidence_id", "<unknown>"))
        for local_path in _paths(record):
            if not (workspace / local_path).is_file():
                errors.append(f"{evidence_id}: broken local path {local_path}")
        if record.get("year") == 2025 and str(record.get("problem", "")).upper() == "A":
            source_class = str(record.get("source_class", "")).lower()
            identity = " ".join((evidence_id, source_class, str(record.get("title", "")))).lower()
            allowed = source_class in {"problem-statement", "problem-attachment", "attachment-metadata"}
            if not allowed or any(term in identity for term in ("solution", "review", "excellent-paper", "解答", "讲评", "优秀论文")):
                errors.append(f"forbidden 2025 A solution evidence: {evidence_id}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", type=Path)
    args = parser.parse_args()
    errors = validate_corpus(args.corpus)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("corpus validation: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
