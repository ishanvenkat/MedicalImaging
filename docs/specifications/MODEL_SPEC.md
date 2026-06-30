# Model Specification

## Overview

| Field | Value |
|-------|-------|
| Task | Binary classification: fractured vs. non fractured |
| Input modality | X-ray (grayscale radiograph) |
| Framework | TensorFlow / Keras 2.x |
| Model type | Convolutional Neural Network (CNN) with data augmentation |

## Architecture (v2 — Expanded Dataset Retrain)

Improvements based on v1 training (95.5% val / 85.8% test — overfitting gap):

| Change | v1 | v2 |
|--------|----|----|
| Input size | 1560 × 1170 | **512 × 384** (same aspect ratio, faster, less overfit) |
| Pooling | Flatten | **GlobalAveragePooling2D** |
| Augmentation | Flip, rotation 5% | Flip, rotation 8%, zoom, contrast |
| Dropout | 0.25 | **0.40** |
| Batch size | 5 | **32** |
| Class weights | None | **Balanced** (reduce false-positive bias) |
| Checkpoint metric | val_accuracy | **val_loss** (aligns with EarlyStopping) |
| Epochs | 15 | **20** (early stopping patience 7) |

Model type is configurable via `MEDIMG_MODEL_TYPE` (`cnn` default, `transfer` for EfficientNetB0 when ImageNet weights are available).

### CNN layers (v2)

| Layer | Details |
|-------|---------|
| Data augmentation | RandomFlip, RandomRotation (8%), RandomZoom, RandomContrast |
| Rescaling | 1/255 |
| Conv2D | 16 filters, 3×3, ReLU, L2(0.01) |
| MaxPooling2D | 2×2 |
| Conv2D | 32 filters, 3×3, ReLU, L2(0.01) |
| MaxPooling2D | 2×2 |
| Conv2D | 64 filters, 3×3, ReLU, L2(0.01) |
| MaxPooling2D | 2×2 |
| Dropout | 0.40 |
| GlobalAveragePooling2D | — |
| Dense | 128 units, ReLU, L2(0.01) |
| Dropout | 0.40 |
| Output | 1 unit, linear logits |

- Input shape: **512 × 384 × 1** (grayscale)

## Architecture (v1 — Notebook / Original 90-image dataset)

Final model from notebook cell 46 — L2 regularization + dropout (no batch normalization):

| Layer | Details |
|-------|---------|
| Data augmentation | RandomFlip (horizontal), RandomRotation (5%) |
| Rescaling | 1/255 |
| Conv2D | 16 filters, 3×3, ReLU, L2(0.01) |
| MaxPooling2D | 2×2 |
| Conv2D | 32 filters, 3×3, ReLU, L2(0.01) |
| MaxPooling2D | 2×2 |
| Conv2D | 64 filters, 3×3, ReLU, L2(0.01) |
| MaxPooling2D | 2×2 |
| Dropout | 0.25 |
| Flatten | — |
| Dense | 128 units, ReLU |
| Output | 1 unit, linear logits |

- Input shape: **1560 × 1170 × 1** (grayscale)
- Parameters: ~1.48M trainable (from notebook `model.summary()`)

## Training Configuration

| Hyperparameter | Value |
|----------------|-------|
| Image size | 1560 × 1170 |
| Color mode | grayscale |
| Batch size | 5 |
| Epochs (final model) | 15 |
| Optimizer | Adam (lr=0.001) |
| Loss | BinaryCrossentropy (from_logits=True) |
| Validation split | 0.2 (seed=123) |
| L2 regularization | 0.01 |
| Dropout | 0.25 |

### Callbacks

- EarlyStopping: monitor `val_loss`, patience=10, restore_best_weights
- ModelCheckpoint: monitor `val_accuracy`, save best weights to `outputs/checkpoints/model_weights.weights.h5`
- ReduceLROnPlateau: monitor `val_loss`, factor=0.2, patience=5

## Dataset Reference

See [`DATA_SPEC.md`](DATA_SPEC.md).

| Split | Samples | Notes |
|-------|---------|-------|
| Train | 72 | 80% of 90 images |
| Validation | 18 | 20% of 90 images |
| Test | — | No held-out test set in notebook |

| Class | Folder name |
|-------|-------------|
| Fractured | `fractured/` |
| Non fractured | `non fractured/` |

## Metrics (Fresh v1 Retrain — Expanded Dataset, 2026-06-25)

Training completed 15 epochs. Best validation accuracy **95.87%**, validation loss **0.1060**.

