# Notebook Integration Guide

## Status: Complete

The notebook has been audited, code extracted to `src/`, the expanded dataset is in `data/train/` and `data/test/`, and the model has been retrained and evaluated locally.

## Audit Summary

| Item | Value |
|------|-------|
| Notebook | `notebooks/fracture_detection.ipynb` |
| Framework | TensorFlow / Keras |
| Dataset | Expanded bone fracture X-ray dataset (~9,223 images total) |
| Train split | `data/train/` — 8,723 images (4,606 fractured / 4,120 not fractured) |
| Test split | `data/test/` — 500 images (238 fractured / 262 not fractured) |
| Image size | 1560 × 1170 grayscale |
| Training split | 80/20 train/validation from `data/train/` (seed=123) |
| Final model | L2 + augmentation + dropout (notebook cell 46 / v1 architecture) |
| Extracted to | `src/models/cnn.py` |

## Local Retrain Results (2026-06-25 — Fresh Full Run)

| Metric | Value |
|--------|-------|
| Best validation accuracy (training) | **95.87%** |
| Best validation loss (training) | **0.1060** |
| Test accuracy | **84.4%** (422/500) |
| Sensitivity (fracture recall) | **94.1%** (224/238) |
| Specificity | **75.6%** (198/262) |
| AUC-ROC | **0.882** |

### Confusion Matrix (Test — 500 images)

```
                 Predicted
                 Fractured   Not fractured
Actual Fractured     224          14
       Not fractured   64         198
```

## Earlier Results (90-image Colab prototype, 2026-06-23)

| Metric | Value |
|--------|-------|
| Best validation accuracy (training) | 88.89% |
| Validation accuracy (evaluate) | 83.33% (15/18) |
| Sensitivity | 90.91% (10/11) |
| Specificity | 71.43% (5/7) |

## Checklist

- [x] Identify ML framework and version
- [x] Record architecture and hyperparameters
- [x] Document dataset source and splits
- [x] Extract metrics from notebook outputs
- [x] Copy architecture to `src/models/cnn.py`
- [x] Copy preprocessing to `src/data/preprocessing.py`
- [x] Wire `src/train.py`, `src/evaluate.py`, `src/infer.py`
- [x] Add notebook footer cell for reproducible runs
- [x] Update `MODEL_SPEC.md` and `DATA_SPEC.md`
- [x] Organize expanded dataset into `data/train/` and `data/test/`
- [x] Retrain locally: `python -m src.train`
- [x] Evaluate locally: `python -m src.evaluate`
- [x] Save training curve and confusion matrix to `docs/presentation/assets/`

## Project Layout

```
notebooks/fracture_detection.ipynb     # Primary demo artifact (Colab origin)
data/
  train/fractured/ | train/not fractured/
  test/fractured/  | test/not fractured/
src/
  models/cnn.py                          # v1 + v2 architecture variants
  train.py | evaluate.py | infer.py      # CLI entry points
outputs/
  checkpoints/model_weights.weights.h5   # Best weights (val_accuracy)
  checkpoints/model_weights_v1.keras     # Legacy full-model backup
  metrics.json
  training.log
  training_curve.png
docs/presentation/assets/
  training_curve.png
  confusion_matrix.png
```

## Quick Start

```bash
pip install -r requirements.txt
python -m src.train
python -m src.evaluate
python -m src.infer --image path/to/xray.jpg
```

## Extract Notebook Assets (Optional)

If you re-run the Colab notebook and want to refresh plots from notebook cell outputs:

```bash
python scripts/extract_notebook_assets.py
```

The canonical training curve for the presentation is the one produced by `src.train` at `docs/presentation/assets/training_curve.png`.

## Verify

```bash
pytest tests/
```

## Related Documents

- [`docs/specifications/MODEL_SPEC.md`](../docs/specifications/MODEL_SPEC.md) — architecture, hyperparameters, metrics
- [`docs/specifications/DATA_SPEC.md`](../docs/specifications/DATA_SPEC.md) — dataset layout, class balance, ethics
- [`docs/presentation/outline.md`](../docs/presentation/outline.md) — GHLC presentation slides

## Notes

- Evaluation runs on the **held-out test set** (`data/test/`), not the validation split used during training.
- Training on full-resolution images at batch size 5 takes several hours on CPU (~25 min/epoch). TensorFlow GPU is not available on native Windows for TF ≥ 2.11; use WSL2 for GPU acceleration.
- Checkpoints save **weights only** (`model_weights.weights.h5`) to avoid large-model save failures on Windows.
- `EarlyStopping` restores weights by `val_loss`; `ModelCheckpoint` saves the best weights by `val_accuracy`.
