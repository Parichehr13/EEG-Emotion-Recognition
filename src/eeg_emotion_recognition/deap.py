from __future__ import annotations

import io
import pickle as pkl
import zipfile
from pathlib import Path
from typing import Sequence

import numpy as np
from scipy import signal
from sklearn.preprocessing import StandardScaler


DEAP_SUBJECTS = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
]


def one_hot(values: np.ndarray, classes: int) -> np.ndarray:
    return np.eye(classes, dtype=np.float32)[values.astype(int)]


def deap_band_definitions(sampling_rate: int) -> dict[str, tuple[float, float]]:
    nyquist = sampling_rate / 2
    return {
        "delta": (0.5 / nyquist, 4 / nyquist),
        "theta": (4 / nyquist, 8 / nyquist),
        "alpha": (8 / nyquist, 14 / nyquist),
        "beta": (14 / nyquist, 30 / nyquist),
        "gamma": (30 / nyquist, 75 / nyquist),
    }


def _zip_member_name(names: list[str], subject: str) -> str:
    matches = [name for name in names if name.endswith(f"s{subject}.dat")]
    if not matches:
        raise FileNotFoundError(f"Could not find s{subject}.dat inside archive.")
    return matches[0]


def _load_subject_dict(source: Path, subject: str) -> dict:
    if source.suffix.lower() == ".zip":
        if "matlab" in source.name.lower():
            raise ValueError(
                "The DEAP notebook logic expects the Python preprocessed archive "
                "with .dat files, but the provided archive looks like the MATLAB release."
            )
        with zipfile.ZipFile(source) as zf:
            member = _zip_member_name(zf.namelist(), subject)
            with zf.open(member) as handle:
                data = handle.read()
        return pkl.load(io.BytesIO(data), encoding="latin1")

    dat_path = source / f"s{subject}.dat"
    if not dat_path.exists():
        raise FileNotFoundError(
            f"Expected {dat_path}. Point --source to an extracted DEAP Python-preprocessed directory."
        )
    with dat_path.open("rb") as handle:
        return pkl.load(handle, encoding="latin1")


def load_deap_band_data(
    source: Path,
    eeg_band: str = "alpha",
    subject_list: Sequence[str] = DEAP_SUBJECTS,
    sampling_rate: int = 128,
    window_size: int = 1280,
    step_size: int = 256,
    channel_len: int = 32,
) -> tuple[np.ndarray, dict[str, np.ndarray]]:
    bands = deap_band_definitions(sampling_rate)
    if eeg_band not in bands:
        raise ValueError(f"Unknown EEG band '{eeg_band}'. Expected one of {sorted(bands)}.")

    eeg_signal: list[np.ndarray] = []
    label_buffers = {
        "valence": [],
        "arousal": [],
        "dominance": [],
        "liking": [],
    }

    numerator, denominator = signal.butter(4, bands[eeg_band], "band")

    for subject in subject_list:
        subject_data = _load_subject_dict(source, subject)
        eeg = subject_data["data"]
        label = subject_data["labels"].copy()

        label[label < 5.5] = 0
        label[label >= 5.5] = 1

        targets = {
            "valence": label.T[0],
            "arousal": label.T[1],
            "dominance": label.T[2],
            "liking": label.T[3],
        }

        for trial_index in range(40):
            sig = eeg[trial_index].T[:, :channel_len]
            filtered = signal.filtfilt(numerator, denominator, sig, axis=0)
            scaled = StandardScaler().fit_transform(filtered)

            start = 0
            while start + window_size < scaled.shape[0]:
                eeg_signal.append(scaled[start : start + window_size, :].astype(np.float32))
                for key, values in targets.items():
                    label_buffers[key].append(int(values[trial_index]))
                start += step_size

    data = np.asarray(eeg_signal, dtype=np.float32)
    labels = {
        key: one_hot(np.asarray(values, dtype=np.int8), classes=2)
        for key, values in label_buffers.items()
    }
    return data, labels

