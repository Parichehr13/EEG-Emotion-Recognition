# EEG_Emotion_Recognition Figures

This folder contains exported figures from `EEG_Emotion_Recognition.ipynb`. The images summarize preprocessing, model behavior, and evaluation results for EEG-based emotion recognition experiments on the **DEAP** and **SEED** datasets.

## Contents

This directory includes:

- `README.md`
- `manifest.json`
- `figure_01_...png` through `figure_48_...png`

The figures cover:

- data loading and preprocessing
- baseline CNN outputs before hyperparameter tuning
- optimized CNN outputs
- training and evaluation outputs
- confusion matrices
- DEAP results for Valence, Arousal, Dominance, and Liking
- SEED results
- selected classical ML baseline outputs

## File Naming

Figure files follow this pattern:

```text
figure_<index>_cell<cell_number>_<section>.png
```

The `manifest.json` file maps each figure to its notebook cell number and section heading.

## Figure Groups

The exported figures are mainly organized around these stages:

- DEAP loading and preprocessing
- baseline CNN outputs
- optimized CNN outputs
- DEAP Valence, Arousal, Dominance, and Liking results
- classical ML baseline outputs
- SEED outputs
