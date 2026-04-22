from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from eeg_emotion_recognition.config import apply_json_config
from eeg_emotion_recognition.models import build_seed_model, compile_classification_model
from eeg_emotion_recognition.seed import load_seed_numpy_arrays, prepare_seed_training_arrays
from eeg_emotion_recognition.training import evaluate_model, fit_model, save_run_outputs, set_seed


TARGET_NAMES = ["Negative", "Neutral", "Positive"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train the SEED CNN from prepared numpy arrays.")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("--source-dir", type=str, required=True, help="Directory containing feature.npy and label.npy.")
    parser.add_argument("--batch-size", type=int, default=512)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--test-size", type=float, default=0.1)
    parser.add_argument("--validation-split", type=float, default=0.15)
    parser.add_argument("--seed", type=int, default=100)
    parser.add_argument("--learning-rate", type=float, default=0.0001)
    parser.add_argument("--min-lr", type=float, default=1e-7)
    parser.add_argument("--output-dir", type=str, required=True)
    args = parser.parse_args()
    return apply_json_config(parser, args)


def main() -> None:
    args = parse_args()
    set_seed(args.seed)

    source_dir = Path(args.source_dir)
    feature, label, _ = load_seed_numpy_arrays(source_dir)
    x, y = prepare_seed_training_arrays(feature, label)

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=args.test_size,
        random_state=args.seed,
    )

    input_shape = (x_train.shape[1], x_train.shape[2])
    model = build_seed_model(input_shape=input_shape, classes=3)
    model = compile_classification_model(model, learning_rate=args.learning_rate, decay=0.0)

    history = fit_model(
        model,
        x_train,
        y_train,
        batch_size=args.batch_size,
        epochs=args.epochs,
        validation_split=args.validation_split,
        min_lr=args.min_lr,
    )
    metrics = evaluate_model(model, x_test, y_test, target_names=TARGET_NAMES)
    save_run_outputs(
        Path(args.output_dir),
        history,
        metrics,
        {
            "dataset": "SEED",
            "feature_source": str(source_dir),
            "batch_size": args.batch_size,
            "epochs": args.epochs,
            "test_size": args.test_size,
            "validation_split": args.validation_split,
            "seed": args.seed,
            "learning_rate": args.learning_rate,
        },
    )

    print(f"SEED test accuracy: {metrics['test_accuracy'] * 100:.4f}%")


if __name__ == "__main__":
    main()
