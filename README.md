# EEG Emotion Recognition

This repository now includes the `ER_with_EEG` notebook for EEG-based emotion recognition experiments.

## Contents

- `notebooks/ER_with_EEG.ipynb`: the main Colab notebook with experiments on the DEAP dataset and SEED feature-based classification.
- `figures/ER_with_EEG/`: exported notebook figures saved from the notebook outputs.

## Current Notebook Notes

The notebook was originally developed in Google Colab and still contains:

- `drive.mount('/content/drive')`
- package installation commands such as `!pip install optuna`
- hardcoded `/content/...` and `/content/drive/MyDrive/...` dataset paths

That means the notebook has been added to the repository as the original source, but it has not yet been refactored into a fully local, repo-relative workflow.

## Suggested Next Step

Refactor the notebook so datasets, saved outputs, and extracted features use project-relative paths instead of Google Drive paths.
