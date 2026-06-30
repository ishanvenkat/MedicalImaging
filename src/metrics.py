"""Metric computation and plotting."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
)


def fracture_probability(logit: float) -> float:
    """Probability of fractured class (label 0) from model logit."""
    return float(1.0 - (1.0 / (1.0 + np.exp(-logit))))


def compute_metrics(y_true: list[int], y_pred: list[int], y_score: list[float]) -> dict[str, Any]:
    """Compute metrics with fractured (0) as the positive class."""
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    tp, fn, fp, tn = cm.ravel() if cm.size == 4 else (0, 0, 0, 0)

    sensitivity = tp / (tp + fn) if (tp + fn) else 0.0
    specificity = tn / (tn + fp) if (tn + fp) else 0.0
    accuracy = accuracy_score(y_true, y_pred)

    y_fractured = [1 if label == 0 else 0 for label in y_true]
    auc = roc_auc_score(y_fractured, y_score) if len(set(y_fractured)) > 1 else 0.0

    return {
        "accuracy": round(accuracy, 4),
        "sensitivity": round(sensitivity, 4),
        "specificity": round(specificity, 4),
        "auc_roc": round(float(auc), 4),
        "confusion_matrix": {
            "true_negative": int(tn),
            "false_positive": int(fp),
            "false_negative": int(fn),
            "true_positive": int(tp),
        },
        "classification_report": classification_report(
            y_true, y_pred, target_names=["fractured", "non fractured"], output_dict=True
        ),
    }


def save_metrics(metrics: dict[str, Any], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")


def plot_confusion_matrix(cm: np.ndarray, class_names: list[str], path: Path) -> None:
    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
    ax.figure.colorbar(im, ax=ax)
    ax.set(
        xticks=np.arange(cm.shape[1]),
        yticks=np.arange(cm.shape[0]),
        xticklabels=class_names,
        yticklabels=class_names,
        ylabel="True label",
        xlabel="Predicted label",
        title="Confusion Matrix",
    )
    thresh = cm.max() / 2.0 if cm.max() else 0
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], "d"), ha="center", va="center", color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def plot_training_history(history: Any, path: Path) -> None:
    acc = history.history["accuracy"]
    val_acc = history.history["val_accuracy"]
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    epochs_range = range(1, len(acc) + 1)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(epochs_range, acc, label="Training Accuracy")
    axes[0].plot(epochs_range, val_acc, label="Validation Accuracy")
    axes[0].legend(loc="lower right")
    axes[0].set_title("Training and Validation Accuracy")

    axes[1].plot(epochs_range, loss, label="Training Loss")
    axes[1].plot(epochs_range, val_loss, label="Validation Loss")
    axes[1].legend(loc="upper right")
    axes[1].set_title("Training and Validation Loss")

    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
