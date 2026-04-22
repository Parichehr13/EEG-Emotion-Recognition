from __future__ import annotations

import json
from argparse import ArgumentParser, Namespace
from pathlib import Path


def apply_json_config(parser: ArgumentParser, args: Namespace) -> Namespace:
    config_path = getattr(args, "config", None)
    if not config_path:
        return args

    data = json.loads(Path(config_path).read_text(encoding="utf-8"))
    defaults = {
        action.dest: action.default
        for action in parser._actions
        if action.dest != "help"
    }

    for key, value in data.items():
        if hasattr(args, key) and getattr(args, key) == defaults.get(key):
            setattr(args, key, value)

    return args


def dump_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

