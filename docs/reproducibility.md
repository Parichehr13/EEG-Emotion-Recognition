# Reproducibility Status

This document separates what is actually verified from what is inferred by reading the notebook and project files.

## Verified in the current cleanup environment

- The repository structure and files were audited locally.
- The main thesis notebook contains:
  - DEAP preprocessing from subject `.dat` files
  - DEAP CNN training
  - DEAP Optuna studies using `NSGAIISampler`
  - classical ML baselines
  - SEED feature-array construction from `ExtractedFeatures`
  - SEED CNN training
- Embedded notebook output cells contain selected-run test accuracies for DEAP and SEED.
- An example Optuna trial-history CSV is present and archived in `results/legacy/`.
- The local workspace contains:
  - `Dataset/SEED/ExtractedFeatures.zip`
  - `Dataset/DEAP/data_preprocessed_matlab.zip`

## Not verified in the current cleanup environment

- Running `python --version` failed because the current `python` command is not usable here.
- `jupyter` is not installed here.
- No notebook cell was rerun.
- No training script was executed.
- No reported metric was independently reproduced.

## Important reproducibility blockers surfaced by the audit

### 1. Environment execution blocker

The current machine session cannot execute Python or Jupyter, so this cleanup is a structure-and-code refactor, not a rerun study.

### 2. DEAP data-format mismatch

The notebook expects `data_preprocessed_python.zip` with `.dat` files.
The local workspace contains `data_preprocessed_matlab.zip`.

That means the original DEAP notebook cannot be honestly described as rerunnable from the local data snapshot without additional dataset preparation.

### 3. Notebook-first workflow

Before this cleanup, preprocessing, training, hyperparameter search, evaluation, plotting, and result reporting were all embedded in one Colab-oriented notebook with hard-coded `/content/...` and Google Drive paths.

### 4. Scientific reporting ambiguity

The reported results are strong, but the original repo did not clearly distinguish:

- best run vs. average over seeds
- selected architecture vs. baseline architecture
- notebook output vs. reproduced script run

This cleanup keeps the reported numbers but labels them as reported selected runs rather than reproduced benchmarks.

## Practical next step for a full reproduction

To convert this into a truly rerun-verified project, the next high-value step is:

1. create a clean Python environment from `requirements.txt`
2. place the correct DEAP Python preprocessed archive in `data/raw/deap/`
3. run one DEAP task end to end from `scripts/train_deap.py`
4. run one SEED experiment end to end from `scripts/prepare_seed_features.py` and `scripts/train_seed.py`
5. save the newly generated outputs under `results/runs/` and update the README only with rerun-verified numbers

