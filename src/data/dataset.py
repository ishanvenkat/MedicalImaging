"""Dataset loaders for fracture detection."""

from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import tensorflow as tf

from PIL import Image

from src.config import Config

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png")


@dataclass
class Sample:
    path: Path
    label: int  # 0 = fractured, 1 = non fractured (alphabetical class order)


def _class_label(name: str) -> int:
    mapping = {
        "fractured": 0,
        "fracture": 0,
        "non fractured": 1,
        "not fractured": 1,
        "non_fractured": 1,
        "normal": 1,
    }
    if name not in mapping:
        raise ValueError(f"Unknown class folder name: {name}")
    return mapping[name]


def is_valid_image(path: Path) -> bool:
    """Return False for GIFs, corrupt files, or unsupported formats."""
    try:
        with Image.open(path) as img:
            if img.format == "GIF":
                return False
            img.verify()
        with Image.open(path) as img:
            img.load()
        return True
    except Exception:
        return False


def discover_samples(data_dir: Path) -> list[Sample]:
    """Discover labeled images from a split directory layout.

    Expected layout:
        data/train/  (or data/test/)
          fractured/
          not fractured/   (or non fractured/)
    """
    samples: list[Sample] = []
    if not data_dir.is_dir():
        return samples

    for class_dir in sorted(data_dir.iterdir()):
        if not class_dir.is_dir():
            continue
        try:
            label = _class_label(class_dir.name)
        except ValueError:
            continue
        for path in sorted(class_dir.iterdir()):
            if not path.is_file() or path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue
            if not is_valid_image(path):
                continue
            samples.append(Sample(path=path, label=label))
    return samples


def stratified_split(
    samples: list[Sample], validation_split: float, seed: int
) -> tuple[list[Sample], list[Sample]]:
    """Split samples by class, matching stratified validation_split behavior."""
    by_label: dict[int, list[Sample]] = {}
    for sample in samples:
        by_label.setdefault(sample.label, []).append(sample)

    train: list[Sample] = []
    val: list[Sample] = []
    rng = random.Random(seed)
    for group in by_label.values():
        shuffled = group[:]
        rng.shuffle(shuffled)
        val_count = int(len(shuffled) * validation_split)
        val.extend(shuffled[:val_count])
        train.extend(shuffled[val_count:])
    return train, val


def _make_dataset(samples: list[Sample], config: Config, shuffle: bool) -> "tf.data.Dataset":
    import tensorflow as tf

    channels = 1 if config.color_mode == "grayscale" else 3
    paths = [str(sample.path) for sample in samples]
    labels = [sample.label for sample in samples]

    ds = tf.data.Dataset.from_tensor_slices((paths, labels))
    if shuffle:
        ds = ds.shuffle(len(samples), seed=config.random_seed)

    def load_sample(path: tf.Tensor, label: tf.Tensor) -> tuple[tf.Tensor, tf.Tensor]:
        image = tf.io.read_file(path)
        image = tf.io.decode_image(image, channels=channels, expand_animations=False)
        image.set_shape([None, None, channels])
        image = tf.image.resize(image, config.image_size)
        return image, label

    ds = ds.map(load_sample, num_parallel_calls=tf.data.AUTOTUNE)
    ds = ds.batch(config.batch_size)
    return ds.prefetch(tf.data.AUTOTUNE)


def compute_class_weights(samples: list[Sample]) -> dict[int, float]:
    """Balanced class weights for imbalanced training data."""
    counts: dict[int, int] = {0: 0, 1: 0}
    for sample in samples:
        counts[sample.label] += 1
    total = sum(counts.values())
    if total == 0:
        return {0: 1.0, 1: 1.0}
    return {
        label: total / (len(counts) * count) if count else 1.0
        for label, count in counts.items()
    }


def load_train_val_datasets(
    config: Config,
) -> tuple["tf.data.Dataset", "tf.data.Dataset", list[Sample], list[Sample]]:
    """Load train/validation datasets from data/train/."""
    train_dir = config.train_dir
    samples = discover_samples(train_dir)
    if not samples:
        raise FileNotFoundError(
            f"No training data found in {train_dir}. "
            "Expected class subfolders 'fractured/' and 'not fractured/' (or 'non fractured/')."
        )

    train_samples, val_samples = stratified_split(
        samples, config.validation_split, config.random_seed
    )
    train_ds = _make_dataset(train_samples, config, shuffle=True)
    val_ds = _make_dataset(val_samples, config, shuffle=False)
    return train_ds, val_ds, train_samples, val_samples


def load_test_dataset(config: Config) -> "tf.data.Dataset":
    """Load held-out test dataset from data/test/."""
    test_dir = config.test_dir
    samples = discover_samples(test_dir)
    if not samples:
        raise FileNotFoundError(
            f"No test data found in {test_dir}. "
            "Expected class subfolders 'fractured/' and 'not fractured/' (or 'non fractured/')."
        )

    return _make_dataset(samples, config, shuffle=False)
