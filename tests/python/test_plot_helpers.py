from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import matplotlib
import pytest

matplotlib.use("Agg")


def load_module(name: str, path: str):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_style_save_and_axis_units(tmp_path):
    style = load_module(
        "plot_style", ".agents/skills/cumcm-visualization/scripts/plot_style.py"
    )
    helpers = load_module(
        "plot_helpers", ".agents/skills/cumcm-visualization/scripts/plot_helpers.py"
    )
    settings = style.paper_style()
    assert settings["figure.dpi"] == 150
    assert settings["savefig.dpi"] >= 300
    fig, ax = helpers.actual_vs_predicted(
        [1, 2], [1.1, 1.9], variable="Thickness", unit="um"
    )
    assert ax.get_xlabel() == "Actual Thickness (um)"
    assert ax.get_ylabel() == "Predicted Thickness (um)"
    outputs = helpers.save_figure(
        fig, tmp_path / "comparison", formats=("png", "pdf")
    )
    assert {path.suffix for path in outputs} == {".png", ".pdf"}
    assert all(path.exists() for path in outputs)


def test_actual_vs_predicted_rejects_shape_mismatch():
    helpers = load_module(
        "plot_helpers_errors",
        ".agents/skills/cumcm-visualization/scripts/plot_helpers.py",
    )
    with pytest.raises(ValueError, match="same length"):
        helpers.actual_vs_predicted([1, 2], [1], variable="y", unit="m")

