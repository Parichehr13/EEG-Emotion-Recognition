from __future__ import annotations

import zipfile
from pathlib import Path

import numpy as np
from scipy.io import loadmat
from sklearn.preprocessing import StandardScaler


FEATURE_TYPES = ["de", "psd", "dasm", "rasm", "asm", "dcau"]
SMOOTH_METHODS = ["movingAve", "LDS"]


def extract_if_zip(source: Path, extract_dir: Path) -> Path:
    if source.is_dir():
        return source

    extract_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(source) as zf:
        zf.extractall(extract_dir)

    mat_roots = [path.parent for path in extract_dir.rglob("label.mat")]
    if not mat_roots:
        raise FileNotFoundError("Could not locate label.mat after extracting SEED features.")
    return mat_roots[0]


def build_seed_feature_arrays(
    root_dir: Path,
    output_dir: Path,
    feature_type: str,
    smooth_method: str,
    num_subjects: int = 15,
    num_experiments: int = 15,
) -> dict[str, np.ndarray]:
    if feature_type not in FEATURE_TYPES:
        raise ValueError(f"Unknown feature_type '{feature_type}'.")
    if smooth_method not in SMOOTH_METHODS:
        raise ValueError(f"Unknown smooth_method '{smooth_method}'.")

    label_path = root_dir / "label.mat"
    labels = loadmat(label_path)["label"][0] + 1

    stacked_arr = None
    stacked_label = None
    cumulative_samples = [0]

    for subject_index in range(num_subjects):
        subject_prefix = f"{subject_index + 1}_"
        for trial_path in sorted(root_dir.iterdir()):
            if not trial_path.name.startswith(subject_prefix) or trial_path.suffix.lower() != ".mat":
                continue

            feature_dict = loadmat(trial_path)
            for experiment_index in range(num_experiments):
                key = f"{feature_type}_{smooth_method}{experiment_index + 1}"
                values = feature_dict[key]
                temp_arr = np.swapaxes(values, 0, 1).reshape(values.shape[1], -1)
                num_samples = temp_arr.shape[0]
                cumulative_samples.append(cumulative_samples[-1] + num_samples)
                temp_labels = np.full((num_samples, 1), labels[experiment_index], dtype=np.int32)

                if stacked_arr is None:
                    stacked_arr = temp_arr.copy()
                    stacked_label = temp_labels.copy()
                else:
                    stacked_arr = np.vstack((stacked_arr, temp_arr))
                    stacked_label = np.vstack((stacked_label, temp_labels))

    if stacked_arr is None or stacked_label is None:
        raise RuntimeError("No SEED feature arrays were constructed. Check the source directory.")

    output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "feature": stacked_arr,
        "label": stacked_label,
        "cumulative": np.asarray(cumulative_samples, dtype=np.int64),
    }
    np.save(output_dir / "feature.npy", payload["feature"])
    np.save(output_dir / "label.npy", payload["label"])
    np.save(output_dir / "cumulative.npy", payload["cumulative"])
    return payload


def load_seed_numpy_arrays(source_dir: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    feature = np.load(source_dir / "feature.npy")
    label = np.load(source_dir / "label.npy")
    cumulative = np.load(source_dir / "cumulative.npy")
    return feature, label, cumulative


def prepare_seed_training_arrays(feature: np.ndarray, label: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    scaled = StandardScaler().fit_transform(feature)
    x = scaled.reshape(-1, feature.shape[1], 1).astype(np.float32)
    y = np.eye(3, dtype=np.float32)[label.astype(int).ravel()]
    return x, y

