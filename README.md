# EEG Emotion Recognition

This repository now includes the `ER_with_EEG` notebook for EEG-based emotion recognition experiments.

## Contents

- `ER_with_EEG.ipynb`: the main Colab notebook with experiments on the DEAP dataset and SEED feature-based classification.
- `figures/ER_with_EEG/`: exported notebook figures saved from the notebook outputs.
- `data/README.md`: instructions for keeping large datasets outside Git history.

## Current Notebook Notes

The notebook was originally developed in Google Colab and still contains:

- `drive.mount('/content/drive')`
- package installation commands such as `!pip install optuna`
- hardcoded `/content/...` and `/content/drive/MyDrive/...` dataset paths

That means the notebook has been added to the repository as the original source, but it has not yet been refactored into a fully local, repo-relative workflow.

## Suggested Next Step

Refactor the notebook so datasets, saved outputs, and extracted features use project-relative paths instead of Google Drive paths.

## Working With Large Datasets

Do not commit the full raw dataset into normal Git history if it is large. This repository is set up so you can keep datasets local and still work with the code.

Recommended local layout:

- keep your original dataset at `D:\emotion\Dataset`
- use a local repo data folder such as `data\Dataset`
- do not push raw dataset files to GitHub unless you intentionally switch to Git LFS

On Windows, you can create a local junction inside the repository that points to your existing dataset folder:

```powershell
New-Item -ItemType Junction -Path .\data\Dataset -Target "D:\emotion\Dataset"
```

This lets notebooks and scripts read the dataset from the repository path without copying the full dataset into Git.
