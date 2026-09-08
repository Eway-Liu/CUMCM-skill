from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest


def load_module(name: str, path: str):
    spec = spec_from_file_location(name, Path(path))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_time_split_is_chronological_and_disjoint():
    module = load_module(
        "validation_utils",
        ".agents/skills/cumcm-modeling/scripts/validation_utils.py",
    )
    train, validation, test = module.time_split(
        10, train_fraction=0.6, validation_fraction=0.2
    )
    assert train == list(range(6))
    assert validation == [6, 7]
    assert test == [8, 9]
    assert max(train) < min(validation) < min(test)


def test_metrics_constraints_and_perturbations_are_deterministic():
    module = load_module(
        "validation_utils_values",
        ".agents/skills/cumcm-modeling/scripts/validation_utils.py",
    )
    metrics = module.regression_metrics([1.0, 2.0], [1.0, 3.0])
    assert metrics["mae"] == 0.5
    assert metrics["rmse"] == 2 ** -0.5
    violations = module.constraint_violations(
        iter([-1.0, 0.5, 3.0]), lower=0.0, upper=2.0
    )
    assert violations == {
        "lower_count": 1,
        "upper_count": 1,
        "max_violation": 1.0,
    }
    assert module.perturbation_grid(100.0, [-0.1, 0.0, 0.1]) == [90.0, 100.0, 110.0]


def test_invalid_inputs_raise_clear_errors():
    module = load_module(
        "validation_utils_errors",
        ".agents/skills/cumcm-modeling/scripts/validation_utils.py",
    )
    with pytest.raises(ValueError, match="fractions"):
        module.time_split(10, 0.9, 0.2)
    with pytest.raises(ValueError, match="same length"):
        module.regression_metrics([1.0], [1.0, 2.0])
