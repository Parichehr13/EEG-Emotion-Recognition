# Data Setup

This repository does **not** redistribute DEAP or SEED data.

## Expected datasets

### DEAP

The DEAP notebook logic expects the **Python preprocessed release** with subject files such as `s01.dat`.

Supported inputs for the DEAP scripts:

- a `data_preprocessed_python.zip` archive
- an extracted directory containing `s01.dat` ... `s32.dat`

Important:
the local workspace used during this cleanup contains `Dataset/DEAP/data_preprocessed_matlab.zip`, which is **not** the format used by the original notebook loader.

Recommended local path:

```text
data/raw/deap/data_preprocessed_python.zip
```

### SEED

The SEED notebook logic uses the extracted-feature release, especially folders built from:

- feature types: `de`, `psd`, `dasm`, `rasm`, `asm`, `dcau`
- smoothing methods: `movingAve`, `LDS`

Supported inputs for the SEED scripts:

- `ExtractedFeatures.zip`
- an extracted directory containing `label.mat` and the trial `.mat` files

Recommended local path:

```text
data/raw/seed/ExtractedFeatures.zip
```

## Produced artifacts

Generated files should live outside version control, for example:

```text
data/
├── raw/
│   ├── deap/
│   └── seed/
├── interim/
└── processed/
    ├── deap/
    └── seed/
```

## Notes on labels

- DEAP labels are binarized at the notebook threshold of `5.5`.
- SEED labels are shifted by `+1` to map the original `-1/0/1` style labels to `0/1/2` before one-hot encoding.

