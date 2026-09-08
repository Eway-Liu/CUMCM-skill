from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path

import pandas as pd


def load_module(name: str, path: str):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_profile_frame_reports_shape_missing_and_duplicates():
    module = load_module(
        "data_profile", ".agents/skills/cumcm-modeling/scripts/data_profile.py"
    )
    frame = pd.DataFrame({"x": [1.0, None, 1.0], "label": ["a", "b", "a"]})
    result = module.profile_frame(frame)
    assert result["shape"] == [3, 2]
    assert result["missing"] == {"x": 1, "label": 0}
    assert result["duplicate_rows"] == 1
    assert result["dtypes"]["x"] == "float64"
    assert result["dtypes"]["label"] in {"object", "str", "string"}


def test_profile_is_strict_json_when_numeric_columns_are_empty():
    module = load_module(
        "data_profile_json", ".agents/skills/cumcm-modeling/scripts/data_profile.py"
    )
    result = module.profile_frame(pd.DataFrame({"x": [None, None]}).astype({"x": "float64"}))
    assert result["numeric_summary"]["x"]["mean"] is None
    json.dumps(result, allow_nan=False)
