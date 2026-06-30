"""Image preprocessing for X-ray fracture detection."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from tensorflow import keras


def load_image_batch(path: Path, image_size: tuple[int, int], color_mode: str = "grayscale") -> np.ndarray:
    """Load a single image as a batch tensor matching the notebook pipeline."""
    if not path.is_file():
        raise FileNotFoundError(f"Image not found: {path}")
    img = keras.utils.load_img(str(path), target_size=image_size, color_mode=color_mode)
    arr = keras.utils.img_to_array(img)
    return np.expand_dims(arr, axis=0)
