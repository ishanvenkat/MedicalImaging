"""Configuration for paths, hyperparameters, and reproducibility."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
MODEL_CHECKPOINT_DIR = OUTPUT_DIR / "checkpoints"
DEFAULT_CHECKPOINT = MODEL_CHECKPOINT_DIR / "model_weights.weights.h5"
DEFAULT_FULL_CHECKPOINT = MODEL_CHECKPOINT_DIR / "model_weights.keras"
DEFAULT_TRAINING_LOG = OUTPUT_DIR / "training.log"


def _env_path(key: str, default: Path) -> Path:
    value = os.environ.get(key)
    if value is None:
        return default
    return Path(value)


def _env_int(key: str, default: int) -> int:
    value = os.environ.get(key)
    if value is None:
        return default
    return int(value)


def _env_float(key: str, default: float) -> float:
    value = os.environ.get(key)
    if value is None:
        return default
    return float(value)


def _env_str(key: str, default: str) -> str:
    return os.environ.get(key, default)


@dataclass
class Config:
    """Project configuration for fracture detection training and evaluation."""

    data_dir: Path = field(default_factory=lambda: _env_path("MEDIMG_DATA_DIR", DATA_DIR))
    train_dir: Path = field(
        default_factory=lambda: _env_path("MEDIMG_TRAIN_DIR", DATA_DIR / "train")
    )
    test_dir: Path = field(default_factory=lambda: _env_path("MEDIMG_TEST_DIR", DATA_DIR / "test"))
    output_dir: Path = field(default_factory=lambda: _env_path("MEDIMG_OUTPUT_DIR", OUTPUT_DIR))
    checkpoint_dir: Path = field(
        default_factory=lambda: _env_path("MEDIMG_CHECKPOINT_DIR", MODEL_CHECKPOINT_DIR)
    )
    checkpoint_path: Path = field(default_factory=lambda: DEFAULT_CHECKPOINT)
    full_checkpoint_path: Path = field(default_factory=lambda: DEFAULT_FULL_CHECKPOINT)
    training_log_path: Path = field(
        default_factory=lambda: _env_path("MEDIMG_TRAINING_LOG", DEFAULT_TRAINING_LOG)
    )

    # v1 notebook CNN — full-resolution training on data/train/
    model_type: str = field(default_factory=lambda: _env_str("MEDIMG_MODEL_TYPE", "v1"))
    img_height: int = field(default_factory=lambda: _env_int("MEDIMG_IMG_HEIGHT", 1560))
    img_width: int = field(default_factory=lambda: _env_int("MEDIMG_IMG_WIDTH", 1170))
    color_mode: str = "grayscale"
    batch_size: int = field(default_factory=lambda: _env_int("MEDIMG_BATCH_SIZE", 5))
    validation_split: float = field(default_factory=lambda: _env_float("MEDIMG_VAL_SPLIT", 0.2))
    epochs: int = field(default_factory=lambda: _env_int("MEDIMG_EPOCHS", 15))
    learning_rate: float = field(default_factory=lambda: _env_float("MEDIMG_LEARNING_RATE", 1e-3))
    random_seed: int = field(default_factory=lambda: _env_int("MEDIMG_SEED", 123))
    l2_reg: float = field(default_factory=lambda: _env_float("MEDIMG_L2_REG", 0.01))
    dropout_rate: float = field(default_factory=lambda: _env_float("MEDIMG_DROPOUT", 0.25))

    class_names: tuple[str, ...] = ("fractured", "non fractured")

    @property
    def image_size(self) -> tuple[int, int]:
        return (self.img_height, self.img_width)

    @property
    def num_channels(self) -> int:
        return 1 if self.color_mode == "grayscale" else 3

    def ensure_dirs(self) -> None:
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)


def get_config() -> Config:
    return Config()
