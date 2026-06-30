"""Light sanity checks for preprocessing."""

from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from src.metrics import fracture_probability


def test_fracture_probability_bounds() -> None:
    assert 0.0 <= fracture_probability(-10.0) <= 1.0
    assert 0.0 <= fracture_probability(10.0) <= 1.0
    assert fracture_probability(0.0) == pytest.approx(0.5)


def test_fracture_probability_direction() -> None:
    assert fracture_probability(-5.0) > fracture_probability(5.0)


def test_discover_samples_empty_dir(tmp_path: Path) -> None:
    from src.data.dataset import discover_samples

    assert discover_samples(tmp_path) == []


def test_discover_samples_layout(tmp_path: Path) -> None:
    from src.data.dataset import discover_samples

    fractured = tmp_path / "fractured"
    normal = tmp_path / "non fractured"
    fractured.mkdir()
    normal.mkdir()
    Image.new("L", (64, 64), color=128).save(fractured / "fx.jpg")
    Image.new("L", (64, 64), color=200).save(normal / "ok.jpg")

    samples = discover_samples(tmp_path)
    assert len(samples) == 2
    labels = {s.path.name: s.label for s in samples}
    assert labels["fx.jpg"] == 0
    assert labels["ok.jpg"] == 1


def test_discover_samples_not_fractured_alias(tmp_path: Path) -> None:
    from src.data.dataset import discover_samples

    fractured = tmp_path / "fractured"
    normal = tmp_path / "not fractured"
    fractured.mkdir()
    normal.mkdir()
    Image.new("L", (64, 64), color=128).save(fractured / "fx.jpg")
    Image.new("L", (64, 64), color=200).save(normal / "ok.jpg")

    samples = discover_samples(tmp_path)
    assert len(samples) == 2
    labels = {s.path.name: s.label for s in samples}
    assert labels["fx.jpg"] == 0
    assert labels["ok.jpg"] == 1
