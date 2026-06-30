# AI-Assisted Medical Imaging: Fracture Detection

**Thesis:** Can AI-assisted medical imaging help expand access to diagnostic healthcare in underserved communities?

This repository supports a GHLC presentation and research project on using convolutional neural networks (CNNs) to detect bone fractures in X-ray images, with an extension exploring deployment in low-resource healthcare settings.

> **Disclaimer:** This is an educational research project. It is not a clinical diagnostic tool and must not be used for medical decision-making.

## Project Structure

| Path | Purpose |
|------|---------|
| [`notebooks/`](notebooks/) | Primary demo artifact — CNN training notebook |
| [`src/`](src/) | Reproducible train, evaluate, and inference modules |
| [`docs/specifications/`](docs/specifications/) | Project, model, data, presentation, and deployment specs |
| [`docs/presentation/`](docs/presentation/) | Timed outline and speaker notes |
| [`.cursor/rules/`](.cursor/rules/) | AI coding and presentation guidelines |
| [`.cursor/skills/`](.cursor/skills/) | Workflow skills for development and presentation prep |

## Quick Start

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set up the dataset** (images are not stored in Git — see [Dataset setup](#dataset-setup) below).

3. Open the notebook:

   ```bash
   jupyter notebook notebooks/fracture_detection.ipynb
   ```

4. For reproducible runs (after notebook integration):

   ```bash
   python -m src.train
   python -m src.evaluate
   python -m src.infer --image path/to/xray.png
   ```

## Dataset Setup

Training images are **not committed to GitHub** — they are too large and are excluded by [`.gitignore`](.gitignore). After cloning this repo, you must add the dataset locally before running `src.train`.

### Expected layout

```
data/
  train/
    fractured/       # ~4,606 images
    not fractured/   # ~4,120 images
  test/
    fractured/       # ~238 images
    not fractured/   # ~268 images
```

Folder names `non fractured/` are also accepted. See [`docs/specifications/DATA_SPEC.md`](docs/specifications/DATA_SPEC.md) for full details.

### How to obtain the data

Choose one of these options:

1. **Copy from your local backup** — If you already trained on this machine, your `data/train/` and `data/test/` folders are the source of truth. Copy them into a fresh clone.

2. **Restore from cloud storage** — Upload your `data/` folder to Google Drive, OneDrive, or similar and download it after cloning. Add the share link to `DATA_SPEC.md` for your own reference.

3. **Rebuild from archive** — If you have `data/archive/Bone_Fracture_Dataset/`, organize its contents into the `train/` and `test/` layout above.

4. **Original 90-image Colab set** — For a minimal demo only, use the archived `FractureXRayImages` layout under `data/archive/` (not comparable to full model metrics).

### Verify and run

```bash
python -c "from src.data.dataset import discover_samples; from src.config import get_config; c=get_config(); print('train', len(discover_samples(c.train_dir))); print('test', len(discover_samples(c.test_dir)))"
```

Expected output after a full setup: `train 8723` and `test 500` (6 invalid/corrupt files are skipped automatically).

Model checkpoints (`outputs/checkpoints/`) are also gitignored. Either train from scratch (`python -m src.train`, several hours on CPU) or copy a saved `model_weights.weights.h5` from backup.

### Custom paths (optional)

Override defaults with environment variables:

```bash
export MEDIMG_TRAIN_DIR=/path/to/train
export MEDIMG_TEST_DIR=/path/to/test
```

## Presentation

GHLC 2026 Student Speaker Series — **application deadline: July 20, 2026, 11:59 PM Eastern**

- **Title:** AI-Assisted Medical Imaging: A Path Toward Global Health Equity
- **Official sources:** [`docs/presentation/sources/`](docs/presentation/sources/) (guidelines PDF + mandatory slide template)
- **Outline:** [`docs/presentation/outline.md`](docs/presentation/outline.md)
- **Speaker notes:** [`docs/presentation/speaker-notes.md`](docs/presentation/speaker-notes.md)
- **Full spec:** [`docs/specifications/PRESENTATION_SPEC.md`](docs/specifications/PRESENTATION_SPEC.md)
- **Slides build guide:** [`docs/presentation/slides-guide.md`](docs/presentation/slides-guide.md)
- **Submission form:** https://forms.gle/Wx7L1WS59DECbtAV8

## Extension Research

How could AI-assisted fracture detection be deployed in low-resource settings? See [`docs/specifications/DEPLOYMENT_RESEARCH.md`](docs/specifications/DEPLOYMENT_RESEARCH.md).

## Notebook Integration Status

- [x] Notebook uploaded and audited
- [x] `MODEL_SPEC.md` and `DATA_SPEC.md` filled
- [x] Code extracted to `src/`
- [x] Expanded dataset in `data/train/` and `data/test/` (~8,723 train / 500 test)
- [x] Retrain: `python -m src.train` (best val accuracy **95.87%**, 15 epochs)
- [x] Evaluate: `python -m src.evaluate` (**84.4%** test acc, **94.1%** sensitivity, **75.6%** specificity)
- [x] Training curve and confusion matrix in `docs/presentation/assets/`

## References

See [`docs/references/bibliography.md`](docs/references/bibliography.md).