Evaluated on held-out test set (`data/test/`, 500 images) using `outputs/checkpoints/model_weights.weights.h5`:

| Metric | Value | Notes |
|--------|-------|-------|
| Test accuracy | **84.4%** | 422/500 correct |
| Sensitivity (fracture recall) | **94.1%** | 224/238 fractured detected |
| Specificity | **75.6%** | 198/262 non-fractured correct |
| AUC-ROC | **0.882** | Fractured class as positive |

### Confusion Matrix (Test)

```
                 Predicted
                 Fractured   Non fractured
Actual Fractured     224          14
       Non fractured   64         198
```

Compared to the interrupted first run (85.8% acc): slightly lower accuracy, but **higher sensitivity** (94.1% vs 90.3%) with more false positives (64 vs 48).

## Metrics (v2 Retrain — Expanded Dataset)

Evaluated on held-out test set (`data/test/`, 500 images):

| Metric | v1 (interrupted) | v2 | Notes |
|--------|------------------|-----|-------|
| Test accuracy | 85.8% | **47.6%** | v2 failed to learn (predicts all fractured) |
| Sensitivity | 90.3% | 100.0% | v2: no false negatives, all positives |
| Specificity | 81.7% | 0.0% | v2: no true negatives |
| AUC-ROC | 0.876 | 0.500 | v2: random/chance level |

v2 training plateaued at ~52.7% validation accuracy (9 epochs, early stopping). The v1 checkpoint remains the best model — see `outputs/checkpoints/model_weights_v1.keras`.

## Metrics (v1 — Expanded Dataset, Interrupted Training)

Evaluated on validation set (18 images) using `outputs/checkpoints/model_weights.keras`:

| Metric | Value | Notes |
|--------|-------|-------|
| Validation accuracy (best epoch) | **88.89%** | Best during training (ModelCheckpoint) |
| Validation accuracy (evaluate) | **83.33%** | 15/18 on loaded checkpoint |
| Sensitivity (fracture recall) | **90.91%** | 10/11 fractured images detected |
| Specificity | **71.43%** | 5/7 non-fractured images correct |
| AUC-ROC | **0.844** | Fractured class as positive |

### Confusion Matrix (Validation)

```
                 Predicted
                 Fractured   Non fractured
Actual Fractured      10           1
       Non fractured    2           5
```

## What the Model Learned

The model learns visual patterns in X-ray images associated with bone fractures — such as discontinuities in bone cortex and abnormal edges — distinguishing them from intact bone structures.

## Known Failure Modes

- **Small dataset (90 images):** High variance in validation metrics; model may not generalize.
- **Overfitting observed:** Baseline model reached 94% val accuracy but degraded; regularization improved stability at ~89%.
- **No demographic diversity documented:** Age, body region, scanner type unknown.
- **High resolution (1560×1170):** Slow training; may not run on low-resource edge devices without downsampling.
- **False positives/negatives:** Not systematically catalogued — run evaluation locally and review misclassified images.

## Model Iterations (Notebook)

| Version | Key change | Best val / test |
|---------|------------|-----------------|
| Baseline (notebook) | 3 Conv blocks, no augmentation | 94.44% val (epoch 3, then degraded) |
| + Augmentation + Dropout | RandomFlip, RandomRotation, Dropout 0.2 | 83.33% val |
| + L2 + BatchNorm | Added L2 and BatchNormalization | 66.67% val (underfitting) |
| Final (90-image Colab) | L2 + Dropout, no BatchNorm | 88.89% val |
| **Expanded dataset (2026-06-25)** | Same v1 architecture, ~8,723 train / 500 test | **95.87% val**, **84.4% test acc** |

## Artifacts

| Artifact | Path |
|----------|------|
| Notebook | `notebooks/fracture_detection.ipynb` |
| Checkpoint (weights) | `outputs/checkpoints/model_weights.weights.h5` |
| Legacy full model | `outputs/checkpoints/model_weights_v1.keras` |
| Metrics JSON | `outputs/metrics.json` |
| Training log | `outputs/training.log` |
| Training curve | `docs/presentation/assets/training_curve.png` |
| Confusion matrix | `docs/presentation/assets/confusion_matrix.png` |

## Integration Status

- [x] Notebook uploaded and audited
- [x] Architecture extracted to `src/models/cnn.py`
- [x] Expanded dataset in `data/train/` and `data/test/`
- [x] Model retrained locally (`python -m src.train`, 15 epochs)
- [x] Full test-set evaluation (`python -m src.evaluate`)
- [x] Training curve and confusion matrix in `docs/presentation/assets/`
