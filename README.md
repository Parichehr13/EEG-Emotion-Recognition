# EEG Emotion Recognition

EEG-based emotion recognition using deep learning, benchmark affective datasets, and an optimized CNN-oriented workflow for emotional state classification.

---

## Overview

This repository presents a research project on **emotion recognition from electroencephalography (EEG)**. The work focuses on building a robust deep learning pipeline for classifying emotional states from brain signals, with experiments centered on public benchmark datasets and CNN-based modeling.

The project is rooted in affective computing and brain-computer interface research, where EEG offers a direct physiological window into emotional processing. The broader study investigates optimized CNN architectures for affect classification, while the repository documents the workflow, experimental outputs, and visual summaries of model behavior.

### Main goals

- classify emotional states from EEG recordings
- build a clear preprocessing-to-classification pipeline
- evaluate performance on standard public datasets
- analyze model learning behavior through training curves
- present the project in a clean, reproducible research format

---

## Workflow Overview

The full pipeline is summarized below.

![Workflow Overview](assets/workflow_overview.png)

**Original workflow slide:** [workflow_original_slide.pptx](assets/workflow_original_slide.pptx)

At a high level, the project follows four stages:

1. **Input EEG signal acquisition**
2. **Preprocessing** including segmentation and relabeling
3. **CNN-based modeling**
4. **Emotional state classification** on benchmark datasets

The framework covers:

- **DEAP** for binary classification tasks across multiple affective dimensions
- **SEED** for multi-class emotion recognition

---

## Datasets

### DEAP

The **DEAP** dataset is a widely used benchmark for affective EEG analysis. In this project, it is used for binary classification across multiple emotional dimensions:

- **Valence**: low vs high
- **Arousal**: low vs high
- **Dominance**: low vs high
- **Liking**: low vs high

### SEED

The **SEED** dataset is used for **multi-class emotion recognition** with three classes:

- **Negative**
- **Neutral**
- **Positive**

Together, these datasets allow the project to evaluate both binary and multi-class EEG emotion recognition settings.

---

## Methodology

### 1. Preprocessing

The preprocessing stage prepares raw EEG signals for learning by organizing them into model-ready segments and labels. This stage may include operations such as:

- segmentation into analysis windows
- relabeling into target emotion classes
- band-based EEG representation
- train / validation / test splitting

### 2. CNN-based learning

A Convolutional Neural Network (CNN) is used to learn discriminative representations from EEG-derived inputs. The overall design emphasizes:

- compact deep learning modeling
- stable optimization during training
- strong performance on benchmark emotion datasets

### 3. Classification

The final output is an emotional state label. Depending on the dataset, the task is either:

- **binary classification** for DEAP dimensions
- **multi-class classification** for SEED emotions

---

## Reported Performance

The project reports strong results on both DEAP and SEED.

### DEAP accuracy

| Task | Accuracy |
|------|----------|
| Valence | **96.46%** |
| Arousal | **97.54%** |
| Dominance | **98.18%** |
| Liking | **98.10%** |

### SEED accuracy

| Task | Accuracy |
|------|----------|
| Negative / Neutral / Positive | **96.14%** |

These results highlight the effectiveness of the proposed EEG emotion recognition framework across both binary and multi-class settings.

---

## Training Behavior

The following plots provide a visual summary of the model training dynamics.

### Accuracy curve

![Training Accuracy](assets/training_accuracy.png)

### Loss curve

![Training Loss](assets/training_loss.png)

The curves show a stable learning process, with training performance improving steadily and validation behavior remaining consistently strong throughout the optimization process.

---

## Complete Figure Gallery

The sections below include **all exported figures currently tracked in the repository**, including the confusion matrices, CNN diagrams, training plots, and classical baseline outputs from the notebook.

<details>
<summary>DEAP Loading And Baseline CNN</summary>

### Figure 01

Notebook section: `Loading Data > Loading and Pre-processing Deap Dataset`

<p align="center">
  <img src="figures/ER_with_EEG/figure_01_cell009_loading-data__loading-and-pre-processing-deap-dataset.png" alt="Figure 01" width="620">
