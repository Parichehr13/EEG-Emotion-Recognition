# EEG Emotion Recognition

Compact, thesis-derived research code for EEG-based emotion recognition with CNNs and Optuna/NSGA-II style hyperparameter search on the DEAP and SEED benchmarks.

This repository is based on the M.Sc. thesis:

> Parichehr Moradi, *EEG-Based Emotion Recognition Using Convolutional Neural Networks and Hyperparameter Optimization*, University of Isfahan, 2022.

GitHub repository: <https://github.com/Parichehr13/EEG-Emotion-Recognition>

## Why this project is worth keeping

The project idea is strong enough to matter for a PhD CV:

- EEG-based emotion recognition is a real research topic, not a toy benchmark.
- The work spans two established datasets: DEAP and SEED.
- The thesis combines deep learning with explicit hyperparameter search rather than only reporting a hand-tuned CNN.
- The notebook already contains nontrivial preprocessing, model design, Optuna-based search, classical baselines, and visual outputs.

The previous weakness was mostly reproducibility and presentation, not lack of technical substance.

## What changed in this cleanup

This repository is intentionally still compact, but it is no longer only a Colab notebook dump.

- `notebooks/EEG_Emotion_Recognition.ipynb` keeps the original thesis notebook as a research record.
- `src/eeg_emotion_recognition/` contains reusable data-loading, model, and training utilities extracted from the notebook logic.
- `scripts/` contains command-line entry points for DEAP training, DEAP hyperparameter search, SEED feature preparation, and SEED training.
- `configs/` contains example experiment configs.
- `results/` contains explicit reported metrics and an archived Optuna trial-history CSV.
- `data/README.md` now documents exactly which dataset artifacts the code expects.
- `docs/reproducibility.md` states what is verified by execution in this environment and what is only inferred from notebook inspection.

## Current reproducibility status

This cleanup improves reproducibility, but it does **not** claim full rerun verification in the current environment.

- Verified by inspection:
  - the notebook contains DEAP preprocessing, DEAP CNN training, DEAP Optuna search, classical ML baselines, SEED feature extraction, and SEED CNN training
  - the notebook includes embedded output cells with reported test accuracies
  - the local workspace contains SEED extracted-feature data and a DEAP MATLAB archive
- Not verified by execution here:
  - end-to-end notebook execution
  - script execution
  - reproduction of reported metrics
- Main blockers in this environment:
  - `python` is not runnable here
  - `jupyter` is not installed here
  - the DEAP notebook expects `data_preprocessed_python.zip` with `.dat` files, while the local workspace currently contains `data_preprocessed_matlab.zip`

If you use this repository in an application or CV, the honest claim is:

> thesis-derived research project with code, structured scripts, and documented reported results; not independently revalidated in this environment.

## Research tasks

### DEAP

Binary classification on four affective dimensions:

- valence: low vs. high
- arousal: low vs. high
- dominance: low vs. high
- liking: low vs. high

The notebook uses 32 EEG channels and applies band-pass filtering before segmentation.

Important implementation note:
the original notebook comment says "10 seconds windows with 2 seconds overlap", but the code advances windows by `256` samples while using `window_size = 1280` at `128 Hz`. That corresponds to a stride of 2 seconds, so the actual overlap is 8 seconds. This repository preserves the notebook behavior and documents it explicitly.

### SEED

Three-class classification:

- negative
- neutral
- positive

The notebook uses the extracted-feature release and builds arrays from `feature_type x smoothing_method` folders such as `de_movingAve`.

## Reported results

The repository currently has **selected-run reported test accuracies**, not repeated-run averages with confidence intervals.
They are recorded in [results/reported_metrics.csv](results/reported_metrics.csv).

Reported selected-run accuracies from the notebook / thesis materials:

| Dataset | Setting | Accuracy |
| --- | --- | --- |
| DEAP | Valence (binary) | 96.47% |
| DEAP | Arousal (binary) | 97.54% |
| DEAP | Dominance (binary) | 98.18% |
| DEAP | Liking (binary) | 98.10% |
| SEED | Negative / Neutral / Positive | 96.14% |

These are useful reported outcomes, but they should be read as thesis/project results rather than independently reproduced benchmark claims.

## Repository layout

```text
.
|-- README.md
|-- CITATION.cff
|-- requirements.txt
|-- configs/
|-- data/
|   `-- README.md
|-- docs/
|   |-- reproducibility.md
|   |-- slides/
|   `-- thesis/
|-- figures/
|   `-- EEG_Emotion_Recognition/
|-- notebooks/
|   |-- EEG_Emotion_Recognition.ipynb
|   `-- archive/
|-- results/
|   |-- README.md
|   |-- legacy/
|   `-- reported_metrics.csv
|-- scripts/
`-- src/
    `-- eeg_emotion_recognition/
```

## Quick start

Install dependencies:

```bash
pip install -r requirements.txt
```

Prepare and train DEAP from the Python preprocessed archive:

```bash
python scripts/train_deap.py \
  --config configs/deap_valence_selected.json \
  --source path/to/data_preprocessed_python.zip \
  --output-dir results/runs/deap_valence_selected
```

Run Optuna/NSGA-II style hyperparameter search for DEAP:

```bash
python scripts/run_deap_optuna.py \
  --config configs/deap_optuna_search.json \
  --source path/to/data_preprocessed_python.zip \
  --task valence \
  --output-dir results/runs/deap_valence_optuna
```

Prepare SEED features from the extracted-feature archive:

```bash
python scripts/prepare_seed_features.py \
  --config configs/seed_de_movingave.json \
  --source path/to/ExtractedFeatures.zip \
  --output-dir data/processed/seed/de_movingAve
```

Train the SEED CNN:

```bash
python scripts/train_seed.py \
  --config configs/seed_de_movingave.json \
  --source-dir data/processed/seed/de_movingAve \
  --output-dir results/runs/seed_de_movingAve
```

## What this repo still does not solve

This is still a compact thesis-derived project, not a full benchmark framework.

- No multi-seed aggregation pipeline is provided yet.
- No subject-independent evaluation pipeline is claimed here.
- No cross-dataset generalization experiments are added.
- No new results are invented in this cleanup.

Those would be reasonable future upgrades, but they should be added only after the current subject-dependent thesis pipeline is rerun cleanly.

## Recommendation for PhD applications

This repository is now much stronger as a CV project than a raw notebook-only version because it shows:

- a real biomedical ML problem
- benchmark awareness across DEAP and SEED
- structured code beyond a notebook
- honest reproducibility boundaries
- documented reported results instead of vague claims

It is strongest when presented as:

> a compact, thesis-derived research project with CNN-based EEG emotion recognition, hyperparameter optimization, and reproducible scripts/documentation for the original workflow.
