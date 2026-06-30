"""Evaluation entry point for fracture detection CNN.

Run: python -m src.evaluate
"""

from __future__ import annotations

import json

import numpy as np

from src.config import get_config
from src.data.dataset import discover_samples, load_test_dataset
from src.metrics import (
    compute_metrics,
    fracture_probability,
    plot_confusion_matrix,
    save_metrics,
)
from src.models.cnn import load_model


def predict_dataset(model, dataset) -> tuple[list[int], list[int], list[float]]:
    y_true: list[int] = []
    y_pred: list[int] = []
    y_score: list[float] = []

    for images, labels in dataset:
        logits = model.predict(images, verbose=0)
        for i, label in enumerate(labels.numpy()):
            logit = float(logits[i][0])
            prob_fractured = fracture_probability(logit)
            y_true.append(int(label))
            y_pred.append(0 if prob_fractured >= 0.5 else 1)
            y_score.append(prob_fractured)

    return y_true, y_pred, y_score


def main() -> None:
    config = get_config()
    config.ensure_dirs()

    if not discover_samples(config.test_dir):
        print(f"No test samples found in {config.test_dir}. See DATA_SPEC.md.")
        return

    if not config.checkpoint_path.is_file():
        print(f"No checkpoint at {config.checkpoint_path}. Run: python -m src.train")
        return

    test_ds = load_test_dataset(config)
    model = load_model(config.checkpoint_path, config)

    print(f"Evaluating on test set ({config.test_dir})...")
    y_true, y_pred, y_score = predict_dataset(model, test_ds)
    metrics = compute_metrics(y_true, y_pred, y_score)

    metrics_path = config.output_dir / "metrics.json"
    save_metrics(metrics, metrics_path)

    cm = np.array(
        [
            [metrics["confusion_matrix"]["true_positive"], metrics["confusion_matrix"]["false_negative"]],
            [metrics["confusion_matrix"]["false_positive"], metrics["confusion_matrix"]["true_negative"]],
        ]
    )
    cm_path = config.output_dir / "confusion_matrix.png"
    assets_cm = config.output_dir.parent / "docs" / "presentation" / "assets" / "confusion_matrix.png"
    plot_confusion_matrix(cm, list(config.class_names), cm_path)
    plot_confusion_matrix(cm, list(config.class_names), assets_cm)

    print(json.dumps(
        {k: v for k, v in metrics.items() if k != "classification_report"},
        indent=2,
    ))
    print(f"\nMetrics saved to: {metrics_path}")
    print(f"Confusion matrix saved to: {cm_path}")


if __name__ == "__main__":
    main()
