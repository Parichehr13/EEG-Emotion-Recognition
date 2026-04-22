from __future__ import annotations

import argparse
import sys
from pathlib import Path

from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from eeg_emotion_recognition.config import apply_json_config
from eeg_emotion_recognition.deap import load_deap_band_data
from eeg_emotion_recognition.models import (
    build_deap_baseline_model,
    build_deap_selected_model,
    compile_classification_model,
)
from eeg_emotion_recognition.paths import default_deap_source
from eeg_emotion_recognition.training import evaluate_model, fit_model, save_run_outputs, set_seed


TARGET_NAMES = ["Low", "High"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a DEAP CNN from the thesis workflow.")
    parser.add_argument("--config", type=str, default=None, help="Optional JSON config file.")
    parser.add_argument("--source", type=str, default=None, help="DEAP Python-preprocessed zip or directory.")
    parser.add_argument("--task", type=str, default="valence", choices=["valence", "arousal", "dominance", "liking"])
    parser.add_argument("--band", type=str, default="alpha")
    parser.add_argument("--model-variant", type=str, default="selected", choices=["baseline", "selected"])
    parser.add_argument("--batch-size", type=int, default=512)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--validation-split", type=float, default=0.15)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--learning-rate", type=float, default=0.001)
    parser.add_argument("--min-lr", type=float, default=1e-4)
    parser.add_argument("--output-dir", type=str, required=True)
    args = parser.parse_args()
    return apply_json_config(parser, args)


def main() -> None:
    args = parse_args()
    set_seed(args.seed)

    source = Path(args.source) if args.source else default_deap_source()
    if source is None:
        raise FileNotFoundError("Could not find a DEAP source. Use --source to provide the Python-preprocessed archive.")

    data, labels = load_deap_band_data(source=source, eeg_band=args.band)
    y = labels[args.task]

    x_train, x_test, y_train, y_test = train_test_split(
        data,
        y,
        test_size=args.test_size,
        random_state=args.seed,
    )

    input_shape = (x_train.shape[1], x_train.shape[2])
    if args.model_variant == "baseline":
        model = build_deap_baseline_model(input_shape=input_shape, classes=2)
    else:
        model = build_deap_selected_model(input_shape=input_shape, classes=2)
    model = compile_classification_model(model, learning_rate=args.learning_rate)

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
            "dataset": "DEAP",
            "task": args.task,
            "band": args.band,
            "model_variant": args.model_variant,
            "batch_size": args.batch_size,
            "epochs": args.epochs,
            "test_size": args.test_size,
            "validation_split": args.validation_split,
            "seed": args.seed,
            "learning_rate": args.learning_rate,
            "source": str(source),
        },
    )

    print(f"DEAP {args.task} test accuracy: {metrics['test_accuracy'] * 100:.4f}%")


if __name__ == "__main__":
    main()

