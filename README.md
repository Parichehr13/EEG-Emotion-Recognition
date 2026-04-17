# EEG Emotion Recognition

<p align="center">
  <img src="figures/ER_with_EEG/figure_08_cell084_cnn-model__5th-layer-i-e-dense2-hpo__training-and-evaluation.png" alt="Optimized CNN architecture" width="320">
</p>

EEG-based emotion recognition using convolutional neural networks, public benchmark datasets, and hyperparameter optimization for affective state classification.

This repository presents my work on **emotion recognition from electroencephalography (EEG)**. It is based on my master's thesis and includes the main experimental notebook, exported figures, and documentation for experiments built around the **DEAP** and **SEED** datasets.

The current implementation is notebook-based and preserves the workflow close to its original research form.

## Overview

Emotion recognition from EEG is an important problem in affective computing, brain-computer interfaces, and human-computer interaction. Compared with surface-level signals such as facial expressions or speech, EEG offers a more direct physiological view of emotional processing.

In this project, I study EEG-based emotion classification with a compact **1D CNN** and compare it with several classical machine learning baselines. The work focuses on building a full pipeline from preprocessing to classification and improving performance through hyperparameter tuning.

## Project Goals

- Build an EEG-based emotion recognition pipeline
- Preprocess and relabel public benchmark datasets for classification
- Train a compact CNN for emotion recognition
- Improve model performance through hyperparameter optimization
- Evaluate both binary and multi-class emotion recognition tasks
- Compare deep learning results with classical ML baselines

## Repository Contents

```text
EEG-Emotion-Recognition/
|-- ER_with_EEG.ipynb
|-- data/
|   `-- README.md
|-- figures/
|   `-- ER_with_EEG/
|       |-- README.md
|       `-- manifest.json
|-- .gitignore
|-- LICENSE
`-- README.md
```

## Main Files

- `ER_with_EEG.ipynb`: main notebook containing preprocessing, model definition, training, evaluation, and baseline experiments
- `figures/ER_with_EEG/`: exported notebook figures including architecture visuals, learning curves, and confusion matrices
- `data/README.md`: dataset notes, access guidance, and expected local folder layout

## Workflow Summary

At a high level, the project follows four stages:

1. EEG signal loading
2. Preprocessing and relabeling
3. CNN-based learning and baseline comparison
4. Emotion classification and evaluation

The repository covers:

- **DEAP** for binary emotion classification across multiple affective dimensions
- **SEED** for three-class emotion recognition

## Datasets

### DEAP

The **DEAP** dataset is a widely used benchmark for emotion analysis using physiological signals. In this project, it is used for binary classification on multiple emotional dimensions.

Main characteristics:

- 32 participants
- 40 trials per participant
- 32 EEG channels used in this project
- Target dimensions: valence, arousal, dominance, and liking

How DEAP is used in this repository:

- Loads the original `.dat` subject files
- Keeps the 32 EEG channels
- Applies Butterworth band-pass filtering
- Uses the alpha band in the current notebook workflow
- Binarizes labels using a 5.5 threshold
- Segments each trial into 10-second windows
- Uses 2-second overlap
- Standardizes each segmented signal before training

This preprocessing supports four binary classification tasks:

- Low vs high valence
- Low vs high arousal
- Low vs high dominance
- Disliking vs liking

### SEED

The **SEED** dataset is a public EEG emotion dataset for recognizing discrete emotions induced by film clips.

Main characteristics:

- 15 subjects
- 3 emotion classes: negative, neutral, and positive

How SEED is used in this repository:

- Uses extracted features rather than raw EEG time series
- Works with official extracted feature files and reshapes them for CNN training
- Documents feature types such as DE, PSD, DASM, RASM, ASM, and DCAU
- Includes smoothing methods such as moving average and LDS
- Uses a working configuration based on differential entropy features
- Uses input vectors of 310 dimensions per sample

The final SEED experiment is a three-class classification task:

- Negative
- Neutral
- Positive

