"""Training entry point for fracture detection CNN.

Run: python -m src.train
Logs: outputs/training.log (via shell redirect, see README)
"""

from __future__ import annotations

import random
from datetime import datetime, timezone

import numpy as np
import tensorflow as tf

from src.config import get_config
from src.data.dataset import discover_samples, load_train_val_datasets
from src.metrics import plot_training_history
from src.models.cnn import build_model, get_callbacks


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


def main() -> None:
    config = get_config()
    config.ensure_dirs()
    set_seed(config.random_seed)

    train_samples = discover_samples(config.train_dir)
    test_samples = discover_samples(config.test_dir)
    if not train_samples:
        print(
            f"No images found in {config.train_dir}.\n"
            "Expected layout:\n"
            "  data/train/fractured/*.jpg\n"
            "  data/train/not fractured/*.jpg\n"
            "See docs/specifications/DATA_SPEC.md."
        )
        return

    started_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"=== Fresh training run started {started_at} ===")
    print(f"Model type: {config.model_type}")
    print(f"Image size: {config.image_size[0]}x{config.image_size[1]}")
    print(f"Batch size: {config.batch_size}")
    print(f"Epochs: {config.epochs}")
    print(f"Log file: {config.training_log_path}")
    print(f"Found {len(train_samples)} training images in {config.train_dir}")
    print(f"Found {len(test_samples)} test images in {config.test_dir}")

    train_ds, val_ds, _, _ = load_train_val_datasets(config)
    model = build_model(config)
    callbacks = get_callbacks(config)

    print(f"Training from epoch 1/{config.epochs}...")
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=config.epochs,
        callbacks=callbacks,
    )

    plot_path = config.output_dir / "training_curve.png"
    plot_training_history(history, plot_path)
    assets_path = config.output_dir.parent / "docs" / "presentation" / "assets" / "training_curve.png"
    plot_training_history(history, assets_path)

    best_val_loss = min(history.history["val_loss"])
    best_val_acc = max(history.history["val_accuracy"])
    print(f"Training complete. Best validation loss: {best_val_loss:.4f}")
    print(f"Best validation accuracy: {best_val_acc:.4f}")
    print(f"Checkpoint saved to: {config.checkpoint_path}")
    print(f"Training curve saved to: {plot_path}")


if __name__ == "__main__":
    main()
