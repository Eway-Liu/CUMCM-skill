from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path


def load_function(module_name: str, path: str, function_name: str):
    spec = spec_from_file_location(module_name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


def test_missing_source_and_evidence_label_are_errors(tmp_path):
    validate_card = load_function(
        "validate_corpus",
        ".agents/skills/cumcm/scripts/validate_corpus.py",
        "validate_card",
    )
    card = tmp_path / "paper.md"
    card.write_text("# Card\nModel: ARIMA\n", encoding="utf-8")
    errors = validate_card(card)
    joined = " ".join(errors)
    assert "source_evidence" in joined
    assert "evidence label" in joined


def test_paper_card_requires_explicit_question_records_and_transfer_fields(tmp_path):
    validate_card = load_function(
        "validate_corpus_question_schema",
        ".agents/skills/cumcm/scripts/validate_corpus.py",
        "validate_card",
    )
    card = tmp_path / "paper-cards" / "paper.md"
    card.parent.mkdir()
    card.write_text(
        "---\nid: paper\nyear: 2024\nproblem: C\n"
        "source_evidence: [ev-paper]\n---\n"
        "# Card\n[observed] source\n",
        encoding="utf-8",
    )
    joined = " ".join(validate_card(card))
    assert "missing heading ## Structured question records" in joined
    assert "missing heading ## Strong Points" in joined
    assert "missing heading ## Weak Points" in joined
    assert "missing heading ## Transferable Patterns" in joined
    assert "missing heading ## Problem-Specific Tricks" in joined
    assert "missing structured question Q1" in joined
    assert "missing structured question Q2" in joined
    assert "missing structured question Q3" in joined


def test_corpus_rejects_duplicate_ids_broken_sources_and_2025a_solutions(tmp_path):
    validate_corpus = load_function(
        "validate_corpus_full",
        ".agents/skills/cumcm/scripts/validate_corpus.py",
        "validate_corpus",
    )
    corpus = tmp_path / "corpus"
    cards = corpus / "paper-cards"
    cards.mkdir(parents=True)
    body = (
        "---\nid: duplicate\nyear: 2024\nproblem: A\n"
        "source_evidence: [ev-paper]\n---\n# Card\n"
        "## Source and evidence quality\n[observed] source\n"
        "## Subproblem objectives and dependencies\n[observed] q\n"
        "## Assumptions, data, and preprocessing\n[observed] data\n"
        "## Baseline, model, and algorithm\n[inferred] model\n"
        "## Validation, sensitivity/robustness, and figure purposes\n"
        "[expert-rule] validate\n"
        "## Reported results, strengths, limitations, and transferable rules\n"
        "[unverified] result\n"
    )
    (cards / "one.md").write_text(body, encoding="utf-8")
    (cards / "two.md").write_text(body, encoding="utf-8")
    records = [
        {
            "evidence_id": "ev-paper",
            "year": 2024,
            "problem": "A",
            "source_class": "local-paper-pdf",
            "local_path": "missing.pdf",
            "label": "observed",
        },
        {
            "evidence_id": "ev-2025-a-solution",
            "year": 2025,
            "problem": "A",
            "source_class": "solution-paper",
            "label": "observed",
        },
    ]
    (corpus / "evidence-ledger.jsonl").write_text(
        "".join(json.dumps(row) + "\n" for row in records), encoding="utf-8"
    )
    errors = validate_corpus(corpus)
    joined = " ".join(errors)
    assert "duplicate card id" in joined
    assert "broken local path" in joined
    assert "forbidden 2025 A solution evidence" in joined
