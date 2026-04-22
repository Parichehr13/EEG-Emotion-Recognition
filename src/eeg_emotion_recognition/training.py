from __future__ import annotations

import json
import random
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.callbacks import ReduceLROnPlateau


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)


def fit_model(
    model,
    x_train: np.ndarray,
    y_train: np.ndarray,
    *,
    batch_size: int,
    epochs: int,
    validation_split: float,
    min_lr: float,
    patience: int = 10,
):
    lr_reducer = ReduceLROnPlateau(
        monitor="val_loss",
        cooldown=0,
        patience=patience,
        min_lr=min_lr,
        factor=0.1,
        verbose=1,
    )
    return model.fit(
        x_train,
        y_train,
        epochs=epochs,
        validation_split=validation_split,
        batch_size=batch_size,
        shuffle=True,
        verbose=1,
        callbacks=[lr_reducer],
    )


def evaluate_model(model, x_test: np.ndarray, y_test: np.ndarray, target_names: list[str]) -> dict:
    scores = model.evaluate(x_test, y_test, batch_size=32, verbose=0)
    y_true = np.argmax(y_test, axis=1)
    y_pred = np.argmax(model.predict(x_test, verbose=0), axis=1)
    report = classification_report(
        y_true,
        y_pred,
        target_names=target_names,
        digits=4,
        output_dict=True,
        zero_division=0,
    )
    cm = confusion_matrix(y_true, y_pred)
    return {
        "test_loss": float(scores[0]),
        "test_accuracy": float(scores[1]),
        "classification_report": report,
        "confusion_matrix": cm,
    }


def save_run_outputs(output_dir: Path, history, metrics: dict, run_config: dict) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    pd.DataFrame(history.history).to_csv(output_dir / "history.csv", index=False)
    pd.DataFrame(metrics["confusion_matrix"]).to_csv(output_dir / "confusion_matrix.csv", index=False)

    with (output_dir / "classification_report.json").open("w", encoding="utf-8") as handle:
        json.dump(metrics["classification_report"], handle, indent=2)

    summary = {
        "test_loss": metrics["test_loss"],
        "test_accuracy": metrics["test_accuracy"],
    }
    with (output_dir / "metrics.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)

    with (output_dir / "run_config.json").open("w", encoding="utf-8") as handle:
        json.dump(run_config, handle, indent=2)