## Dataset Access

The datasets are **not included** in this repository.

They are large and may also have their own access and redistribution conditions, so this repository contains the code, figures, and documentation only. Please obtain the datasets from their official sources:

- **DEAP**: https://www.eecs.qmul.ac.uk/mmv/datasets/deap/
- **SEED**: https://bcmi.sjtu.edu.cn/home/seed/index.html

See [data/README.md](data/README.md) for additional dataset notes and the recommended local folder structure.

## Methodology

### Preprocessing

The preprocessing stage organizes EEG signals into model-ready inputs and labels. Depending on the dataset, the workflow includes:

- segmentation into analysis windows
- relabeling into target emotion classes
- band-based EEG representation
- train, validation, and test splitting

### CNN-Based Learning

The main deep learning model used in this project is a compact **1D CNN**.

High-level architecture:

1. Conv1D
2. AveragePooling1D
3. BatchNormalization
4. Conv1D
5. AveragePooling1D
6. BatchNormalization
7. Conv1D
8. GlobalAveragePooling1D
9. BatchNormalization
10. Dropout
11. Dense
12. Dense
13. Dropout
14. Softmax output

Optimized configuration used in the notebook:

- `C1`: 32 filters, kernel size 2, stride 1, padding `same`, ReLU
- `C2`: 128 filters, kernel size 5, stride 1, padding `same`, ReLU
- `C3`: 192 filters, kernel size 3, stride 2, padding `same`, ReLU
- `FC1`: 64 units, `tanh`
- `FC2`: 8 units, `tanh`
- Dropout: 0.2 and 0.1

### Hyperparameter Optimization

A major part of this project is improving CNN performance through hyperparameter tuning.

The notebook includes layer-wise hyperparameter search using **Optuna**, while the broader thesis context is motivated by evolutionary optimization ideas for CNN design in EEG emotion recognition.

The tuning workflow covers:

- 1st convolution layer (`C1`)
- 2nd convolution layer (`C2`)
- 3rd convolution layer (`C3`)
- 1st dense layer (`FC1`)
- 2nd dense layer (`FC2`)

### Classical ML Baselines

The notebook also evaluates several traditional machine learning methods on DEAP:

- LDA
- SVM
- Random Forest
- MLP
- KNN

These experiments provide a comparison point for the CNN-based approach.

## Training Setup

### DEAP

- Input shape: `(1280, 32)`
- Train/test split: `80/20`
- Validation split during training: `15%`
- Tasks: valence, arousal, dominance, and liking

### SEED

- Input shape: `(310, 1)`
- Train/test split: `90/10`
- Validation split during training: `15%`
- Task: negative / neutral / positive

## Results

### Summary Table

| Dataset | Task | Test Accuracy |
|---|---|---:|
| DEAP | Valence | **96.47%** |
| DEAP | Arousal | **97.54%** |
| DEAP | Dominance | **98.18%** |
| DEAP | Liking | **98.10%** |
| SEED | Negative / Neutral / Positive | **96.14%** |

These results are consistent with the performance reported in the associated thesis experiments.

## Example Figures

### Architecture Figure

<p align="center">
  <img src="figures/ER_with_EEG/figure_08_cell084_cnn-model__5th-layer-i-e-dense2-hpo__training-and-evaluation.png" alt="Optimized CNN architecture" width="320">
</p>

### DEAP Valence Confusion Matrix

<p align="center">
  <img src="figures/ER_with_EEG/figure_12_cell097_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="DEAP valence confusion matrix" width="520">
</p>

### DEAP Arousal Confusion Matrix

<p align="center">
  <img src="figures/ER_with_EEG/figure_20_cell117_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="DEAP arousal confusion matrix" width="520">
</p>

### DEAP Dominance Confusion Matrix

<p align="center">
  <img src="figures/ER_with_EEG/figure_28_cell137_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="DEAP dominance confusion matrix" width="520">
</p>

### DEAP Liking Confusion Matrix

