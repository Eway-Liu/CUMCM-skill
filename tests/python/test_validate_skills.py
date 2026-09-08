from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_module(name: str, path: str):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_suite_validator_reports_broken_contracts(tmp_path):
    module = load_module(
        "validate_skills", ".agents/skills/cumcm/scripts/validate_skills.py"
    )
    repeated = (
        "Detailed XGBoost tutorial duplicated across specialist skills with enough "
        "words to represent misplaced detailed knowledge."
    )
    for name in (
        "cumcm-global",
        "cumcm-modeling",
        "cumcm-visualization",
        "cumcm-thesis",
    ):
        folder = tmp_path / name
        folder.mkdir()
        folder.joinpath("SKILL.md").write_text(
            f"---\nname: {name}\ndescription: bad\n---\n# Placeholder\n"
            "See [missing](references/missing.md).\n"
            "Run `scripts/missing.py`.\n"
            f"{repeated}\n",
            encoding="utf-8",
        )
    errors = module.validate_suite(tmp_path)
    joined = "\n".join(errors)
    assert "description" in joined
    assert "broken reference" in joined
    assert "broken artifact" in joined
    assert "scaffold marker" in joined
    assert "duplicated detailed knowledge" in joined


def test_suite_validator_accepts_minimal_valid_suite(tmp_path):
    module = load_module(
        "validate_skills_valid", ".agents/skills/cumcm/scripts/validate_skills.py"
    )
    for name in module.EXPECTED_SKILLS:
        folder = tmp_path / name
        (folder / "references").mkdir(parents=True)
        (folder / "references" / "guide.md").write_text("# Guide\n", encoding="utf-8")
        folder.joinpath("SKILL.md").write_text(
            f"---\nname: {name}\n"
            "description: Use when a mathematical modeling task needs this specialist.\n"
            "---\n# Entry\nSee [guide](references/guide.md).\n",
            encoding="utf-8",
        )
    assert module.validate_suite(tmp_path) == []


def test_global_routes_the_bidirectional_structure_model_index():
    entry = Path(".agents/skills/cumcm-global/SKILL.md").read_text(encoding="utf-8")
    index = Path(".agents/skills/cumcm/references/bidirectional-index.md")
    assert "../cumcm/references/bidirectional-index.md" in entry
    assert index.is_file()
    text = index.read_text(encoding="utf-8")
    assert "## Problem structure -> model families" in text
    assert "## Model family -> problem structures" in text
