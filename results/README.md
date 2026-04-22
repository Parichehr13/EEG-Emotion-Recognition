# Results

This directory intentionally separates:

- `reported_metrics.csv`
  - reported selected-run results extracted from notebook outputs / thesis materials
  - not independently rerun in this environment
- `legacy/`
  - archived artifacts copied from the original working directory

Future reproducible script outputs should be written under:

```text
results/runs/<experiment_name>/
```

Recommended outputs per run:

- `metrics.json`
- `classification_report.json`
- `confusion_matrix.csv`
- `history.csv`
- `run_config.json`

