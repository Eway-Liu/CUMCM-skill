from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location


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
