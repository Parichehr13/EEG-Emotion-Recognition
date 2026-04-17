# EEG_Emotion_Recognition Figures

This directory contains the exported figures generated from the notebook `EEG_Emotion_Recognition.ipynb` in the main repository. These images document the workflow, model behavior, and evaluation results for EEG-based emotion recognition experiments on the **DEAP** and **SEED** datasets.

The repository as a whole is based on an M.Sc. thesis on EEG emotion recognition using deep learning and hyperparameter optimization.

---

## What This Folder Contains

The figures in this folder are visual outputs extracted from notebook cells and saved as `.png` files. They mainly cover:

- data loading and preprocessing
- baseline CNN experiments before hyperparameter tuning
- optimized CNN experiments after hyperparameter optimization
- training and evaluation outputs
- confusion matrices
- DEAP results for Valence, Arousal, Dominance, and Liking
- SEED dataset results
- selected classical machine learning baseline outputs

This folder currently includes:

- `README.md`
- `manifest.json`
- `figure_01_...png` through `figure_48_...png`

---

## Purpose

This folder serves as a visual summary of the experimental pipeline and results. It is especially useful for readers who want to:

- inspect the model outputs without opening the full notebook
- quickly review evaluation results
- compare baseline and optimized model behavior
- reuse result figures in documentation, presentations, or academic reporting
---

## Figure Groups

The figures in this directory naturally fall into the following groups:

- DEAP loading and preprocessing
- baseline CNN outputs before hyperparameter tuning
- optimized CNN outputs
- DEAP Valence results
- DEAP Arousal results
- DEAP Dominance results
- DEAP Liking results
- classical ML baseline outputs
- SEED outputs

This grouping mirrors the overall experimental flow from preprocessing to baseline modeling, optimization, and final evaluation.

---

## Suggested Reading Order

For a quick walkthrough of the experiment, review the figures in this order:

1. Data loading and preprocessing
2. Baseline CNN figures
3. Training and evaluation before tuning
4. Optimized CNN and hyperparameter search outputs
5. DEAP outputs across Valence, Arousal, Dominance, and Liking
6. Classical ML baseline outputs
7. SEED outputs

This order follows the narrative of the notebook and helps readers move from setup to results logically.

---

## Relation To The Thesis

This figure collection comes from a thesis-driven research project focused on:

- EEG-based emotion recognition
- CNN-based deep learning
- layer-by-layer hyperparameter optimization
- multi-objective optimization concepts used in model design
- evaluation on DEAP and SEED

The reported results in the project include strong classification performance on both datasets, with DEAP accuracies of **96.46%** for Valence, **97.54%** for Arousal, **98.18%** for Dominance, **98.10%** for Liking, and **96.14%** on SEED.

---

## Notes On Reproducibility

These figures are exported outputs from the notebook as saved at the time of export. They are useful for inspection and reporting, but they should not be interpreted as proof that the notebook was rerun during export.

Full reproducibility depends on the availability of:

- the notebook itself
- dataset access instructions
- preprocessing details
- model configuration
- training environment information

---

## How To Use These Figures

You can use this folder to:

- browse experiment outputs without running the notebook
- support the main repository README with visual evidence
- include selected figures in slides or reports
- compare outputs between baseline and optimized models
- verify which stages of the pipeline have saved visual results

---

## Recommended Future Improvements

This folder could become even more useful with additions such as:

- short captions for each figure
- grouping figures into subfolders such as `deap/`, `seed/`, `baseline/`, and `optimized/`
- a compact index table mapping figure filenames to descriptions
- direct cross-links from the root README to especially important figures

---

## Example Folder Structure

```text
figures/EEG_Emotion_Recognition/
|-- README.md
|-- manifest.json
|-- figure_01_...
|-- figure_02_...
|-- ...
`-- figure_48_...
```

---

## Source

Repository: `Parichehr13/EEG-Emotion-Recognition`  
Folder: `figures/EEG_Emotion_Recognition/`
