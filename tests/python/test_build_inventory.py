from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location

import pytest


def load_module(path: Path):
    spec = spec_from_file_location("build_inventory", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_inventory_classifies_problem_paper_and_attachment(tmp_path):
    (tmp_path / "2024试题" / "A题").mkdir(parents=True)
    (tmp_path / "2024试题" / "A题" / "A题.pdf").write_bytes(b"%PDF")
    (tmp_path / "2024试题" / "A题" / "附件.xlsx").write_bytes(b"PK")
    (tmp_path / "2024优秀论文").mkdir()
    (tmp_path / "2024优秀论文" / "A016.pdf").write_bytes(b"%PDF")
    module = load_module(Path(".agents/skills/cumcm/scripts/build_inventory.py"))
    rows = module.build_inventory(tmp_path)
    assert [row["kind"] for row in rows] == ["problem", "attachment", "paper"]
    assert {row["year"] for row in rows} == {2024}
    assert {row["problem"] for row in rows} == {"A"}


def test_inventory_is_stable_and_excludes_generated_and_hidden_files(tmp_path):
    import hashlib

    source = tmp_path / "2022试题"
    source.mkdir()
    (source / "B题.pdf").write_bytes(b"problem")
    (source / "format2022.doc").write_bytes(b"format")
    for directory in ["corpus/inventory", ".git", ".worktrees/nested", "tests"]:
        target = tmp_path / directory
        target.mkdir(parents=True)
        (target / "irrelevant.pdf").write_bytes(b"generated")
    (source / "linked.pdf").symlink_to(source / "B题.pdf")
    module = load_module(Path(".agents/skills/cumcm/scripts/build_inventory.py"))
    rows = module.build_inventory(tmp_path)
    assert rows == module.build_inventory(tmp_path)
    assert [row["path"] for row in rows] == ["2022试题/B题.pdf", "2022试题/format2022.doc"]
    assert rows[0]["size_bytes"] == 7
    assert rows[0]["sha256"] == hashlib.sha256(b"problem").hexdigest()
    assert rows[1]["kind"] == "other"
    assert rows[1]["problem"] is None


@pytest.mark.parametrize("relative, expected", [
    ("2024优秀论文/2024A 基于几何模型的板凳龙运动路径问题.pdf", (2024, "A", "paper")),
    ("cumcm2021/cumcm2021a/CUMCM2021-A.pdf", (2021, "A", "problem")),
    ("cumcm2020/cumcm2020a/2020A-炉温曲线.docx", (2020, "A", "problem")),
])
def test_identify_year_letter_filenames(relative, expected):
    module = load_module(Path(".agents/skills/cumcm/scripts/build_inventory.py"))
    assert module.identify(Path(relative)) == expected


@pytest.mark.parametrize("filename", ["2025A synthetic.pdf", "A016.pdf"])
def test_inventory_skips_holdout_paper_before_opening(tmp_path, monkeypatch, filename):
    paper = tmp_path / "2025优秀论文" / filename
    paper.parent.mkdir()
    paper.write_bytes(b"synthetic hold-out fixture")
    module = load_module(Path(".agents/skills/cumcm/scripts/build_inventory.py"))
    original_open = Path.open

    def guarded_open(path, *args, **kwargs):
        assert path != paper, "Hold-out paper content must not be opened"
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded_open)
    assert module.build_inventory(tmp_path) == []