<p align="center">
  <img src="figures/ER_with_EEG/figure_36_cell157_training-and-evaluation__training-and-evaluation-with-std-calculation__training-and-evaluation-with-std-calculation.png" alt="DEAP liking confusion matrix" width="520">
</p>

### SEED Three-Class Confusion Matrix

<p align="center">
  <img src="figures/ER_with_EEG/figure_48_cell200_training-and-evaluation__loading-and-pre-processing-seed-dataset__training-and-evaluation.png" alt="SEED confusion matrix" width="520">
</p>

## Key Observations

- The optimized CNN performs strongly on both datasets
- The DEAP tasks achieve high binary classification accuracy across all four emotional dimensions
- The SEED experiment achieves strong multi-class performance
- The CNN outperforms the classical ML baselines included in the notebook
- Careful preprocessing and model tuning are important for EEG emotion recognition

## How To Run

Because the notebook was originally written in **Google Colab**, some paths and commands are still Colab-specific.

Current notebook notes:

- `drive.mount('/content/drive')`
- `!pip install ...`
- hardcoded `/content/...` paths
- Google Drive save/load paths for intermediate arrays

To run locally, you will likely need to:

1. Download the datasets manually from their official sources
2. Replace Google Drive and Colab paths with local project paths
3. Update unzip commands and file-loading paths
4. Install the required Python packages locally
5. Rerun the notebook step by step

Suggested environment:

```bash
pip install numpy scipy matplotlib scikit-learn tensorflow optuna pydot graphviz notebook jupyter
```

## Reproducibility Notes

This repository preserves the notebook close to its original research form. That is useful for transparency, but it also means the project is not yet fully packaged as a clean Python module.

Potential next cleanup steps:

- Move preprocessing into reusable Python scripts
- Replace hardcoded Colab paths with relative paths
- Add a `requirements.txt`
- Add dataset path configuration
- Separate training utilities from analysis cells
- Export final model checkpoints and logs in a cleaner structure

## Why This Project Matters

Emotion recognition from EEG is relevant to several active research and application areas:

- Affective computing
- Brain-computer interfaces
- Human-computer interaction
- Adaptive intelligent systems
- Mental health and assistive technologies

Compared with surface-level behavioral signals, EEG provides a physiological signal that can capture internal emotional dynamics more directly.

## Research Background

This project is based on my master's thesis:

**Using Evolutionary Computation Algorithms for EEG-Based Emotion Recognition**

The thesis studies deep learning for EEG emotion recognition and focuses on improving CNN design through hyperparameter optimization. It evaluates the method on DEAP and SEED and reports strong results for both datasets.

## Citation

If you use this repository, please cite the original datasets and acknowledge the related thesis work.

Suggested acknowledgement:

> This repository is based on thesis work on EEG-based emotion recognition using CNNs and hyperparameter optimization, evaluated on the DEAP and SEED datasets.

Suggested BibTeX entry:

```bibtex
@mastersthesis{moradi2022eegemotion,
  title     = {Using Evolutionary Computation Algorithms for EEG-Based Emotion Recognition},
  author    = {Moradi, Parichehr},
  school    = {University of Isfahan},
  year      = {2022}
}
```

## Acknowledgements

- DEAP dataset creators
- SEED dataset creators
- University of Isfahan
- Thesis supervisor and academic collaborators

## Future Work

- Refactor the notebook into a modular Python project
- Support direct raw EEG pipelines for SEED
- Run cross-subject and subject-independent evaluations
- Compare additional architectures such as LSTM, EEGNet, and transformer-based models
- Add experiment tracking and reproducible configuration files
- Explore cross-dataset generalization and explainability for EEG features

## Author

**Parichehr Moradi**  
Biomedical Engineering Researcher  
Focus areas: EEG, affective computing, deep learning, biomedical signal analysis

## License

This repository is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

## Data Note

This repository does **not** redistribute the DEAP or SEED datasets. Please follow the original dataset licenses and access policies when using them.
