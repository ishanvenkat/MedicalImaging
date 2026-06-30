"""Single-image inference demo for presentations.

Run: python -m src.infer --image path/to/xray.jpg
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

from src.config import get_config
from src.data.preprocessing import load_image_batch
from src.metrics import fracture_probability
from src.models.cnn import load_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run fracture detection on one X-ray image.")
    parser.add_argument("--image", type=Path, required=True, help="Path to a single X-ray image.")
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=None,
        help="Weights or full-model checkpoint (default: outputs/checkpoints/model_weights.weights.h5).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = get_config()
    config.ensure_dirs()

    checkpoint = args.checkpoint or config.checkpoint_path
    if not checkpoint.is_file():
        raise FileNotFoundError(
            f"Checkpoint not found: {checkpoint}. Train with: python -m src.train"
        )

    model = load_model(checkpoint, config)
    batch = load_image_batch(args.image, config.image_size, config.color_mode)

    start = time.perf_counter()
    logits = model.predict(batch, verbose=0)
    elapsed_ms = (time.perf_counter() - start) * 1000

    prob_fractured = fracture_probability(float(logits[0][0]))
    prob_non_fractured = 1.0 - prob_fractured

    print(f"Image: {args.image}")
    print(f"Inference time: {elapsed_ms:.1f} ms")
    print(f"Fractured:     {prob_fractured * 100:.2f}%")
    print(f"Non-fractured: {prob_non_fractured * 100:.2f}%")
    print(f"Prediction: {'fractured' if prob_fractured >= 0.5 else 'non fractured'}")


if __name__ == "__main__":
    main()
