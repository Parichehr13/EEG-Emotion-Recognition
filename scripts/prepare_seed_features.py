from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from eeg_emotion_recognition.config import apply_json_config
from eeg_emotion_recognition.paths import default_seed_source
from eeg_emotion_recognition.seed import build_seed_feature_arrays, extract_if_zip


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare SEED feature arrays from the extracted-feature release.")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("--source", type=str, default=None, help="ExtractedFeatures.zip or extracted directory.")
    parser.add_argument("--extract-dir", type=str, default="data/interim/seed_extracted")
    parser.add_argument("--feature-type", type=str, default="de")
    parser.add_argument("--smooth-method", type=str, default="movingAve")
    parser.add_argument("--output-dir", type=str, required=True)
    args = parser.parse_args()
    return apply_json_config(parser, args)


def main() -> None:
    args = parse_args()
    source = Path(args.source) if args.source else default_seed_source()
    if source is None:
        raise FileNotFoundError("Could not find a SEED source. Use --source to provide ExtractedFeatures.zip.")

    root_dir = extract_if_zip(source, Path(args.extract_dir))
    payload = build_seed_feature_arrays(
        root_dir=root_dir,
        output_dir=Path(args.output_dir),
        feature_type=args.feature_type,
        smooth_method=args.smooth_method,
    )
    print(f"Saved SEED arrays to {args.output_dir}")
    print(f"Feature shape: {payload['feature'].shape}")
    print(f"Label shape: {payload['label'].shape}")


if __name__ == "__main__":
    main()

