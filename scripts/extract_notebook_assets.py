"""Extract presentation assets embedded in the fracture detection notebook."""

from __future__ import annotations

import base64
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK = PROJECT_ROOT / "notebooks" / "fracture_detection.ipynb"
ASSETS = PROJECT_ROOT / "docs" / "presentation" / "assets"


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    with NOTEBOOK.open(encoding="utf-8") as f:
        nb = json.load(f)

    for idx in [28, 38, 47]:
        for out in nb["cells"][idx].get("outputs", []):
            png_b64 = out.get("data", {}).get("image/png")
            if png_b64:
                (ASSETS / f"training_curve_cell{idx}.png").write_bytes(base64.b64decode(png_b64))

    final_src = ASSETS / "training_curve_cell47.png"
    if final_src.is_file():
        (ASSETS / "training_curve.png").write_bytes(final_src.read_bytes())
        print(f"Saved {ASSETS / 'training_curve.png'}")
    else:
        print("No training curve found in notebook outputs.")


if __name__ == "__main__":
    main()
