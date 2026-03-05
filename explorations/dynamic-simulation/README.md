# Dynamic Model Simulation

Numerical solution of the dynamic investment/insurance problem from the
intrahousehold public goods model (Section 2 of the paper).

## What this does

1. Solves the Bellman equation via value function iteration (VFI)
2. Extracts policy functions for investment $s^*(w_i)$ and insurance $q^*(w_i)$
3. Generates publication-quality figures showing regime-dependent behavior

## Usage

```bash
pip install -r ../../requirements.txt
python run.py
```

Figures are saved to `output/`.

## Status

Exploration -- not yet graduated to `scripts/`.