</p>

### Figure 02

Notebook section: `CNN Model Before HP Tuning > Loading Data and Labels`

<p align="center">
  <img src="figures/ER_with_EEG/figure_02_cell021_cnn-model-before-hp-tuning__loading-data-and-labels.png" alt="Figure 02" width="620">
</p>

### Figure 03

Notebook section: `Training and Evaluation Before HP Tuning > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_03_cell028_training-and-evaluation-before-hp-tuning__training-and-evaluation__training-and-evaluation.png" alt="Figure 03" width="620">
</p>

### Figure 04

Notebook section: `Training and Evaluation Before HP Tuning > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_04_cell029_training-and-evaluation-before-hp-tuning__training-and-evaluation__training-and-evaluation.png" alt="Figure 04" width="620">
</p>

### Figure 05

Notebook section: `Training and Evaluation Before HP Tuning > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_05_cell032_training-and-evaluation-before-hp-tuning__training-and-evaluation__training-and-evaluation.png" alt="Figure 05" width="620">
</p>

### Figure 06

Notebook section: `Training and Evaluation Before HP Tuning > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_06_cell033_training-and-evaluation-before-hp-tuning__training-and-evaluation__training-and-evaluation.png" alt="Figure 06" width="620">
</p>

</details>

<details>
<summary>Optimized CNN And DEAP Valence Outputs</summary>

### Figure 07

Notebook section: `CNN Model > 5th Layer (i.e. Dense2) HPO > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_07_cell082_cnn-model__5th-layer-i-e-dense2-hpo__training-and-evaluation.png" alt="Figure 07" width="620">
</p>

### Figure 08

Notebook section: `CNN Model > 5th Layer (i.e. Dense2) HPO > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_08_cell084_cnn-model__5th-layer-i-e-dense2-hpo__training-and-evaluation.png" alt="Figure 08" width="620">
</p>

### Figure 09

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_09_cell092_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 09" width="620">
</p>

### Figure 10

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_10_cell093_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 10" width="620">
</p>

### Figure 11

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_11_cell096_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 11" width="620">
</p>

### Figure 12

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_12_cell097_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 12" width="620">
</p>

### Figure 13

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_13_cell100_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 13" width="620">
</p>

### Figure 14

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_14_cell101_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 14" width="620">
</p>

### Figure 15

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_15_cell104_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 15" width="620">
</p>

### Figure 16

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_16_cell105_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 16" width="620">
</p>

</details>

<details>
<summary>DEAP Arousal Outputs</summary>

### Figure 17

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_17_cell112_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 17" width="620">
</p>

### Figure 18

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_18_cell113_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 18" width="620">
</p>

### Figure 19

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_19_cell116_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 19" width="620">
</p>

### Figure 20

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_20_cell117_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 20" width="620">
</p>

### Figure 21

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_21_cell120_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 21" width="620">
</p>

### Figure 22

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_22_cell121_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 22" width="620">
</p>

### Figure 23

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_23_cell124_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 23" width="620">
</p>

### Figure 24

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_24_cell125_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 24" width="620">
</p>

</details>

<details>
<summary>DEAP Dominance Outputs</summary>

### Figure 25

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_25_cell132_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 25" width="620">
</p>

### Figure 26

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_26_cell133_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 26" width="620">
</p>

### Figure 27

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_27_cell136_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 27" width="620">
</p>

### Figure 28

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_28_cell137_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 28" width="620">
</p>

### Figure 29

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_29_cell140_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 29" width="620">
</p>

### Figure 30

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_30_cell141_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 30" width="620">
</p>

### Figure 31

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_31_cell144_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 31" width="620">
</p>

### Figure 32

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_32_cell145_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 32" width="620">
</p>

</details>

<details>
<summary>DEAP Liking Outputs</summary>

### Figure 33

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_33_cell152_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 33" width="620">
</p>

### Figure 34

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_34_cell153_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 34" width="620">
</p>

### Figure 35

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_35_cell156_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 35" width="620">
</p>

### Figure 36

