from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_function(module_name: str, path: str, function_name: str):
    spec = spec_from_file_location(module_name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, function_name)


def write_card(path: Path, body: str) -> None:
    path.write_text(body, encoding="utf-8")


def test_structure_terms_outweigh_topic_words(tmp_path):
    search_cards = load_function(
        "search_cases",
        ".agents/skills/cumcm/scripts/search_cases.py",
        "search_cards",
    )
    write_card(
        tmp_path / "a.md",
        "---\ntags: [small-sample, nonlinear, regression]\n"
        "source_evidence: [e1]\n---\n# A\nEvidence: observed\n"
        "Validation: leave-one-out",
    )
    write_card(
        tmp_path / "b.md",
        "---\ntags: [image, deep-learning]\nsource_evidence: [e2]\n"
        "---\n# B\nEvidence: observed\nValidation: holdout\n"
        "small sample nonlinear prediction small sample nonlinear prediction",
    )
    results = search_cards(tmp_path, "small sample nonlinear prediction", top=1)
    assert results[0]["path"].endswith("a.md")
    assert results[0]["evidence_ids"] == ["e1"]


def test_chinese_structure_synonyms_match_tags(tmp_path):
    search_cards = load_function(
        "search_cases_cn",
        ".agents/skills/cumcm/scripts/search_cases.py",
        "search_cards",
    )
    write_card(
        tmp_path / "optimization.md",
        "---\nid: opt\ntags: [mixed-integer, constrained-optimization, uncertainty]\n"
        "source_evidence: [ev-opt]\n---\n# Optimization\n"
        "## Validation\nfeasibility and scenario checks",
    )
    results = search_cards(tmp_path, "整数 决策变量 约束 不确定性", top=3)
    assert results[0]["id"] == "opt"
    assert results[0]["score"] > 0
