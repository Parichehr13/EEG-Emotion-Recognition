from __future__ import annotations

import argparse
import sys
from pathlib import Path

import optuna
from sklearn.model_selection import train_test_split

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from eeg_emotion_recognition.config import apply_json_config, dump_json
from eeg_emotion_recognition.deap import load_deap_band_data
from eeg_emotion_recognition.models import build_deap_optuna_model, compile_classification_model
from eeg_emotion_recognition.paths import default_deap_source
from eeg_emotion_recognition.training import set_seed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the DEAP Optuna search used in the thesis notebook.")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("--source", type=str, default=None)
    parser.add_argument("--task", type=str, default="valence", choices=["valence", "arousal", "dominance", "liking"])
    parser.add_argument("--band", type=str, default="alpha")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--n-trials", type=int, default=100)
    parser.add_argument("--test-size", type=float, default=0.2)
    parser.add_argument("--validation-split", type=float, default=0.15)
    parser.add_argument("--train-limit", type=int, default=5000)
    parser.add_argument("--test-limit", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--learning-rate", type=float, default=0.001)
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

    if args.train_limit:
        x_train = x_train[: args.train_limit]
        y_train = y_train[: args.train_limit]
    if args.test_limit:
        x_test = x_test[: args.test_limit]
        y_test = y_test[: args.test_limit]

    input_shape = (x_train.shape[1], x_train.shape[2])

    def objective(trial: optuna.Trial) -> float:
        model = build_deap_optuna_model(trial, input_shape=input_shape, classes=2)
        model = compile_classification_model(model, learning_rate=args.learning_rate)
        model.fit(
            x_train,
            y_train,
            validation_split=args.validation_split,
            shuffle=True,
            batch_size=args.batch_size,
            epochs=args.epochs,
            verbose=1,
        )
        score = model.evaluate(x_test, y_test, verbose=0)
        return float(score[1])

    sampler = optuna.samplers.NSGAIISampler(seed=args.seed)
    study = optuna.create_study(direction="maximize", sampler=sampler)
    study.optimize(objective, n_trials=args.n_trials)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    study.trials_dataframe().to_csv(output_dir / "trials.csv", index=False)
    dump_json(output_dir / "best_trial.json", {"value": study.best_trial.value, "params": study.best_trial.params})
    dump_json(
        output_dir / "run_config.json",
        {
            "dataset": "DEAP",
            "task": args.task,
            "band": args.band,
            "batch_size": args.batch_size,
            "epochs": args.epochs,
            "n_trials": args.n_trials,
            "test_size": args.test_size,
            "validation_split": args.validation_split,
            "train_limit": args.train_limit,
            "test_limit": args.test_limit,
            "seed": args.seed,
            "learning_rate": args.learning_rate,
            "source": str(source),
        },
    )

    print(f"Best DEAP {args.task} Optuna accuracy: {study.best_trial.value * 100:.4f}%")
    print(f"Best params: {study.best_trial.params}")


if __name__ == "__main__":
    main()