Notebook section: `Training and Evaluation > Training and Evaluation with std calculation > Training and Evaluation with std calculation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_36_cell157_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="Figure 36" width="620">
</p>

### Figure 37

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_37_cell160_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 37" width="620">
</p>

### Figure 38

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_38_cell161_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 38" width="620">
</p>

### Figure 39

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_39_cell164_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 39" width="620">
</p>

### Figure 40

Notebook section: `Training and Evaluation > Training and Evaluation > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_40_cell165_training-and-evaluation__training-and-evaluation__training-and-evaluation.png" alt="Figure 40" width="620">
</p>

</details>

<details>
<summary>Classical ML Baseline Outputs</summary>

### Figure 41

Notebook section: `ML Models > SVM > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_41_cell173_ml-models__svm__training-and-evaluation.png" alt="Figure 41" width="620">
</p>

### Figure 42

Notebook section: `ML Models > RFC > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_42_cell175_ml-models__rfc__training-and-evaluation.png" alt="Figure 42" width="620">
</p>

### Figure 43

Notebook section: `ML Models > MLP > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_43_cell177_ml-models__mlp__training-and-evaluation.png" alt="Figure 43" width="620">
</p>

### Figure 44

Notebook section: `ML Models > KNN > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_44_cell179_ml-models__knn__training-and-evaluation.png" alt="Figure 44" width="620">
</p>

</details>

<details>
<summary>SEED Outputs</summary>

### Figure 45

Notebook section: `CNN Model > Loading and Pre-processing SEED Dataset > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_45_cell191_cnn-model__loading-and-pre-processing-seed-dataset__training-and-evaluation.png" alt="Figure 45" width="620">
</p>

### Figure 46

Notebook section: `Training and Evaluation > Loading and Pre-processing SEED Dataset > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_46_cell196_training-and-evaluation__loading-and-pre-processing-seed-dataset__training-and-evaluation.png" alt="Figure 46" width="620">
</p>

### Figure 47

Notebook section: `Training and Evaluation > Loading and Pre-processing SEED Dataset > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_47_cell197_training-and-evaluation__loading-and-pre-processing-seed-dataset__training-and-evaluation.png" alt="Figure 47" width="620">
</p>

### Figure 48

Notebook section: `Training and Evaluation > Loading and Pre-processing SEED Dataset > Training and Evaluation`

<p align="center">
  <img src="figures/ER_with_EEG/figure_48_cell200_training-and-evaluation__loading-and-pre-processing-seed-dataset__training-and-evaluation.png" alt="Figure 48" width="620">
</p>

</details>

---

## Why This Project Matters

Emotion recognition from EEG is relevant to several active research and application areas, including:

- **affective computing**
- **brain-computer interfaces**
- **human-computer interaction**
- **adaptive intelligent systems**
- **mental health and assistive technologies**

Compared with surface-level behavioral signals, EEG provides a physiological measure that can capture internal emotional dynamics more directly.

---

## Suggested Repository Structure

A clean structure for this project can follow the layout below:

```text
EEG-Emotion-Recognition/
├── README.md
├── assets/
│   ├── workflow_overview.png
│   ├── workflow_original_slide.pptx
│   ├── training_accuracy.png
│   └── training_loss.png
├── notebooks/
├── src/
├── data/
├── results/
└── docs/
```

---

## Future Directions

Potential next steps for extending this work include:

- subject-independent evaluation
- cross-dataset generalization
- explainable AI for EEG feature importance
- attention-based or transformer-based EEG models
- real-time emotion recognition pipelines
- broader comparison with alternative deep learning baselines

---

## Author

**Parichehr Moradi**  
Biomedical Engineering Researcher  
Focus areas: EEG, affective computing, deep learning, biomedical signal analysis

---

## Citation

If this repository is used in academic or technical work, please cite the corresponding thesis or project report.

```bibtex
@mastersthesis{moradi2022eegemotion,
  title     = {Using Evolutionary Computation Algorithms for EEG-Based Emotion Recognition},
  author    = {Moradi, Parichehr},
  school    = {University of Isfahan},
  year      = {2022}
}
```
