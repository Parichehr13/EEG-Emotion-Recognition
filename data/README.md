# EEG Emotion Recognition

This repository contains my work on EEG-based emotion recognition using deep learning and evolutionary hyperparameter optimization.

The project focuses on classifying affective states from electroencephalography (EEG) signals, with experiments designed around two widely used public datasets: **DEAP** and **SEED**.

## Overview

Emotion recognition from EEG is an important problem in affective computing, brain-computer interfaces, and human-computer interaction. In this project, EEG signals are used to learn discriminative representations of human emotional states, and a convolutional neural network (CNN) based framework is optimized to improve classification performance.

Because the datasets used in this work are large and have their own access conditions, they are **not included in this GitHub repository**. Instead, this repository provides the code, notebooks, and documentation needed to reproduce the experiments once the datasets are obtained from their official sources.

## Datasets

### 1. DEAP Dataset

The **DEAP** dataset is a well-known multimodal benchmark for emotion analysis using physiological signals. It was created to support research on affective state recognition from bodily responses during multimedia stimulation.

In DEAP, participants watched short music video excerpts designed to elicit emotional responses. During each trial, physiological data were recorded and participants reported their subjective emotional experience. The dataset is especially valuable because it combines brain activity with self-assessed emotional labels, making it suitable for supervised learning in emotion recognition tasks.

#### Main Characteristics of DEAP

- 32 participants
- 40 one-minute music video trials per participant
- 32-channel EEG recordings
- Additional peripheral physiological signals
- Self-assessment labels including:
- **Valence**
- **Arousal**
- **Dominance**
- **Liking**
- **Familiarity**

#### Why DEAP Is Important

DEAP is one of the most widely used public datasets for EEG-based affective computing. It provides a standardized benchmark for evaluating machine learning and deep learning methods on emotional dimensions such as valence and arousal, and it is particularly useful for comparing results across studies.

#### Access

The dataset is not redistributed in this repository. Please obtain it from the official DEAP source and follow its license and usage terms.

---

### 2. SEED Dataset

The **SEED** dataset is another widely used public dataset for EEG-based emotion recognition. It was developed to study human emotional responses induced by film clips and has become a standard benchmark for EEG classification of discrete emotional states.

In the original SEED dataset, subjects watched carefully selected film clips intended to evoke **positive**, **neutral**, and **negative** emotions. EEG signals were recorded during these sessions, and part of the dataset also includes eye-movement information, making it useful for both unimodal and multimodal emotion recognition research.

#### Main Characteristics of SEED

- 15 subjects in total
- 12 subjects with both EEG and eye-movement data
- 3 additional subjects with EEG only
- Emotion classes:
- **Positive**
- **Neutral**
- **Negative**
- Data collected across **three sessions** for each subject
- Preprocessed EEG and extracted feature files are available from the official dataset source

#### Why SEED Is Important

SEED is especially useful for studying EEG-based recognition of discrete emotions. It is commonly used in research on subject-dependent and subject-independent emotion classification, feature engineering, and deep learning methods for affective brain-computer interfaces.

#### Access

The dataset is not redistributed in this repository. Please request or download it from the official SEED dataset website and respect its data access policy.

---

## Why The Datasets Are Not Included In This Repository

The datasets used in this project are **large** and may also be subject to **distribution, licensing, or access restrictions** from their original providers. For that reason, this repository includes only the implementation and documentation, not the raw dataset files.

This keeps the repository lightweight, easier to clone, and compliant with dataset usage conditions.

## How The Datasets Are Used In This Project

This project uses **DEAP** and **SEED** to evaluate EEG-based emotion recognition models.

In the thesis associated with this repository, both datasets are used for **training and evaluation** of a CNN-based framework whose hyperparameters are optimized using an evolutionary multi-objective strategy. The experiments focus on improving classification performance for different emotional targets.

For **DEAP**, the work evaluates emotion recognition on:

- Valence
- Arousal
- Dominance
- Liking

For **SEED**, the work evaluates classification of:

- Positive
- Neutral
- Negative emotional states

## Repository Structure

```text
EEG-Emotion-Recognition/
|-- ER_with_EEG.ipynb
|-- figures/
|-- data/
|   |-- README.md
|-- README.md
```

## Dataset Setup

After obtaining the datasets from their official sources, place them locally in a directory structure similar to the following:

```text
data/
|-- Dataset/
|   |-- DEAP/
|   `-- SEED/
```

> Note: The `data/` directory should remain local for dataset contents and should not be used to push raw dataset files to GitHub.

## Research Context

This repository is based on my thesis work on **EEG-based emotion recognition using evolutionary computation for hyperparameter optimization**. The main goal is to improve deep neural network performance by automatically searching for better model configurations instead of relying only on manually selected hyperparameters.

The study uses public benchmark datasets to evaluate the proposed method and compare its performance with existing approaches in the literature.

## Results Summary

According to the thesis experiments, the proposed method achieved strong classification performance on both datasets.

### DEAP

Reported test accuracy:

- **Valence:** 96.46%
- **Arousal:** 97.54%
- **Dominance:** 98.18%
- **Liking:** 98.10%

### SEED

Reported best recognition accuracy:

- **96.14%**

These results indicate that the proposed framework is effective for EEG-based emotion recognition on both dimensional and discrete emotion benchmarks.

## Citation And Acknowledgement

If you use the datasets, please cite the original dataset creators and follow their official terms of use.

If you use or reference this repository, please also acknowledge the related thesis work.

## References

- DEAP: A Database for Emotion Analysis using Physiological Signals
- SEED Dataset, BCMI Laboratory, Shanghai Jiao Tong University
- Thesis: *EEG-Based Emotion Recognition Using Convolutional Neural Networks and Hyperparameter Optimization*

## Notes

- This repository does **not** contain the DEAP or SEED dataset files.
- Please download the datasets only from their official providers.
- If you use this code, make sure your local paths match the dataset directory structure used in the notebooks or scripts.
