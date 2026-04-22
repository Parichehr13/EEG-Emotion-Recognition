from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def first_existing_path(candidates: list[str]) -> Path | None:
    for candidate in candidates:
        path = PROJECT_ROOT / candidate
        if path.exists():
            return path
    return None


def default_deap_source() -> Path | None:
    return first_existing_path(
        [
            "data/raw/deap/data_preprocessed_python.zip",
            "Dataset/DEAP/data_preprocessed_python.zip",
            "data/raw/deap/data_preprocessed_python",
            "Dataset/DEAP/data_preprocessed_python",
            "Dataset/DEAP/data_preprocessed_matlab.zip",
        ]
    )


def default_seed_source() -> Path | None:
    return first_existing_path(
        [
            "data/raw/seed/ExtractedFeatures.zip",
            "Dataset/SEED/ExtractedFeatures.zip",
            "data/raw/seed/ExtractedFeatures",
        ]
    )

