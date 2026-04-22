# EEG Emotion Recognition

EEG-based emotion recognition with convolutional neural networks and hyperparameter optimization on the DEAP and SEED benchmarks.

This repository contains thesis-derived research code and preserves the original experimental notebook alongside lightweight scripts for data preparation, training, and evaluation.

## Overview

The project studies emotion recognition from EEG in two settings:

- binary affective classification on DEAP
- three-class emotion classification on SEED

The repository includes:

- the main experimental notebook
- exported figures from the notebook
- reusable Python modules for dataset preparation, model definition, and training
- simple command-line scripts and example configs
- reported result tables from the thesis experiments

## Datasets and Tasks

| Dataset | Task | Labels |
| --- | --- | --- |
| DEAP | Binary classification | Valence, Arousal, Dominance, Liking as low vs. high |
| SEED | Three-class classification | Negative, Neutral, Positive |

DEAP experiments use the Python preprocessed release with subject `.dat` files.
SEED experiments use the extracted-feature release.

Raw datasets are not redistributed in this repository.

## Method Summary

The repository follows the original thesis workflow:

1. prepare dataset-specific inputs
2. train CNN models for EEG classification
3. evaluate selected DEAP and SEED tasks
4. run Optuna-based hyperparameter search for selected DEAP experiments

Implementation highlights:

- DEAP preprocessing follows the notebook logic: band-pass filtering, standardization, and sliding-window segmentation.
- SEED preparation builds numpy arrays from the released extracted-feature `.mat` files.
- Hyperparameter search is implemented with Optuna using `NSGAIISampler`.

## Reported Results

The values below are reported thesis experiment results recorded from the project notebook and thesis materials.
They are included here as reported results, not as freshly rerun results from this README revision.

| Dataset | Setting | Accuracy |
| --- | --- | --- |
| DEAP | Valence | 96.47% |
| DEAP | Arousal | 97.54% |
| DEAP | Dominance | 98.18% |
| DEAP | Liking | 98.10% |
| SEED | Negative / Neutral / Positive | 96.14% |

Structured copies of these reported values are available in [results/reported_metrics.csv](results/reported_metrics.csv).

## Repository Contents

```text
.
|-- README.md
|-- CITATION.cff
|-- requirements.txt
|-- configs/
|-- data/
|   `-- README.md
|-- docs/
|   `-- reproducibility.md
|-- figures/
|   `-- EEG_Emotion_Recognition/
|-- notebooks/
|   |-- EEG_Emotion_Recognition.ipynb
|   `-- archive/
|-- results/
|   |-- reported_metrics.csv
|   `-- legacy/
|-- scripts/
`-- src/
    `-- eeg_emotion_recognition/
```

## Reproducibility

Install dependencies:

```bash
pip install -r requirements.txt
```

Example commands:

```bash
python scripts/train_deap.py \
  --config configs/deap_valence_selected.json \
  --source path/to/data_preprocessed_python.zip \
  --output-dir results/runs/deap_valence

python scripts/run_deap_optuna.py \
  --config configs/deap_optuna_search.json \
  --source path/to/data_preprocessed_python.zip \
  --task valence \
  --output-dir results/runs/deap_valence_optuna

python scripts/prepare_seed_features.py \
  --config configs/seed_de_movingave.json \
  --source path/to/ExtractedFeatures.zip \
  --output-dir data/processed/seed/de_movingAve

python scripts/train_seed.py \
  --config configs/seed_de_movingave.json \
  --source-dir data/processed/seed/de_movingAve \
  --output-dir results/runs/seed_de_movingAve
```

Dataset setup details are documented in [data/README.md](data/README.md).
Additional notes on what is and is not currently verified are documented in [docs/reproducibility.md](docs/reproducibility.md).

## Limitations

- The reported results are thesis results and are not newly reproduced in this README revision.
- The repository remains centered on the original thesis workflow and is not intended as a general EEG benchmark framework.
- Repeated-run aggregation, subject-independent evaluation, and cross-dataset experiments are not provided here.
- Some original experiments remain easiest to inspect in the preserved notebook.
